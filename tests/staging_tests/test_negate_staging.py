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

json_data_to_match_negation = {
    'instruments': [
        {
            'questions': [
                {
                    'question_no': '1',
                    'question_text': 'I feel nervous',
                },
                {
                    'question_no': '2',
                    'question_text': 'I don\'t feel nervous',
                },
            ],
        }
    ]
}

endpoint = 'https://harmonystagingtmp.azurewebsites.net/text/match'

response = requests.post(endpoint, headers=headers, json=json_data_to_match_negation)

response_no_negation = requests.post(endpoint + "?is_negate=false", headers=headers, json=json_data_to_match_negation)


class TestMatch(unittest.TestCase):

    def test_negation_instrument_correct_size_dictionary_response(self):
        self.assertEqual(8, len(response.json()))

    def test_negation_instrument_first_question_conserved(self):
        self.assertEqual("I feel nervous", response.json()["questions"][0]["question_text"])

    def test_negation_instrument_correct_number_of_questions(self):
        self.assertEqual(2, len(response.json()["questions"]))

    def test_negation_instrument_correct_number_of_matches(self):
        self.assertEqual(2, len(response.json()["matches"]))
        self.assertEqual(2, len(response.json()["matches"][0]))

    def test_negation_instrument_high_like_for_like_match(self):
        self.assertLess(0.99, response.json()["matches"][0][0])

    def test_negation_instrument_negative_match(self):
        self.assertGreater(0, response.json()["matches"][0][1])

    def test_negation_instrument_positive_match(self):
        self.assertLess(0, response_no_negation.json()["matches"][0][1])


if __name__ == '__main__':
    unittest.main()
