import time
from selenium import webdriver

browser = webdriver.Chrome()

url = 'http://www.google.com'
browser.get(url)

"""
<input class="gLFyf gsfi" name="q"
title="Search" value="">
"""

time.sleep(2)
name = 'q'
search_el = browser.find_element_by_name('q')
# print(search_el)

search_el.send_keys('Selenium Check it')

"""
<input class="gNO89b" value="Google Search" name="btnK" type="submit">
"""


submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()

