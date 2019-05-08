from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def before_all(context):

	context.browser = webdriver.Chrome('/Users/irwansyarifudin/Downloads/chromedriver')

def after_all(context):
	context.browser.quit()