from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Here chromedriver is installed and in PATH
        self.driver.get("C://Users//tanma//Downloads//Pibit.ai SDET Assignment Tanmay Agrawal//Part2.html")  # Replace with the actual path to your HTML file

    def test_successful_login(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("validUsername")
        driver.find_element(By.ID, "password").send_keys("validPassword")
        driver.find_element(By.ID, "login").click()
        # Adding sample assertion to check for successful login
        success_message = driver.find_element(By.ID, "successMessage").text
        self.assertEqual(success_message, "Login successful!", "Login should be successful")

    def test_failed_login(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("invalidUsername")
        driver.find_element(By.ID, "password").send_keys("invalidPassword")
        driver.find_element(By.ID, "login").click()
        # Adding sample assertion to check for failed login
        error_message = driver.find_element(By.ID, "errorMessage").text
        self.assertEqual(error_message, "Invalid username or password.", "Error message should be displayed")

    def test_empty_fields(self):
        driver = self.driver
        driver.find_element(By.ID, "login").click()
        # Adding sample assertion to check for handling empty fields
        error_message = driver.find_element(By.ID, "errorMessage").text
        self.assertEqual(error_message, "Please enter username and password.", "Error message for empty fields should be displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    