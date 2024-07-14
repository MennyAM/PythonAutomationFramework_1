from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_xpath = "(//p[@class='oxd-userdropdown-name'])[1]"
        self.logout_link_linkText = "Logout"

    def click_welcome(self):
        self.driver.find_element(By.XPATH, self.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()
