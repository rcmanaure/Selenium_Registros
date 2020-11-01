from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstagramBot():
    def __init__(self, email, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.email = email
        self.password = password

    def logIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        sleep(2)

    def followUser(self, user):
        self.browser.get('https://www.instagram.com/' + user + '/')
        sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            sleep(2)
        else:
            print("Ya estas siguiendo a este Usuario")
    


# bot = InstagramBot('youremail', 'yourpassword')
# bot.signIn()
# bot.followWithUsername('therock')
# bot.unfollowWithUsername('therock')