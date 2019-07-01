from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
	def should_not_be_items_in_cart(self):
		assert self.is_not_element_present(*CartPageLocators.ITEMS_LINK), "Cart is not empty"
		
	def should_be_empty_cart_text(self):
		cart_text = self.browser.find_element(*CartPageLocators.EMPTY_CART_TEXT)
		assert cart_text.text == 'Your basket is empty. Continue shopping', "Cart is not empty"
