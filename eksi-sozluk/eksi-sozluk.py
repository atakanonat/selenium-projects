# Imports
from selenium import webdriver
import random
import time

# Run chromedriver
browser = webdriver.Chrome()

# Select a topic url with blank page number
url = 'https://eksisozluk.com/geceye-bir-sarki-birak--5086776?p='

entries = []

# Get max page number
browser.get(url+str(1))
max_page = browser.find_element_by_css_selector('a.last').text

for _ in range(5):
    # Randomise page number
    randomPage = random.randint(1, int(max_page))

    # Create newUrl with randomized page number
    newUrl = url + str(randomPage)

    # Redirect to newUrl
    browser.get(newUrl)

    # Find entries with css selector
    elements = browser.find_elements_by_css_selector('.content')
    for element in elements:
        entries.append(element.text)

    time.sleep(3)

# Save entries as a txt file
with open('entries.txt', 'w', encoding='UTF-8') as file:
    for i, entry in enumerate(entries):
        file.write(f'{i+1}.entry\n{entry}\n*********************\n')

# Close browser
browser.close()
