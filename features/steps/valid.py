from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

@given(u':go to page kitabisa ')
def step(context):
   context.browser.get('https://www.kitabisa.com')

@given(u': click navbar "Donasi"')
def step(context):
    context.browser.find_element_by_xpath("//a[@class='btn btn--mtrl header-actions__btn'][contains(text(),'Donasi')]").click()
    time.sleep(3)

@given(u': choose one item ')
def step(context):
    dricontextver.browser.find_element_by_xpath("//div[@class='campaign-container col flex-container']//div[1]//div[1]//a[1]").click()
    time.sleep(5)

@given(u': click button donasi sekarang')
def step(context):
    context.browser.find_element_by_xpath("//a[@class='btn btn--block btn--large btn--round btn-contribute btn--pink']").click()
    time.sleep(5)

@when(u': input paid ')
def step(context):
    context.browser.find_element_by_id("target-donasi").send_keys("100000")
    time.sleep(3)

@when(u': click button pilih methode paid')
def step(context):
    context.browser.find_element_by_xpath("//span[@class='text-blue text-bold']").click()
    time.sleep(3)

@when(u': click choose methode')
def step(context):
   context.browser.find_element_by_xpath("//li[2]").click()
 
@when(u': input Nama ')
def step(context):
    context.browser.find_element_by_xpath("Donations_donorName").click()

@when(u': Input email or WhatsApp')
def step(context):
    context.browser.find_element_by_id("emailOrPhone").click()

@when(u': input comment')
def step(context):
    context.browser.find_element_by_id("Donations_comment").click()

@then(u': i should see redirect paid ')
def step(context):
    context.browser.find_element_by_xpath("//button[@class='btn btn--pink btn--large btn--block text-bold']").click()
    time.sleep(5)