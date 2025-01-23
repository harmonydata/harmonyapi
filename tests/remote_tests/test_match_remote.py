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
            'file_id': 'fd60a9a64b1b4078a68f4bc06f20253c',
            'instrument_id': '7829ba96f48e4848abd97884911b6795',
            'instrument_name': 'GAD-7 English',
            'file_name': 'GAD-7 EN.pdf',
            'file_type': 'pdf',
            'file_section': 'GAD-7 English',
            'language': 'en',
            'questions': [
                {
                    'question_no': '1',
                    'question_intro': 'Over the last two weeks, how often have you been bothered by the following problems?',
                    'question_text': 'Feeling nervous, anxious, or on edge',
                    'options': [
                        'Not at all',
                        'Several days',
                        'More than half the days',
                        'Nearly every day',
                    ],
                    'source_page': 0,
                },
                {
                    'question_no': '2',
                    'question_intro': 'Over the last two weeks, how often have you been bothered by the following problems?',
                    'question_text': 'Not being able to stop or control worrying',
                    'options': [
                        'Not at all',
                        'Several days',
                        'More than half the days',
                        'Nearly every day',
                    ],
                    'source_page': 0,
                },
            ],
        },
        {
            'file_id': 'fd60a9a64b1b4078a68f4bc06f20253c',
            'instrument_id': '7829ba96f48e4848abd97884911b6795',
            'instrument_name': 'GAD-7 Portuguese',
            'file_name': 'GAD-7 PT.pdf',
            'file_type': 'pdf',
            'file_section': 'GAD-7 Portuguese',
            'language': 'en',
            'questions': [
                {
                    'question_no': '1',
                    'question_intro': 'Durante as últimas 2 semanas, com que freqüência você foi incomodado/a pelos problemas abaixo?',
                    'question_text': 'Sentir-se nervoso/a, ansioso/a ou muito tenso/a',
                    'options': [
                        'Nenhuma vez',
                        'Vários dias',
                        'Mais da metade dos dias',
                        'Quase todos os dias',
                    ],
                    'source_page': 0,
                },
                {
                    'question_no': '2',
                    'question_intro': 'Durante as últimas 2 semanas, com que freqüência você foi incomodado/a pelos problemas abaixo?',
                    'question_text': ' Não ser capaz de impedir ou de controlar as preocupações',
                    'options': [
                        'Nenhuma vez',
                        'Vários dias',
                        'Mais da metade dos dias',
                        'Quase todos os dias',
                    ],
                    'source_page': 0,
                },
            ],
        },
    ],
    'query': 'anxiety',
    'parameters': {
        'framework': 'huggingface',
        'model': 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2',
    },
}

endpoint = 'https://api.harmonydata.ac.uk/text/match'

response = requests.post(endpoint, headers=headers, json=json_data_to_match_gad_7)


class TestMatch(unittest.TestCase):

    def test_gad_7_correct_size_dictionary_response(self):
        self.assertEqual(7, len(response.json()))

    def test_gad_7_first_question_conserved(self):
        self.assertEqual("Feeling nervous, anxious, or on edge", response.json()["questions"][0]["question_text"])

    def test_gad_7_correct_number_of_questions(self):
        self.assertEqual(4, len(response.json()["questions"]))

    def test_gad_7_correct_number_of_query_similarities(self):
        self.assertEqual(4, len(response.json()["query_similarity"]))

    def test_gad_7_correct_number_of_matches(self):
        self.assertEqual(4, len(response.json()["matches"]))
        self.assertEqual(4, len(response.json()["matches"][0]))

    def test_gad_7_high_like_for_like_match(self):
        self.assertLess(0.99, response.json()["matches"][0][0])

    def test_gad_7__en_vs_pt_high_like_for_like_match(self):
        self.assertLess(0.90, response.json()["matches"][0][2])


if __name__ == '__main__':
    unittest.main()
