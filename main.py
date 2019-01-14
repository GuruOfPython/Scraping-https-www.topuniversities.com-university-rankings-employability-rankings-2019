#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Chrome Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import os
from lxml import html

CHROME_OPTIONS = Options()
# CHROME_OPTIONS.add_argument("--headless")
# CHROME_OPTIONS.add_argument('--disable-gpu')  # Last I checked this was necessary.
# CHROME_OPTIONS.add_argument('--disable-notifications')
# prefs = {"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096}
# CHROME_OPTIONS.add_experimental_option('prefs', prefs)
# CHROME_OPTIONS.add_argument('--ignore-certificate-errors')
# CHROME_OPTIONS.add_argument("--test-type")
# CHROME_OPTIONS.add_argument('--disable-infobars')
# CHROME_OPTIONS.add_argument('--disable-extensions')
# CHROME_OPTIONS.add_argument('--profile-directory=Default')
# CHROME_OPTIONS.add_argument('--incognito')
# CHROME_OPTIONS.add_argument('--disable-plugins-discovery')
CHROME_OPTIONS.add_argument('--start-maximized')

driver = webdriver.Chrome(options=CHROME_OPTIONS, executable_path=os.getcwd() + r"\WebDriver\chromedriver.exe")
driver.get(url="https://www.topuniversities.com/university-rankings/employability-rankings/2019")

WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//span[@class="jcf-select-text"]/span[text()="25"]'))
)

option = driver.find_element_by_xpath('//span[@class="jcf-select-text"]/span[text()="25"]')
option.click()

all_select = driver.find_element_by_xpath('//span[text()="All"]')
all_select.click()

tree = html.fromstring(driver.page_source)

rows = tree.xpath('//table[@id="qs-rankings"]/tbody/tr')
for i, row in enumerate(rows):
    try:
        rank = row.xpath('.//span[@class="rank "]/text()')
    except:
        rank = ""
    try:
        name = ""
    except:
        name = ""
    try:
        location = ""
    except:
        location = ""
    try:
        link = ""
    except:
        link = ""