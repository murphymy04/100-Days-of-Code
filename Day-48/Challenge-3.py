from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")
keys = webdriver.Keys()
box = driver.find_element(by="name", value="fName")
values = ["Myles", "Murphy", "smiles20004@gmail.com"]

box.send_keys(values[0])
driver.find_element(by="name", value="lName").send_keys(values[1])
driver.find_element(by="name", value="email").send_keys(values[2])
box.send_keys(keys.ENTER)

time.sleep(5)
driver.quit()
