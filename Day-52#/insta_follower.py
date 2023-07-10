from selenium import webdriver


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome
        self.driver.get(url="https://www.instagram.com/accounts/login/")


    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass
