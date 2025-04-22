"""
MIT License

Copyright (c) 2023 Ulster University (https://www.ulster.ac.uk).
Project: Harmony (https://harmonydata.ac.uk)
Maintainer: Thomas Wood (https://fastdatascience.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import copy
import uuid
from typing import Annotated
from typing import List

from fastapi import APIRouter, Body, status, Depends, Query
from harmony.matching.default_matcher import match_instruments_with_function
from harmony.matching.matcher import (
    match_instruments_with_catalogue_instruments,
    match_query_with_catalogue_instruments,
)
from harmony.parsing.wrapper_all_parsers import convert_files_to_instruments
from harmony.schemas.requests.text import (
    RawFile,
    Instrument,
    MatchBody,
    SearchInstrumentsBody,
)
from harmony.schemas.responses.text import (
    MatchResponse,
    CacheResponse,
    SearchInstrumentsResponse,
)

from harmony.schemas.enums.clustering_algorithms import ClusteringAlgorithm
from harmony_api import helpers, dependencies, constants
from harmony_api import http_exceptions
from harmony_api.core.settings import get_settings
from harmony_api.services.instruments_cache import InstrumentsCache
from harmony_api.services.vectors_cache import VectorsCache

settings = get_settings()

router = APIRouter(prefix="/text")

# Cache
instruments_cache = InstrumentsCache()
vectors_cache = VectorsCache()

# Catalogue data
print("INFO:\t  Loading catalogue data...")
catalogue_data_default = helpers.get_catalogue_data_default()
catalogue_data_embeddings_for_model = {}
for harmony_api_model in constants.ALL_HARMONY_API_MODELS:
    catalogue_embeddings_for_model = helpers.get_catalogue_data_model_embeddings(
        harmony_api_model
    )
    catalogue_data_embeddings_for_model[harmony_api_model["model"]] = (
        catalogue_embeddings_for_model
    )


@router.post(path="/parse", response_model_exclude_none=True)
def parse_instruments(
        files: Annotated[
            List[RawFile],
            Body(
                examples={
                    "pdf": {
                        "summary": "PDF document",
                        "description": "A tiny PDF file in MIME+Base 64 with some plain text containing two of the GAD-7 items.",
                        "value": [
                            {
                                "file_id": "d39f31718513413fbfc620c6b6135d0c",
                                "file_name": "GAD-7.pdf",
                                "file_type": "pdf",
                                "content": "data:application/pdf;base64,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ZXJpZgovQ0lEU3lzdGVtSW5mbyA8PCAvUmVnaXN0cnkgKEFkb2JlKSAvT3JkZXJpbmcgKElkZW50aXR5KSAvU3VwcGxlbWVudCAwID4+Ci9Gb250RGVzY3JpcHRvciAxMiAwIFIKL0NJRFRvR0lETWFwIC9JZGVudGl0eQovVyBbMCBbNjAwIDYzNiAzMTggMzE4IDY5NCA1OTIgMzIwIDMyMCA2NDQgNjQwIDQ3OCA1NjUgNjAyIDY0NCA1MTMgMzE4IDU5NiA1NjQgNjQwIDYzNiA4NzUgNDAyIDY0MCA2NDAgNTYwIDg1NiA1NjUgXQpdCj4+CmVuZG9iagoxNSAwIG9iago8PCAvTGVuZ3RoIDU0NiA+PgpzdHJlYW0KL0NJREluaXQgL1Byb2NTZXQgZmluZHJlc291cmNlIGJlZ2luCjEyIGRpY3QgYmVnaW4KYmVnaW5jbWFwCi9DSURTeXN0ZW1JbmZvIDw8IC9SZWdpc3RyeSAoQWRvYmUpIC9PcmRlcmluZyAoVUNTKSAvU3VwcGxlbWVudCAwID4+IGRlZgovQ01hcE5hbWUgL0Fkb2JlLUlkZW50aXR5LVVDUyBkZWYKL0NNYXBUeXBlIDIgZGVmCjEgYmVnaW5jb2Rlc3BhY2VyYW5nZQo8MDAwMD4gPEZGRkY+CmVuZGNvZGVzcGFjZXJhbmdlCjIgYmVnaW5iZnJhbmdlCjwwMDAwPiA8MDAwMD4gPDAwMDA+CjwwMDAxPiA8MDAxQT4gWzwwMDMxPiA8MDAyRT4gPDAwMDk+IDwwMDQ2PiA8MDA2NT4gPDAwNkM+IDwwMDY5PiA8MDA2RT4gPDAwNjc+IDwwMDcyPiA8MDA3Nj4gPDAwNkY+IDwwMDc1PiA8MDA3Mz4gPDAwMkM+IDwwMDYxPiA8MDA3OD4gPDAwNjQ+IDwwMDMyPiA8MDA0RT4gPDAwNzQ+IDwwMDYyPiA8MDA3MD4gPDAwNjM+IDwwMDc3PiA8MDA3OT4gXQplbmRiZnJhbmdlCmVuZGNtYXAKQ01hcE5hbWUgY3VycmVudGRpY3QgL0NNYXAgZGVmaW5lcmVzb3VyY2UgcG9wCmVuZAplbmQKCmVuZHN0cmVhbQplbmRvYmoKNyAwIG9iago8PCAvVHlwZSAvRm9udAovU3VidHlwZSAvVHlwZTAKL0Jhc2VGb250IC9EZWphVnVTZXJpZgovRW5jb2RpbmcgL0lkZW50aXR5LUgKL0Rlc2NlbmRhbnRGb250cyBbMTQgMCBSXQovVG9Vbmljb2RlIDE1IDAgUj4+CmVuZG9iagoxNiAwIG9iago8PAovTGVuZ3RoIDQKPj4Kc3RyZWFtCv///+AKZW5kc3RyZWFtCmVuZG9iagozIDAgb2JqCjw8Ci9UeXBlIC9QYWdlcwovS2lkcyAKWwo2IDAgUgpdCi9Db3VudCAxCi9Qcm9jU2V0IFsvUERGIC9UZXh0IC9JbWFnZUIgL0ltYWdlQ10KPj4KZW5kb2JqCnhyZWYKMCAxOAowMDAwMDAwMDAwIDY1NTM1IGYgCjAwMDAwMDAwMTUgMDAwMDAgbiAKMDAwMDAwMDE2OSAwMDAwMCBuIAowMDAwMDA4MjQzIDAwMDAwIG4gCjAwMDAwMDAyMTggMDAwMDAgbiAKMDAwMDAwMDMxMyAwMDAwMCBuIAowMDAwMDAwMzUwIDAwMDAwIG4gCjAwMDAwMDgwNTIgMDAwMDAgbiAKMDAwMDAwMDY3MCAwMDAwMCBuIAowMDAwMDAxMjQ0IDAwMDAwIG4gCjAwMDAwMDA0ODQgMDAwMDAgbiAKMDAwMDAwMDY1MCAwMDAwMCBuIAowMDAwMDAxMjYzIDAwMDAwIG4gCjAwMDAwMDE1MzkgMDAwMDAgbiAKMDAwMDAwNzEzNSAwMDAwMCBuIAowMDAwMDA3NDU0IDAwMDAwIG4gCjAwMDAwMDgxODkgMDAwMDAgbiAKMDAwMDAwNzExNCAwMDAwMCBuIAp0cmFpbGVyCjw8Ci9TaXplIDE4IAovSW5mbyAxIDAgUgovUm9vdCAyIDAgUgo+PgpzdGFydHhyZWYKODM0MSAKJSVFT0YK",
                            }
                        ],
                    },
                    "xlsx (Openpyxl)": {
                        "summary": "Excel format (Openpyxl engine)",
                        "description": "A small Excel file in MIME+Base 64 format containing some items from the GAD-7.",
                        "value": [
                            {
                                "file_id": "1d66bce4b80c4b0eaefe33f00cddedef",
                                "file_name": "GAD-7.xlsx",
                                "file_type": "xlsx",
                                "content": "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,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",
                            }
                        ],
                    },
                    "xlsx (Xlsxwriter)": {
                        "summary": "Excel format (Xlsxwriter engine)",
                        "description": "A small Excel file in MIME+Base 64 format containing some items from the GAD-7.",
                        "value": [
                            {
                                "file_id": "1d66bce4b80c4b0eaefe33f00cddedef",
                                "file_name": "GAD-7.xlsx",
                                "file_type": "xlsx",
                                "content": "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,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",
                            }
                        ],
                    },
                    "txt": {
                        "summary": "Plain text document",
                        "description": "A small plain text file containing some items from the GAD-7.",
                        "value": [
                            {
                                "file_id": "97bdeeffe67d4f5fa271724c2200f268",
                                "file_name": "GAD-7.txt",
                                "file_type": "txt",
                                "content": "1. Feeling nervous, anxious, or on edge\tNot at all/Several days/More than half the days/Nearly every day\n2. Not being able to stop or control worrying\tNot at all/Several days/More than half the days/Nearly every day",
                            }
                        ],
                    },
                    "csv": {
                        "summary": "CSV file",
                        "description": "A small CSV file containing some items from the GAD-7.",
                        "value": [
                            {
                                "file_id": "97bdeeffe6aaa5fa271724c2200f268",
                                "file_name": "GAD-7.csv",
                                "file_type": "csv",
                                "content": "Question number\tQuestion text\tOptions\n1\tFeeling nervous, anxious, or on edge\tNot at all/Several days/More than half the days/Nearly every day\n2\tNot being able to stop or control worrying\tNot at all/Several days/More than half the days/Nearly every day\n3\tWorrying too much about different things\tNot at all/Several days/More than half the days/Nearly every day\n4\tTrouble relaxing\tNot at all/Several days/More than half the days/Nearly every day\n5\tBeing so restless that it is hard to sit still\tNot at all/Several days/More than half the days/Nearly every day\n6\tBecoming easily annoyed or irritable\tNot at all/Several days/More than half the days/Nearly every day\n7\tFeeling afraid, as if something awful might happen\tNot at all/Several days/More than half the days/Nearly every day",
                            }
                        ],
                    },
                }
            ),
        ]
) -> List[Instrument]:
    """
    Parse PDFs or Excels or text files into Instruments, and identifies the language.

    If the file is binary (Excel or PDF), you must supply each file with the content in MIME format and the bytes in
    base64 encoding, like the example RawFile in the schema.

    If the file is plain text, supply the file content as a standard string.
    """

    # Assign any missing IDs
    for file in files:
        if file.file_id is None:
            file.file_id = uuid.uuid4().hex

    # List of all the instruments
    instruments: List[Instrument] = []

    # A list of files whose instruments are not cached
    files_with_no_cached_instruments = []

    for file in files:
        instrument_key = instruments_cache.generate_key(file.content)
        if instruments_cache.has(instrument_key):
            # If instruments are cached
            instruments.extend(instruments_cache.get(instrument_key))
        else:
            # If instruments are not cached
            files_with_no_cached_instruments.append(file)

    # Get instruments that aren't cached yet and cache them
    for file_with_no_cached_instruments in files_with_no_cached_instruments:
        new_instruments = convert_files_to_instruments(
            [file_with_no_cached_instruments]
        )
        instrument_key = instruments_cache.generate_key(
            file_with_no_cached_instruments.content
        )
        instruments_cache.set(instrument_key, new_instruments)
        instruments.extend(new_instruments)

    return instruments


@router.post(
    path="/match", response_model=MatchResponse, status_code=status.HTTP_200_OK, response_model_exclude_none=True
)
def match(
        match_body: MatchBody,
        _model_is_available=Depends(dependencies.model_from_match_body_is_available),
        include_catalogue_matches: bool = Query(default=False),
        catalogue_sources: List[str] = Query(default=[]),
        is_negate: bool = True,
        clustering_algorithm: ClusteringAlgorithm = ClusteringAlgorithm.affinity_propagation
) -> MatchResponse:
    """
    Match instruments.
    """

    # Model
    model = match_body.parameters
    model_dict = model.model_dump(mode="json")

    # Get query
    query = match_body.query
    if type(query) is str:
        query = query.strip()
    if query == "":
        query = None

    # Get instruments
    instruments = match_body.instruments
    instruments = helpers.assign_missing_ids_to_instruments(instruments)

    # Get cached vectors of texts
    texts_cached_vectors = helpers.get_cached_text_vectors(
        instruments=instruments, query=query, model=model_dict
    )

    # Get MHC embeddings
    mhc_questions, mhc_all_metadata, mhc_embeddings = helpers.get_mhc_embeddings(
        model.model
    )

    # Get vect function
    vectorisation_function = helpers.get_vectorisation_function_for_model(
        model=model_dict
    )
    if not vectorisation_function:
        raise http_exceptions.CouldNotFindResourceHTTPException(
            "Could not find a vectorisation function for model."
        )

    # Currently only the model "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" is supported for
    # catalogue matches.
    if model_dict["model"] != constants.HUGGINGFACE_MINILM_L12_V2["model"]:
        include_catalogue_matches = False

    # Catalogue data
    catalogue_embeddings = catalogue_data_embeddings_for_model[model_dict["model"]]
    if catalogue_embeddings.size == 0:
        # If the embeddings are not available, do not include catalogue matches
        include_catalogue_matches = False
    catalogue_data = {}
    if include_catalogue_matches:
        catalogue_data = {"all_embeddings_concatenated": catalogue_embeddings}
        catalogue_data.update(catalogue_data_default)

        # Filter catalogue data
        if catalogue_sources:
            catalogue_data = helpers.filter_catalogue_data(
                catalogue_data=copy.deepcopy(catalogue_data), sources=catalogue_sources
            )

    # Match
    match_response_from_library = match_instruments_with_function(
        instruments=instruments,
        query=query,
        topics=match_body.topics,
        mhc_questions=mhc_questions,
        mhc_all_metadatas=mhc_all_metadata,
        mhc_embeddings=mhc_embeddings,
        texts_cached_vectors=texts_cached_vectors,
        vectorisation_function=vectorisation_function,
        is_negate=is_negate,
        clustering_algorithm=clustering_algorithm
    )

    # Get catalogue matches
    closest_catalogue_instrument_matches = []
    if include_catalogue_matches:
        instruments, closest_catalogue_instrument_matches = match_instruments_with_catalogue_instruments(
            instruments=instruments,
            catalogue_data=catalogue_data,
            vectorisation_function=vectorisation_function,
            texts_cached_vectors=texts_cached_vectors,
        )

    # Add new vectors to cache
    vectors_cache.add(
        new_text_vectors=match_response_from_library.new_vectors_dict,
        model_name=model.model,
        framework=model.framework
    )

    # List of matches
    matches_jsonable = match_response_from_library.similarity_with_polarity.tolist()

    # Query similarity
    if match_response_from_library.query_similarity is not None:
        query_similarity = match_response_from_library.query_similarity.tolist()
    else:
        query_similarity = None

    # Response options similarity
    response_options_similarity = match_response_from_library.response_options_similarity.tolist()

    return MatchResponse(
        instruments=instruments,
        questions=match_response_from_library.questions,
        matches=matches_jsonable,
        query_similarity=query_similarity,
        closest_catalogue_instrument_matches=closest_catalogue_instrument_matches,
        instrument_to_instrument_similarities=match_response_from_library.instrument_to_instrument_similarities,
        clusters=match_response_from_library.clusters,
        response_options_similarity=response_options_similarity
    )


@router.post(
    path="/examples", response_model=List[Instrument], status_code=status.HTTP_200_OK, response_model_exclude_none=True
)
def get_example_instruments() -> List[Instrument]:
    """
    Get example instruments.
    """

    return helpers.get_example_instruments()


@router.get(path="/cache", response_model=CacheResponse, status_code=status.HTTP_200_OK,
            response_model_exclude_none=True)
def get_cache() -> CacheResponse:
    """
    Get all items from cache.
    """

    instruments_list = []
    for instrument_cache_values in instruments_cache.get_cache().values():
        for instrument_cache_value in instrument_cache_values:
            instruments_list.append(instrument_cache_value)

    vectors_list = []
    for vector_cache_value in vectors_cache.get_cache().values():
        vectors_list.append(vector_cache_value)

    return CacheResponse(
        instruments=instruments_list,
        vectors=vectors_list,
    )


@router.post(
    path="/search_instruments",
    response_model=SearchInstrumentsResponse,
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
def search_instruments(
        search_instruments_body: SearchInstrumentsBody = SearchInstrumentsBody(),
        query: str | None = Query(default=None),
        instrument_length_min: int = Query(default=5, gt=0),
        instrument_length_max: int = Query(default=10, gt=0),
        sources: List[str] = Query(default=[]),
        topics: List[str] = Query(default=[]),
) -> SearchInstrumentsResponse:
    """
    Search instruments.
    """

    # Model
    model = search_instruments_body.parameters
    model_dict = model.model_dump(mode="json")

    # Get vect function
    vectorisation_function = helpers.get_vectorisation_function_for_model(
        model=model_dict
    )
    if not vectorisation_function:
        raise http_exceptions.CouldNotFindResourceHTTPException(
            "Could not find a vectorisation function for model."
        )

    # Currently only the model "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" is supported for
    # searching instruments.
    if model_dict["model"] != constants.HUGGINGFACE_MINILM_L12_V2["model"]:
        return SearchInstrumentsResponse(instruments=[])

    # Catalogue data
    catalogue_embeddings = catalogue_data_embeddings_for_model[model_dict["model"]]
    if catalogue_embeddings.size == 0:
        return SearchInstrumentsResponse(instruments=[])
    catalogue_data = {"all_embeddings_concatenated": catalogue_embeddings}
    catalogue_data.update(catalogue_data_default)

    # Filter catalogue data
    if sources or topics or instrument_length_min or instrument_length_max:
        catalogue_data = helpers.filter_catalogue_data(
            catalogue_data=copy.deepcopy(catalogue_data),
            sources=sources,
            topics=topics,
            instrument_length_min=instrument_length_min,
            instrument_length_max=instrument_length_max,
        )

    # Return up to 100 instruments
    max_results = 100

    # Query is provided: Match the query with the catalogue instruments
    if query:
        texts_cached_vectors = helpers.get_cached_text_vectors(
            instruments=[], query=query, model=model_dict
        )

        match_result = match_query_with_catalogue_instruments(
            query=query,
            catalogue_data=catalogue_data,
            vectorisation_function=vectorisation_function,
            texts_cached_vectors=texts_cached_vectors,
            max_results=max_results,
        )

        # Add new vectors to cache
        vectors_cache.add(
            new_text_vectors=match_result["new_text_vectors"],
            model_name=model.model,
            framework=model.framework,
        )

        return SearchInstrumentsResponse(instruments=match_result["instruments"])

    # No query provided: Get the first n catalogue instruments
    else:
        catalogue_instruments = catalogue_data["all_instruments"][:max_results]
        instruments = [
            Instrument.model_validate(catalogue_instrument)
            for catalogue_instrument in catalogue_instruments
        ]

        return SearchInstrumentsResponse(instruments=instruments)
