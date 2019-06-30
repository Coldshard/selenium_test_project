from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
	def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
		
	def go_to_cart(self):
		cart_link = self.browser.find_element(*MainPageLocators.CART_LINK)
		cart_link.click()

	def should_not_be_items_in_cart(self):
		assert self.is_not_element_present(*MainPageLocators.ITEMS_LINK), "Cart is not empty"
		
	def should_be_empty_cart_text(self):
		assert (*MainPageLocators.EMPTY_CART_TEXT).text == 'Your basket is empty.', "Cart is not empty"

	# def go_to_login_page(self):
		# link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
		# link.click()
		# alert = self.browser.switch_to.alert
		# alert.accept()
		# # return LoginPage(browser=self.browser, url=self.browser.current_url)
