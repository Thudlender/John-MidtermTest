import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class TestCustomerForm(unittest.TestCase):

    def test_case1(self):
        driver = webdriver.Chrome(executable_path="D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver.get("http://127.0.0.1/customer/customer.php")
        
        firstNameInput = driver.find_element(By.ID, "first-name")
        lastNameInput = driver.find_element(By.ID, "last-name")
        ageInput = driver.find_element(By.ID, "age")
        submitButton = driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canonc")
        ageInput.send_keys("2")

        # Submit the form
        submitButton.click()
        
        result = driver.find_element(By.ID, "firstname").text
        self.assertEqual("First Name: johnjohn", result)
        
        driver.close()

    # Define other test_case methods similarly

if __name__ == "__main__":
    unittest.main()