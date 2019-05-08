from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re, datetime
import HtmlTestRunner
import progressbar
import os
from time import sleep

class Test_input_100(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--incognito")
        options.add_argument("--no-sandbox")
        options.headless = True
        capabilities = options.to_capabilities()
        self.driver = webdriver.Chrome('/Users/irwansyarifudin/Documents/kitabisa2/chromedriver 4')
        self.verificationErrors = []
        self.accept_next_alert = True

        print('\n')
        print("Testing automation dengan mode headless dimulai ... ")
        bar = progressbar.ProgressBar(maxval=20, \
            widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        for i in range(20):
            bar.update(i+1)
            sleep(0.1)
        bar.finish()
        print('\n')

  
    def test_input_100(self):

        driver = self.driver

        self.driver.get("https://www.kitabisa.com")

        driver.fullscreen_window()
    

        driver.find_element_by_xpath("//a[@class='btn btn--mtrl header-actions__btn'][contains(text(),'Donasi')]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[@class='campaign-container col flex-container']//div[1]//div[1]//a[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//a[@class='btn btn--block btn--large btn--round btn-contribute btn--pink']").click()
        element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='white-box white-box--desc block large-margin-top']"))

        )
        time.sleep(5)
        print("success to page donasi")

        driver.find_element_by_id("target-donasi").click()
        driver.find_element_by_id("target-donasi").send_keys("100")
        time.sleep(3)
        print("success input donasi")
        driver.find_element_by_xpath("//p[contains(text(),'Jumlah donasi harus lebih besar dari Rp 1.000.')]").text
        self.assertTrue(True, "Jumlah donasi harus lebih besar dari Rp 1.000.")

        driver.find_element_by_id("Donations_donorName").click()
        driver.find_element_by_id("Donations_donorName").send_keys("test123")
        print("success donasi nama")

        driver.find_element_by_id("emailOrPhone").click()
        driver.find_element_by_id("emailOrPhone").send_keys("test@gmail.com")
        print("success isi email/phone")

        driver.find_element_by_id("Donations_comment").click()
        driver.find_element_by_id("Donations_comment").send_keys("Get well soon ya !!")
        print("success isi comment")

        driver.find_element_by_xpath("//button[@class='btn btn--pink btn--large btn--block text-bold']").click()
        print("redirect to page paid")
        time.sleep(5)
        


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
    # testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir')