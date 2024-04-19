import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome('/home/isha/Downloads/chromedriver.exe')

# Open Google Images
query = "tuta absoluta"
url = f"https://www.google.com/search?q={query}&tbm=isch"
driver.get(url)

# Scroll to load more images
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
image_elements = soup.find_all("img", class_="rg_i")

# Create a directory to save images
save_dir = "img"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Download images
for idx, image_elem in enumerate(image_elements):
    image_url = image_elem.get("src")
    if image_url:
        image_path = os.path.join(save_dir, f"{query}_{idx}.jpg")
        with open(image_path, "wb") as f:
            f.write(requests.get(image_url).content)

# Close the WebDriver
driver.quit()

print("Images downloaded successfully!")
