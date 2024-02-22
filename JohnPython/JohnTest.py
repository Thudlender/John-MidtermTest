from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import unittest

class TestCustomer(unittest.TestCase):
    

    def test_input1(self):
            driver = None
            driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("http://127.0.0.1/customer/customer.php")

        
            name = driver.find_element(By.ID, "firstName")
            last = driver.find_element(By.ID, "lastName")
            age = driver.find_element(By.ID, "age")
            drp_title = Select(driver.find_element(By.ID, "title"))
            drp_title.select_by_index(0)
        
            name.send_keys("johnjohn")
            last.send_keys("TangMo")
            age.send_keys("4")
        
            submit = driver.find_element(By.ID, "submit")
            submit.click()
        
            time.sleep(1)
        
            result = driver.find_element(By.ID, "firstName").text
            self.assertEqual("First Name: johnjohn", result)
            driver.save_screenshot("CaturedImg/TestJohnny01.png")
            driver.close()

    def test_input2(self):
            driver = None
            driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("http://127.0.0.1/customer/customer.php")
        
            name = driver.find_element(By.ID, "firstName")
            last = driver.find_element(By.ID, "lastName")
            age = driver.find_element(By.ID, "age")
            drp_title = Select(driver.find_element(By.ID, "title"))
            drp_title.select_by_index(0)
        
            name.send_keys("johnny")
            last.send_keys("canonc")
            age.send_keys("2")
        
            submit = driver.find_element(By.ID, "submit")
            submit.click()
        
            time.sleep(1)
        
            result = driver.find_element(By.ID, "firstName").text
            self.assertEqual("First Name: johnny", result)
            driver.save_screenshot("CaturedImg/TestJohnny02.png")
            driver.close()

    def test_input3(self):
            driver = None
            driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("http://127.0.0.1/customer/customer.php")
        
            name = driver.find_element(By.ID, "firstName")
            last = driver.find_element(By.ID, "lastName")
            age = driver.find_element(By.ID, "age")
            drp_title = Select(driver.find_element(By.ID, "title"))
            drp_title.select_by_index(0)
        
            name.send_keys("johnWeak")
            last.send_keys("NoneStop")
            age.send_keys("6")
        
            submit = driver.find_element(By.ID, "submit")
            submit.click()
        
            time.sleep(1)
        
            result = driver.find_element(By.ID, "firstName").text
            self.assertEqual("First Name: johnWeak", result)
            driver.save_screenshot("CaturedImg/TestJohnny03.png")
            driver.close()

    def test_input4(self):
            driver = None
            driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("http://127.0.0.1/customer/customer.php")
        
            name = driver.find_element(By.ID, "firstName")
            last = driver.find_element(By.ID, "lastName")
            age = driver.find_element(By.ID, "age")
            drp_title = Select(driver.find_element(By.ID, "title"))
            drp_title.select_by_index(0)
        
            name.send_keys("johnWeek")
            last.send_keys("BadBoy")
            age.send_keys("2")
        
            submit = driver.find_element(By.ID, "submit")
            submit.click()
        
            time.sleep(1)
        
            result = driver.find_element(By.ID, "firstName").text
            self.assertEqual("First Name: johnWeek", result)
            driver.save_screenshot("CaturedImg/TestJohnny04.png")
            driver.close()

    def test_input5(self):
            driver = None
            driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("http://127.0.0.1/customer/customer.php")
        
            name = driver.find_element(By.ID, "firstName")
            last = driver.find_element(By.ID, "lastName")
            age = driver.find_element(By.ID, "age")
            drp_title = Select(driver.find_element(By.ID, "title"))
            drp_title.select_by_index(0)
        
            name.send_keys("johnNotDoe")
            last.send_keys("NoneStart")
            age.send_keys("2")
        
            submit = driver.find_element(By.ID, "submit")
            submit.click()
        
            time.sleep(1)
        
            result = driver.find_element(By.ID, "firstName").text
            self.assertEqual("First Name: johnNotDoe", result)
            driver.save_screenshot("CaturedImg/TestJohnny05.png")
            driver.close()

    def test_input6(self):
            driver = None
            driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("http://127.0.0.1/customer/customer.php")
        
            name = driver.find_element(By.ID, "firstName")
            last = driver.find_element(By.ID, "lastName")
            age = driver.find_element(By.ID, "age")
            drp_title = Select(driver.find_element(By.ID, "title"))
            drp_title.select_by_index(0)
        
            name.send_keys("johnFront")
            last.send_keys("Stopped")
            age.send_keys("11")
        
            submit = driver.find_element(By.ID, "submit")
            submit.click()
        
            time.sleep(1)
        
            result = driver.find_element(By.ID, "firstName").text
            self.assertEqual("First Name: johnFront", result)
            driver.save_screenshot("CaturedImg/TestJohnny06.png")
            driver.close()

    def test_input7(self):
            driver = None
            driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("http://127.0.0.1/customer/customer.php")
        
            name = driver.find_element(By.ID, "firstName")
            last = driver.find_element(By.ID, "lastName")
            age = driver.find_element(By.ID, "age")
            drp_title = Select(driver.find_element(By.ID, "title"))
            drp_title.select_by_index(0)
        
            name.send_keys("johnDoe")
            last.send_keys("JoeMama")
            age.send_keys("15")
        
            submit = driver.find_element(By.ID, "submit")
            submit.click()
        
            time.sleep(1)
        
            result = driver.find_element(By.ID, "firstName").text
            self.assertEqual("First Name: johnDoe", result)
            driver.save_screenshot("CaturedImg/TestJohnny07.png")
            driver.close()

    def test_input8(self):
            driver = None
            driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("http://127.0.0.1/customer/customer.php")
        
            name = driver.find_element(By.ID, "firstName")
            last = driver.find_element(By.ID, "lastName")
            age = driver.find_element(By.ID, "age")
            drp_title = Select(driver.find_element(By.ID, "title"))
            drp_title.select_by_index(0)
        
            name.send_keys("Youngjohn")
            last.send_keys("Bobby")
            age.send_keys("45")
        
            submit = driver.find_element(By.ID, "submit")
            submit.click()
        
            time.sleep(1)
        
            result = driver.find_element(By.ID, "firstName").text
            self.assertEqual("First Name: Youngjohn", result)
            driver.save_screenshot("CaturedImg/TestJohnny08.png")
            driver.close()

    def test_input9(self):
            driver = None
            driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("http://127.0.0.1/customer/customer.php")
        
            name = driver.find_element(By.ID, "firstName")
            last = driver.find_element(By.ID, "lastName")
            age = driver.find_element(By.ID, "age")
            drp_title = Select(driver.find_element(By.ID, "title"))
            drp_title.select_by_index(0)
        
            name.send_keys("johnDough")
            last.send_keys("DoughNut")
            age.send_keys("22")
        
            submit = driver.find_element(By.ID, "submit")
            submit.click()
        
            time.sleep(1)
        
            result = driver.find_element(By.ID, "firstName").text
            self.assertEqual("First Name: johnDough", result)
            driver.save_screenshot("CaturedImg/TestJohnny09.png")
            driver.close()

    def test_input10(self):
            driver = None
            driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("http://127.0.0.1/customer/customer.php")
        
            name = driver.find_element(By.ID, "firstName")
            last = driver.find_element(By.ID, "lastName")
            age = driver.find_element(By.ID, "age")
            drp_title = Select(driver.find_element(By.ID, "title"))
            drp_title.select_by_index(0)
        
            name.send_keys("johnnyDepp")
            last.send_keys("Shipper")
            age.send_keys("9")
        
            submit = driver.find_element(By.ID, "submit")
            submit.click()
        
            time.sleep(1)
        
            result = driver.find_element(By.ID, "firstName").text
            self.assertEqual("First Name: johnnyDepp", result)
            driver.save_screenshot("CaturedImg/TestJohnny10.png")
            driver.close()

    def test_input11(self):
            driver = None
            driver_path = "D:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=driver_path)
            driver.get("http://127.0.0.1/customer/customer.php")
        
            name = driver.find_element(By.ID, "firstName")
            last = driver.find_element(By.ID, "lastName")
            age = driver.find_element(By.ID, "age")
            drp_title = Select(driver.find_element(By.ID, "title"))
            drp_title.select_by_index(0)
        
            name.send_keys("johnBrother")
            last.send_keys("LoveSister")
            age.send_keys("9")
        
            submit = driver.find_element(By.ID, "submit")
            submit.click()
        
            time.sleep(1)
        
            result = driver.find_element(By.ID, "firstName").text
            self.assertEqual("First Name: johnBrother", result)
            driver.save_screenshot("CaturedImg/TestJohnny11.png")
            driver.close()

    
if __name__ == "__main__":
    unittest.main()