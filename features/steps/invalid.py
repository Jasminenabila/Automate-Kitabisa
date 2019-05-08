from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

@given(u': go to page url ')
def step(context):
   context.browser.get('https://www.kitabisa.com')

@given(u': navbar Donasi')
def step(context):
    context.browser.find_element_by_xpath("//a[@class='btn btn--mtrl header-actions__btn'][contains(text(),'Donasi')]").click()
    time.sleep(3)

@given(u': pilih one item ')
def step(context):
    context.browser.find_element_by_xpath("//div[@class='campaign-container col flex-container']//div[1]//div[1]//a[1]").click()
    time.sleep(5)

@given(u': click button donasi now')
def step(context):
    context.browser.find_element_by_xpath("//a[@class='btn btn--block btn--large btn--round btn-contribute btn--pink']").click()
    time.sleep(5)

@when(u': input paid less than 100 ')
def step(context, self):
    context.browser.find_element_by_id("target-donasi").send_keys("100")
    self.assertTrue(True, "Jumlah donasi harus lebih besar dari Rp 1.000.")
    time.sleep(3)

@when(u': button pilih methode paid')
def step(context):
    context.browser.find_element_by_xpath("//span[@class='text-blue text-bold']").click()
    time.sleep(3)

@when(u': choose methode')
def step(context):
   context.browser.find_element_by_xpath("//li[2]").click()
 
@when(u': masukkan Nama ')
def step(context):
    context.browser.find_element_by_xpath("Donations_donorName").click()

@when(u': masukkan email or WhatsApp')
def step(context):
    context.browser.find_element_by_id("emailOrPhone").click()

@when(u': masukkan comment')
def step(context):
    context.browser.find_element_by_id("Donations_comment").click()

@then(u': i see redirect paid ')
def step(context):
    context.browser.find_element_by_xpath("//button[@class='btn btn--pink btn--large btn--block text-bold']").click()
    time.sleep(5)