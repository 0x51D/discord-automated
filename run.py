import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Discord:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('window-size=1280x720')
        self.browser = webdriver.Chrome(options=self.options)
    
    def testSel(self, email, password):
        self.browser.get('https://discord.com')
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_class_name('appButton-3GZ9-9').click()
        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]
        submitButton = self.browser.find_element_by_class_name('button-3k0cO7')

        emailInput.send_keys(email)
        passwordInput.send_keys(password)
        time.sleep(2)
        submitButton.click()

        time.sleep(5)

        addServer = self.browser.find_element_by_class_name('tutorialContainer-SGrQ1h')
        addServer.click()

Discord = Discord()
Discord.testSel('email', 'password')