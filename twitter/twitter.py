# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import loginInfo
import time

# Run chromedriver
browser = webdriver.Chrome()

# Go to twitter.com
browser.get('https://twitter.com/')

time.sleep(3)

# Select log in with email choice
sign_in = browser.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span')
sign_in.click()

withUsername = browser.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a')
withUsername.click()

time.sleep(6)

# Enter username and password informations that imported from loginInfo.py file
username = browser.find_element_by_xpath(
    '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
username.send_keys(loginInfo.username)

next_button = browser.find_element_by_xpath(
    '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
next_button.click()

time.sleep(2)

password = browser.find_element_by_xpath(
    '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
password.send_keys(loginInfo.password)

time.sleep(2)

login_button = browser.find_element_by_xpath(
    '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
login_button.click()

time.sleep(5)

# Search for desired hashtag topic
search_field = browser.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
search_field.send_keys('#news' + Keys.ENTER)

time.sleep(5)

# Script for scrolling to take all tweets about topic
lenOfPage = browser.execute_script("""
    window.scrollTo(0, document.body.scrollHeight);
    var lenOfPage = document.body.scrollHeight;
    return lenOfPage;
""")

tweets = []

# Scroll and tweet append to tweets list loop
while True:
    lastCount = lenOfPage

    time.sleep(3)

    elements = browser.find_elements_by_css_selector(
        '.css-901oao.r-18jsvk2.r-1qd0xha.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0 > span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0')

    for element in elements:
        if element.text.strip() != '':
            tweets.append(element.text)

    lenOfPage = browser.execute_script("""
        window.scrollTo(0, document.body.scrollHeight);
        var lenOfPage = document.body.scrollHeight;
        return lenOfPage;
    """)

    if lastCount == lenOfPage:
        break

time.sleep(3)

# Save tweets into a text file
with open('tweets.txt', 'w', encoding='UTF-8') as file:
    for idx, tweet in enumerate(tweets):
        file.write(str(idx) + '.\t---->\t' +
                   tweet + '\n********************\n')

# Close browser
browser.close()