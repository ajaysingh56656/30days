from urllib.parse import urlparse
import os
import time
import requests
from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver

url = 'https://www.instagram.com'

browser = webdriver.Chrome()
browser.get(url)

time.sleep(2)
username = browser.find_element_by_name('username')
username.send_keys(INSTA_USERNAME)
passward = browser.find_element_by_name('password')
passward.send_keys(INSTA_PASSWORD)

time.sleep(2)
button = browser.find_element_by_css_selector('button[type="submit"]')
button.click()

# body_el = browser.find_element_by_css_selector('body')
# html_text = body_el.get_attribute('innerHTML')
# print(html_text)

time.sleep(2)
""" <button class="sqdOP yWX7d y3zKF" type="button">Not Now</button> """
my_close_button_xpath = "//button[contains(text(), 'Not Now')]"
time.sleep(2)
my_close_button = browser.find_element_by_xpath(my_close_button_xpath)
time.sleep(2)
my_close_button.click()
time.sleep(2)

"""<button class="aOOlW>Not Now</button>"""
my_close_notification_xpath = "//button[contains(text(), 'Not Now')]"
time.sleep(2)
my_close_notification_button = browser.find_element_by_xpath(my_close_notification_xpath)
time.sleep(2)
my_close_notification_button.click()
time.sleep(2)


def click_to_follow(browser):
    """<button class="_5f5mN jIbKX _6VtSN  yZn4P">Follow</button>"""
    my_follow_button_xpath = "//button[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    # my_follow_button_xpath = "//a[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    # my_follow_button_xpath = "//*[contains(text(), 'Follow')][not(contains(text(), 'Following'))]"
    my_follow_button_elements = browser.find_elements_by_xpath(my_follow_button_xpath)
    time.sleep(2)
    for button in my_follow_button_elements:
        time.sleep(2)
        try:
            button.click()
        except:
            pass


url_next = 'https://www.instagram.com/therock/'
browser.get(url_next)
time.sleep(2)
click_to_follow(browser)


# time.sleep(2)
# the_rock_url = "https://www.instagram.com/therock/"
# browser.get(the_rock_url)
#
# post_url_pattern = "https://www.instagram.com/p/<post-slug-id>"
# post_xpath_str = "//a[contains(@href, '/p/')]"
# post_links = browser.find_elements_by_xpath(post_xpath_str)
# post_link_el = None
#
# if len(post_links) > 0:
#     post_link_el = post_links[0]
#
# if post_link_el:
#     post_href = post_link_el.get_attribute("href")
#     browser.get(post_href)
#
# video_els = browser.find_elements_by_xpath("//video")
# images_els = browser.find_elements_by_xpath("//img")
#
# base_dir = os.path.dirname(os.path.abspath(__file__))
# data_dir = os.path.join(base_dir, "data")
# os.makedirs(data_dir, exist_ok=True)


# PIL to verify the size of any given image.

# def scrape_and_save(elements):
#     for el in elements:
#         url = el.get_attribute('src')
#         base_url = urlparse(url).path
#         filename = os.path.basename(base_url)
#         filepath = os.path.join(data_dir, filename)
#         if os.path.exists(filepath):
#             continue
#         with requests.get(url, stream=True) as r:
#             try:
#                 r.raise_for_status()
#             except:
#                 continue
#             with open(filepath, 'wb') as f:
#                 for chunk in r.iter_content(chunk_size=8192):
#                     if chunk:
#                         f.write(chunk)


# scrape_and_save(images_els)

"""
LONG TERM Goal:
Use machine learning to classify the post's
image or video
and then comment in a relevant fashion
"""

"""
<textarea aria-label="Add a comment…" placeholder="Add a comment…" class="Ypffh" autocomplete="off" autocorrect="off" style="height: 18px;"></textarea>
<button class="sqdOP yWX7d y3zKF " type="submit">Post</button>
"""


# def automate_comment(browser, cont="Rock"):
#     time.sleep(3)
#     comment_xpath_str = "//textarea[contains(@placeholder, 'Add a comment…')]"
#     comment_el = browser.find_element_by_xpath(comment_xpath_str)
#     time.sleep(4)
#     comment_el.send_keys(cont)
#     submit_btns_xpath = "button[type='submit']"
#     submit_btns_els = browser.find_elements_by_css_selector(submit_btns_xpath)
#     time.sleep(2)
#     for btn in submit_btns_els:
#         try:
#             btn.click()
#         except:
#             pass
#
#
# automate_comment(browser)

# def automate_likes(browser):
#     like_heart_svg_xpath = "//*[contains(@aria-label, 'Like')]"
#     all_like_hearts_elements = browser.find_elements_by_xpath(like_heart_svg_xpath)
#     max_heart_h = -1
#     for heart_el in all_like_hearts_elements:
#         h = heart_el.get_attribute("height")
#         current_h = int(h)
#         if current_h > max_heart_h:
#             max_heart_h = current_h
#     all_like_hearts_elements = browser.find_elements_by_xpath(like_heart_svg_xpath)
#     for heart_el in all_like_hearts_elements:
#         h = heart_el.get_attribute("height")
#         if h == max_heart_h or h == f"{max_heart_h}":
#             parent_button = heart_el.find_element_by_xpath('..')
#             time.sleep(2)
#             try:
#                 parent_button.click()
#             except:
#                 pass
