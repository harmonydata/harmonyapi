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

import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.add_argument('--headless') # If you want to run without a graphical view
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://harmonydata.ac.uk/app")

time.sleep(1)

dropdown_span = driver.find_element(By.XPATH, '//div[@id="multiple-checkbox"]')

dropdown_span.click()

time.sleep(1)

dropdown_options = driver.find_elements(By.XPATH, '//span[contains(@class, "MuiListItemText-primary")]')

dropdown_options[1].click()

dropdown_options[2].click()

time.sleep(1)

action = webdriver.common.action_chains.ActionChains(driver)

action.move_to_element_with_offset(dropdown_options[0], 5, -50)

action.click()

action.perform()

time.sleep(1)

harmonise_button = driver.find_element(By.XPATH, '//p[contains(@class, "MuiTypography-root")]')

harmonise_button.click()

time.sleep(1)


class TestOneMatch(unittest.TestCase):

    def test_gad_7_correct_size_dictionary_response(self):
        self.assertIn("Found 41 matches", driver.page_source)
