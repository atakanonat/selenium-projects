# Imports
from selenium import webdriver
import time
import loginInfo

# Run chromedriver
browser = webdriver.Chrome()

# Go to instagram main page
browser.get('https://www.instagram.com/')

time.sleep(1)

# Log in via Facebook informations
fb_button = browser.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[5]/button')
fb_button.click()

time.sleep(2)

email = browser.find_element_by_xpath('//*[@id="email"]')
password = browser.find_element_by_xpath('//*[@id="pass"]')

# Take username and password from loginInfo.py file
password.send_keys(loginInfo.password)

login_button = browser.find_element_by_xpath('//*[@id="loginbutton"]')
login_button.click()

time.sleep(15)

# Close notification pop-up
turnoff_notifications = browser.find_element_by_xpath(
    '/html/body/div[5]/div/div/div/div[3]/button[2]')
turnoff_notifications.click()

# Enter profile page
profile_dropdown_button = browser.find_element_by_xpath(
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')
profile_dropdown_button.click()

profile_button = browser.find_element_by_xpath(
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]')
profile_button.click()

time.sleep(2)

# Followers list
followers_button = browser.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
followers_button.click()

time.sleep(4)

# Script for scrolling to take all followers
lenOfPage = browser.execute_script("""
    followers = document.querySelector(".isgrP");
    followers.scrollTo(0, followers.scrollHeight);
    var lenOfPage = followers.scrollHeight;
    return lenOfPage;
""")

# Scroll loop
while True:
    lastCount = lenOfPage
    time.sleep(2)

    lenOfPage = browser.execute_script("""
        followers = document.querySelector(".isgrP");
        followers.scrollTo(0, followers.scrollHeight);
        var lenOfPage = followers.scrollHeight;
        return lenOfPage;
    """)

    if lastCount == lenOfPage:
        break

# Take followers
followers = browser.find_elements_by_css_selector('a.FPmhX.notranslate._0imsa')

# Save as text file
with open('followers.txt', 'w', encoding='UTF-8') as file:
    for follower in followers:
        file.write(follower.text + '\n********************\n')

# Close browser
browser.close()
