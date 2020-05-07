from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import csv
from bs4 import BeautifulSoup as bs

# set up the webdriver
url = 'https://immi.homeaffairs.gov.au/visas/working-in-australia/skill-occupation-list#'
browser = webdriver.Chrome()
browser.get(url)
load_time = 15
try:
    page_title = WebDriverWait(browser, load_time).until(ec.presence_of_element_located((By.ID, 's4-workspace')))
    print('page is ready')
except TimeoutException:
    print('loading took too much time')

page_source = browser.page_source  # get page source
print(page_source)

# define field name
field_title = ['Occupation', 'ANZSCO Code', 'List']
with open(AU_Occp_list1, 'w', newline='utf-8') as file:
    # start to scrape

