import unittest
import time
import warnings
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class TestLogin(unittest.TestCase): 

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        s=Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, options=options)
        warnings.simplefilter('ignore', ResourceWarning)
       
    def test1_success_login(self): 
        driver = self.driver
        driver.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("ganjar@ganjar.co")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[2]").send_keys("ganjar")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)

        response_data = driver.find_element(By. XPATH, "/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text

        self.assertEqual(response_data, 'Welcome ganjar')
        self.assertEqual(response_message, 'Anda Berhasil Login')

    def test2_failed_login_with_empty_email_and_password(self):
        driver = self.driver
        driver.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[2]").send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)

        response_data = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(response_data, 'Email tidak valid')
        self.assertEqual(response_message, 'Cek kembali email anda')

    def test3_failed_login_with_empty_email(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[2]").send_keys("ganjar")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)

        response_data = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(response_data, 'Email tidak valid')
        self.assertEqual(response_message, 'Cek kembali email anda')

    def test4_failed_login_with_password_contain_symbol(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("ganjar@ganjar.co")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[2]").send_keys("g@nj@r")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)

        response_data = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(response_data, 'Password tidak valid')
        self.assertEqual(response_message, 'Tidak boleh mengandung symbol')

    def test5_failed_login_with_empty_password(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("ganjar@ganjar.co")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[2]").send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)

        response_data = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(response_data, "User's not found")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test6_failed_login_with_phone_number_in_email(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("081345755941")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[2]").send_keys("ganjar")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)

        username = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/form/input[1]")))
        assert username.get_attribute("validationMessage") == "Please include an '@' in the email address. '" + username.get_attribute('value') + "'" + " is missing an '@'."

    def test7_failed_login_with_password_contain_numbers(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("ganjar@ganjar.co")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[2]").send_keys("g4nj4r")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)

        response_data = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(response_data, "User's not found")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test8_failed_login_with_unregistered_email(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("ganjar@ganjar.co.id")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[2]").send_keys("ganjar")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)

        response_data = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(response_data, "User's not found")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

    def test9_failed_login_with_password_turned_uppercase(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]").send_keys("ganjar@ganjar.co")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[2]").send_keys("GANJAR")
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[3]").click()
        time.sleep(3)

        response_data = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/h2").text
        response_message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]").text
        self.assertEqual(response_data, 'Email tidak valid')
        self.assertEqual(response_message, 'Cek kembali email anda')

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()