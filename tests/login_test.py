import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import moment
import time


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            time.sleep(2)
            x = driver.title
            assert x == "OrangeHRM"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currentTime = moment.now().strftime("%d/%m/%Y_%H:%M:%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currentTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,attachment_type=allure.attachment_type.PNG)
            # driver.get_screenshot_as_file("C:/Users/rotem/PycharmProjects/AutomationFramework_1/screenshots/"+screenshotName+".png")
            driver.get_screenshot_as_file("C:/Users/rotem/PycharmProjects/AutomationFramework_1/screenshots/"+"filename.png")
            raise

        except:
            print("There was an exception")
            raise

        else:
            print("No exceptions occurred")

        finally:
            print("I am inside the finally block")

