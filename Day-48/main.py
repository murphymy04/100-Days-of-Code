from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

clicker = driver.find_element(by="id", value="cookie")

upgrades = driver.find_elements(by="css selector", value="#store div")
upgrades = [i.get_attribute("id") for i in upgrades]
upgrades.remove(upgrades[-1])


def get_prices():
    prices = driver.find_elements(by="css selector", value="#store b")
    prices.remove(prices[-1])
    for i in range(len(prices)):
        prices[i] = int(prices[i].text.split("- ")[1].strip().replace(",", ""))
    return prices


def highest(money, price, upgrade_id):
    possible_purchase = []
    items_dict = {}
    for i in range(len(price)):
        if money >= price[i]:
            possible_purchase.append(price[i])
        items_dict.update({price[i]: upgrade_id[i]})
    if money >= price[0]:
        purchase = max(possible_purchase)
        upgrader = driver.find_element(by="id", value=f"{items_dict.get(purchase)}")
        upgrader.click()


current_time = time.time()
stop_time = current_time + (60 * 5)

while True:
    clicker.click()
    cookie_count = int(driver.find_element(by="id", value="money").text)
    value_of_item = get_prices()
    highest(cookie_count, value_of_item, upgrades)
    current_time = time.time()
    if current_time >= stop_time:
        velocity = driver.find_element(by="id", value="cps")
        print(velocity)
        break

driver.quit()
