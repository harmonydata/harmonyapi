'''
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

'''

import unittest

import requests

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
}

json_data_to_match_gad_7 = {
    'instruments': [
        {
            "file_id": "614b672c9dfb41c386fbbd4e44ff38b4",
            "instrument_id": "65c0c54c3f2d4288b232f2df3c1db889",
            "instrument_name": "SCARED English (adult)",
            "file_name": "SCARED English (adult).pdf",
            "file_type": "pdf",
            "file_section": None,
            "study": None,
            "sweep": None,
            "metadata": None,
            "language": "en",
            "questions": [
                {
                    "question_no": "1",
                    "question_intro": None,
                    "question_text": "When I feel frightened, it is hard for me to breathe",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "2",
                    "question_intro": None,
                    "question_text": "I get headaches when I am at school",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "3",
                    "question_intro": None,
                    "question_text": "I don’t like to be with people I don’t know well",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "4",
                    "question_intro": None,
                    "question_text": "I get scared if I sleep away from home",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "5",
                    "question_intro": None,
                    "question_text": "I worry about other people liking me",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "6",
                    "question_intro": None,
                    "question_text": "When I get frightened, I feel like passing out",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "7",
                    "question_intro": None,
                    "question_text": "I am nervous",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "8",
                    "question_intro": None,
                    "question_text": "I follow my mother or father wherever they go",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "9",
                    "question_intro": None,
                    "question_text": "People tell me that I look nervous",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "10",
                    "question_intro": None,
                    "question_text": "I feel nervous with people I don’t know well",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "11",
                    "question_intro": None,
                    "question_text": "My I get stomachaches at school",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "12",
                    "question_intro": None,
                    "question_text": "When I get frightened, I feel like I am going crazy",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "13",
                    "question_intro": None,
                    "question_text": "I worry about sleeping alone",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "14",
                    "question_intro": None,
                    "question_text": "I worry about being as good as other kids",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "15",
                    "question_intro": None,
                    "question_text": "When I get frightened, I feel like things are not real",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "16",
                    "question_intro": None,
                    "question_text": "I have nightmares about something bad happening to my parents",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "17",
                    "question_intro": None,
                    "question_text": "I worry about going to school",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "18",
                    "question_intro": None,
                    "question_text": "When I get frightened, my heart beats fast",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "19",
                    "question_intro": None,
                    "question_text": "I get shaky",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "20",
                    "question_intro": None,
                    "question_text": "I have nightmares about something bad happening to me",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "21",
                    "question_intro": None,
                    "question_text": "I worry about things working out for me",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "22",
                    "question_intro": None,
                    "question_text": "When I get frightened, I sweat a lot",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "23",
                    "question_intro": None,
                    "question_text": "I am a worrier",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "24",
                    "question_intro": None,
                    "question_text": "I get really frightened for no reason at all",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "25",
                    "question_intro": None,
                    "question_text": "I am afraid to be alone in the house",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "26",
                    "question_intro": None,
                    "question_text": "It is hard for me to talk with people I don’t know well",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "27",
                    "question_intro": None,
                    "question_text": "When I get frightened, I feel like I am choking",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "28",
                    "question_intro": None,
                    "question_text": "People tell me that I worry too much",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "29",
                    "question_intro": None,
                    "question_text": "I don’t like to be away from my family",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "30",
                    "question_intro": None,
                    "question_text": "I am afraid of having anxiety (or panic) attacks",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "31",
                    "question_intro": None,
                    "question_text": "I worry that something bad might happen to my parents",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "32",
                    "question_intro": None,
                    "question_text": "I feel shy with people I don’t know well",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "33",
                    "question_intro": None,
                    "question_text": "I worry about what is going to happen in the future",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "34",
                    "question_intro": None,
                    "question_text": "When I get frightened, I feel like throwing up",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "35",
                    "question_intro": None,
                    "question_text": "I worry about how well I do things",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "36",
                    "question_intro": None,
                    "question_text": "I am scared to go to school",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "37",
                    "question_intro": None,
                    "question_text": "I worry about things that have already happened",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "38",
                    "question_intro": None,
                    "question_text": "When I get frightened, I feel dizzy",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "39",
                    "question_intro": None,
                    "question_text": "I feel nervous when I am with other children or adults and I have to do something while they watch me (for example: read aloud, speak, play a game, play a sport)",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "40",
                    "question_intro": None,
                    "question_text": "I feel nervous when I am going to parties, dances, or any place where there will be people that I don’t know well",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "41",
                    "question_intro": None,
                    "question_text": "I am shy",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                }
            ],
            "closest_catalogue_instrument_matches": [],
            "grouping": ""
        },
        {
            "file_id": "2643b44e8bb94556b37cab134e5c0afe",
            "instrument_id": "a2ebc5ef638e46cd94ad1d99fbfdaeae",
            "instrument_name": "SCARED English (child)",
            "file_name": "SCARED English (child).pdf",
            "file_type": "pdf",
            "file_section": None,
            "study": None,
            "sweep": None,
            "metadata": None,
            "language": "en",
            "questions": [
                {
                    "question_no": "1",
                    "question_intro": None,
                    "question_text": "When my child feels frightened, it is hard for him/her to breathe",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "2",
                    "question_intro": None,
                    "question_text": "My child gets headaches when he/she is at school",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "3",
                    "question_intro": None,
                    "question_text": "My child doesn’t like to be with people he/she doesn’t know well",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "4",
                    "question_intro": None,
                    "question_text": "My child gets scared if he/she sleeps away from home",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "5",
                    "question_intro": None,
                    "question_text": "My child worries about other people liking him/her",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "6",
                    "question_intro": None,
                    "question_text": "When my child gets frightened, he/she feels like passing out",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "7",
                    "question_intro": None,
                    "question_text": "My child is nervous",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "8",
                    "question_intro": None,
                    "question_text": "My child follows me wherever I go",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "9",
                    "question_intro": None,
                    "question_text": "People tell me that my child looks nervous",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "10",
                    "question_intro": None,
                    "question_text": "My child feels nervous with people he/she doesn’t know well",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "11",
                    "question_intro": None,
                    "question_text": "My child gets stomachaches at school",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "12",
                    "question_intro": None,
                    "question_text": "When my child gets frightened, he/she feels like he/she is going crazy",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "13",
                    "question_intro": None,
                    "question_text": "My child worries about sleeping alone",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "14",
                    "question_intro": None,
                    "question_text": "My child worries about being as good as other kids",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "15",
                    "question_intro": None,
                    "question_text": "When he/she gets frightened, he/she feels like things are not real",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "16",
                    "question_intro": None,
                    "question_text": "My child has nightmares about something bad happening to his/her parents",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "17",
                    "question_intro": None,
                    "question_text": "My child worries about going to school",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "18",
                    "question_intro": None,
                    "question_text": "When my child gets frightened, his/her heart beats fast",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "19",
                    "question_intro": None,
                    "question_text": "He/she gets shaky",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "20",
                    "question_intro": None,
                    "question_text": "My child has nightmares about something bad happening to him/her",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "21",
                    "question_intro": None,
                    "question_text": "My child worries about things working out for him/her",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "22",
                    "question_intro": None,
                    "question_text": "When my child gets frightened, he/she sweats a lot",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "23",
                    "question_intro": None,
                    "question_text": "My child is a worrier",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "24",
                    "question_intro": None,
                    "question_text": "My child gets really frightened for no reason at all",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "25",
                    "question_intro": None,
                    "question_text": "My child is afraid to be alone in the house",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "26",
                    "question_intro": None,
                    "question_text": "It is hard for my child to talk with people he/she doesn’t know well",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "27",
                    "question_intro": None,
                    "question_text": "When my child gets frightened, he/she feels like he/she is choking",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "28",
                    "question_intro": None,
                    "question_text": "People tell me that my child worries too much",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "29",
                    "question_intro": None,
                    "question_text": "My child doesn’t like to be away from his/her family",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "30",
                    "question_intro": None,
                    "question_text": "My child is afraid of having anxiety (or panic) attacks",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "31",
                    "question_intro": None,
                    "question_text": "My child worries that something bad might happen to his/her parents",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "32",
                    "question_intro": None,
                    "question_text": "My child feels shy with people he/she doesn’t know well",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "33",
                    "question_intro": None,
                    "question_text": "My child worries about what is going to happen in the future",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "34",
                    "question_intro": None,
                    "question_text": "When my child gets frightened, he/she feels like throwing up",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "35",
                    "question_intro": None,
                    "question_text": "My child worries about how well he/she does things",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "36",
                    "question_intro": None,
                    "question_text": "My child is scared to go to school",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "37",
                    "question_intro": None,
                    "question_text": "My child worries about things that have already happened",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "38",
                    "question_intro": None,
                    "question_text": "When my child gets frightened, he/she feels dizzy",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "39",
                    "question_intro": None,
                    "question_text": "My child feels nervous when he/she is with other children or adults and he/she has to do something while they watch him/her (for example: read aloud, speak, play a game, play a sport)",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "40",
                    "question_intro": None,
                    "question_text": "My child feels nervous when he/she is going to parties, dances, or any place where there will be people that he/she doesn’t know well",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                },
                {
                    "question_no": "41",
                    "question_intro": None,
                    "question_text": "My child is shy",
                    "options": [
                        "Not True or Hardly Ever True",
                        "Somewhat True or Sometimes True",
                        "Very True or Often True"
                    ],
                    "source_page": 0,
                    "instrument_id": None,
                    "instrument_name": None,
                    "topics_auto": None,
                    "topics_strengths": None,
                    "nearest_match_from_mhc_auto": None,
                    "closest_catalogue_question_match": None
                }
            ],
            "closest_catalogue_instrument_matches": [],
            "grouping": ""
        }
    ],
    'parameters': {
        "framework": "huggingface",
        "model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    }
}

endpoint = 'https://harmonystagingtmp.azurewebsites.net/text/match'

response = requests.post(endpoint, headers=headers, json=json_data_to_match_gad_7)

class TestMatchBiggerPayload(unittest.TestCase):

    def test_big_match_command(self):
        self.assertEqual(5, len(response.json()))


if __name__ == '__main__':
    unittest.main()
