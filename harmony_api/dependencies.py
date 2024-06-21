from harmony.schemas.requests.text import MatchBody, MatchCatalogueBody
from harmony_api import http_exceptions, helpers, constants


def model_from_match_body_is_available(match_body: MatchBody) -> bool:
    """
    Check model availability.
    """

    model = match_body.parameters
    __check_model(model.dict())

    return True


def model_from_match_catalogue_body_is_available(
    match_catalogue_body: MatchCatalogueBody,
) -> bool:
    """
    Check model availability.
    """

    model = match_catalogue_body.parameters
    __check_model(model.dict())

    return True


def model_from_match_catalogue_body_is_minilm_l12_v2(
    match_catalogue_body: MatchCatalogueBody,
) -> bool:
    """
    Check if model is HUGGINGFACE MINILM_L12_V2.
    """

    model = match_catalogue_body.parameters
    model_dict = model.dict()

    if model_dict["model"] != constants.HUGGINGFACE_MINILM_L12_V2["model"]:
        raise http_exceptions.CouldNotProcessRequestHTTPException(
            "Could not process request because the provided model is not supported."
        )

    return True


def __check_model(model_dict: dict):
    if model_dict not in constants.ALL_HARMONY_API_MODELS:
        raise http_exceptions.CouldNotProcessRequestHTTPException(
            "Could not process request because the model does not exist."
        )
    if not helpers.check_model_availability(model_dict):
        raise http_exceptions.CouldNotProcessRequestHTTPException(
            "Could not process request because the model is not available."
        )
