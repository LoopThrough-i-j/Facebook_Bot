from selenium import webdriver
from secrets import *
from time import sleep
from selenium.webdriver.chrome.options import Options

class FB_Bot():

    def __init__(self):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 2 
        })
        self.driver = webdriver.Chrome()
    

    def login(self):
        self.driver.get("https://www.facebook.com/")
        sleep(3)
        email_id_box  = self.driver.find_element_by_xpath('//*[@id="email"]')
        password_box  = self.driver.find_element_by_xpath('//*[@id="pass"]')
        submit_button = self.driver.find_element_by_xpath('//*[@value="Log In"]')

        email_id_box.send_keys(email)
        password_box.send_keys(password)
        submit_button.click()
        sleep(2)
        #click anywhere on screen
        webdriver.common.action_chains.ActionChains(self.driver).click().perform()

    def Create_Post(self):
        
        
        self.driver.find_element_by_xpath('//*[@class="_4a0a img sp_XgkAvD-od66 sx_0f6ab7"]').click()
        sleep(3)
        message_field=self.driver.find_element_by_xpath('//*[@class="_1mf _1mj"]/span')
        message_field.send_keys("This is an automatically generated message in Python .Plz Hit a Like XD.")
        submit_message = self.driver.find_element_by_xpath('//*[@class="_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft"]')
        submit_message.click()



bot = FB_Bot()
bot.login()
bot.Create_Post()
