from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import random

class instagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def CloseBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        login_button = driver.find_element_by_xpath('//a[@href="/accounts/login/?source=auth_switcher"]')
        login_button.click()
        time.sleep(3)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        pass_elem = driver.find_element_by_xpath("//input[@name='password']")
        pass_elem.clear()
        pass_elem.send_keys(self.password)
        pass_elem.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.get('https://www.instagram.com/scorpion_112233/')

    def like_photo(self,hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(3)

        pic_hrefs = []
        for i in range(1,2):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(3)

                hrefs_in_view = driver.find_elements_by_tag_name('a')
                pic_hrefs = [elem.get_attribute('href') for elem in hrefs_in_view if '.com/p/' in elem.get_attribute('href')]

            except Exception :
                continue

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(3)
            try:
                time.sleep(random.randint(2,6))
                driver.find_element_by_xpath('//button[@type="button"]').click()
            except Exception as e :
                time.sleep(3)

usernamee='scorpion_112233'
passwordd='09375947271'
ig = instagramBot(usernamee,passwordd)
ig.login()

hashtag = ['linux']
while True:
    try:
        tag = random.choice(hashtag)
        ig.like_photo(tag)
    except Exception:
        ig.CloseBrowser()
        time.sleep(5)
        ig = instagramBot(usernamee,passwordd)
        ig.login()

