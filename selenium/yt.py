import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(www.youtube.com)

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# Search for the video.
time.sleep(1)
wait.until(visible((By.NAME, "search_query")))
driver.find_element_by_name("search_query").click()
driver.find_element_by_name("search_query").send_keys(video)
driver.find_element_by_id("search-icon-legacy").click()

# Play the video.
wait.until(visible((By.ID, "video-title")))
driver.find_element_by_id("video-title").click()