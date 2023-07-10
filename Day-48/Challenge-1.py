from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.python.org")

time = driver.find_elements(by="css selector", value=".event-widget time")
name = driver.find_elements(by="css selector", value=".event-widget li a")
events = {}

for i in range(len(time)):
    events[i] = {
        "time": time[i].text,
        "name": name[i].text
    }

print(events)

driver.quit()
