from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(by="xpath", value='//*[@id="articlecount"]/a[1]')
# articles.click()

search = driver.find_element(by="name", value="search")
search.send_keys("Pokemon\n")


time.sleep(5)
driver.quit()