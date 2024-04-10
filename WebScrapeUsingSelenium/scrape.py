import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Define the URL of the webpage containing the top 100 romantic movies
url = "https://www.rottentomatoes.com/search?search=romantic%20movies"

# Set up Selenium WebDriver (assuming you have Chrome WebDriver installed)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # To run Chrome in headless mode
driver = webdriver.Chrome(options=chrome_options)

# Open the webpage
driver.get(url)

# Scroll down the webpage to load all movies (if needed)
scrolls = 20  # Increase the number of scrolls
for _ in range(scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust the sleep time as needed

# Find all movie containers on the webpage
try:
    movie_containers = driver.find_elements_by_xpath("//ul[@slot='list']")
except NoSuchElementException as e:
    print("Error finding movie containers:", e)
    movie_containers = []

# Create a directory to save the scraped data if it doesn't exist
if not os.path.exists('scraped_data'):
    os.makedirs('scraped_data')

# Open a file to store the scraped data
with open('scraped_data/top_100_romantic_movies.csv', 'w', encoding='utf-8') as f:
    # Write header
    f.write("Title,Release Date\n")

    # Extract data for each movie
    for movie_container in movie_containers:
        try:
            # Extract movie title
            title_element = movie_container.find_element_by_xpath(".//a[@class='unset']")
            title = title_element.text.strip()

            # Extract release date
            release_date_element = movie_container.find_element_by_xpath(".//span[@class='year']")
            release_date = release_date_element.text.strip()

            # Write data to file
            f.write(f"{title},{release_date}\n")
        except NoSuchElementException as e:
            print("Error extracting data for a movie:", e)

# Close the WebDriver
driver.quit()

print("Scraping complete. Data saved in 'top_100_romantic_movies.csv'.")
