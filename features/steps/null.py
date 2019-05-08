# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# import time

# @given(u':go to page ')
# def step(context):
#    context.browser.get('https://www.kitabisa.com')

# @given(u': click navbar Donasi')
# def step(context):
#     context.browser.find_element_by_xpath("//a[@class='btn btn--mtrl header-actions__btn'][contains(text(),'Donasi')]").click()
#     time.sleep(3)

# @given(u': pilih one item saja ')
# def step(context):
#     dricontextver.browser.find_element_by_xpath("//div[@class='campaign-container col flex-container']//div[1]//div[1]//a[1]").click()
#     time.sleep(5)

# @when(u': click button donasi ')
# def step(context):
#     context.browser.find_element_by_xpath("//a[@class='btn btn--block btn--large btn--round btn-contribute btn--pink']").click()
#     time.sleep(5)

# @then(u': i should see notif error ')
# def step(context):
#     context.browser.find_element_by_xpath("//button[@class='btn btn--pink btn--large btn--block text-bold']").click()
#     time.sleep(5)