from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import requests
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://news.ycombinator.com/')
driver.find_element_by_class_name('storylink').click()

