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

import json
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


class TestDifferentFrameworks(unittest.TestCase):

    def test_huggingface(self):
        response = requests.post(endpoint, headers=headers, json=json_data_to_match_gad_7)

        print(response.json()["matches"][0][0])

        self.assertLess(0.99, response.json()["matches"][0][0])

    def test_google_nonexistent(self):
        payload_google = json.loads(json.dumps(json_data_to_match_gad_7))
        payload_google["parameters"]["framework"] = "google"

        response = requests.post(endpoint, headers=headers, json=payload_google)

        self.assertIn("model does not exist", response.text)

    def test_google_real(self):
        payload_google = json.loads(json.dumps(json_data_to_match_gad_7))
        payload_google["parameters"]["framework"] = "google"
        payload_google["parameters"]["model"] = "textembedding-gecko@003"

        response = requests.post(endpoint, headers=headers, json=payload_google)

        self.assertLess(0.99, response.json()["matches"][0][0])

    def test_google_different_from_huggingface(self):
        response_huggingface = requests.post(endpoint, headers=headers, json=json_data_to_match_gad_7)

        payload_google = json.loads(json.dumps(json_data_to_match_gad_7))
        payload_google["parameters"]["framework"] = "google"
        payload_google["parameters"]["model"] = "textembedding-gecko@003"

        response_google = requests.post(endpoint, headers=headers, json=payload_google)

        abs_diff = abs(response_huggingface.json()["matches"][0][1] - response_google.json()["matches"][0][1])

        print("Absolute difference", abs_diff)

        self.assertLess(0.1, abs_diff)

    def test_google_monolingual(self):
        payload_google = json.loads(json.dumps(json_data_to_match_gad_7))
        payload_google["parameters"]["framework"] = "google"
        payload_google["parameters"]["model"] = "textembedding-gecko@003"

        response = requests.post(endpoint, headers=headers, json=payload_google)

        self.assertGreater(0.92, response.json()["matches"][0][2])

    def test_google_multilingual(self):
        payload_google = json.loads(json.dumps(json_data_to_match_gad_7))
        payload_google["parameters"]["framework"] = "google"
        payload_google["parameters"]["model"] = "textembedding-gecko-multilingual"

        response = requests.post(endpoint, headers=headers, json=payload_google)

        self.assertLess(0.92, response.json()["matches"][0][2])

    def test_openai(self):
        payload_openai = json.loads(json.dumps(json_data_to_match_gad_7))
        payload_openai["parameters"]["framework"] = "openai"
        payload_openai["parameters"]["model"] = "text-embedding-3-large"

        response = requests.post(endpoint, headers=headers, json=payload_openai)

        self.assertLess(0.99, response.json()["matches"][0][0])

    def test_azure_openai(self):
        payload_openai = json.loads(json.dumps(json_data_to_match_gad_7))
        payload_openai["parameters"]["framework"] = "azure_openai"
        payload_openai["parameters"]["model"] = "fds-text-embedding-3-large"

        response = requests.post(endpoint, headers=headers, json=payload_openai)

        self.assertLess(0.99, response.json()["matches"][0][0])

    def test_azure_openai_same_as_vanilla_openai(self):
        payload_vanilla_openai = json.loads(json.dumps(json_data_to_match_gad_7))
        payload_vanilla_openai["parameters"]["framework"] = "openai"
        payload_vanilla_openai["parameters"]["model"] = "text-embedding-3-large"

        vanilla_openai_response = requests.post(endpoint, headers=headers, json=payload_vanilla_openai)

        payload_azure_openai = json.loads(json.dumps(json_data_to_match_gad_7))
        payload_azure_openai["parameters"]["framework"] = "azure_openai"
        payload_azure_openai["parameters"]["model"] = "fds-text-embedding-3-large"

        azure_openai_response = requests.post(endpoint, headers=headers, json=payload_azure_openai)

        self.assertGreater(0.01,
                           abs(vanilla_openai_response.json()["matches"][0][0] -
                               azure_openai_response.json()["matches"][0][0]))
        self.assertGreater(0.01,
                           abs(vanilla_openai_response.json()["matches"][0][1] -
                               azure_openai_response.json()["matches"][0][1]))
        self.assertGreater(0.01,
                           abs(vanilla_openai_response.json()["matches"][0][2] -
                               azure_openai_response.json()["matches"][0][2]))


if __name__ == '__main__':
    unittest.main()
