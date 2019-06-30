from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
	def add_product_to_cart(self):
		cart_link = self.browser.find_element(*ProductPageLocators.CART_LINK)
		cart_link.click()

	def should_be_product_page(self):
		self.should_be_product_url()
		self.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину

	def should_be_product_url(self):
		assert '?promo=' in self.browser.current_url, "Not product url"

	def should_be_add_to_cart_button(self):
		assert self.is_element_present(*ProductPageLocators.CART_LINK), "No cart button"
	
	def should_be_success_message(self):
		assert self.is_element_present(*ProductPageLocators.CART_PRODUCT_NAME), "No success message"

	def should_be_valid_cart_name(self):
		product_name = self.browser.find_element(*ProductPageLocators.PAGE_PRODUCT_NAME)
		cart_product_name = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_NAME)
		assert product_name.text == cart_product_name.text, "Invalid product name"
		
	def should_be_valid_cart_price(self):
		product_price = self.browser.find_element(*ProductPageLocators.PAGE_PRODUCT_PRICE)
		cart_product_price = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_PRICE)
		assert product_price.text == cart_product_price.text, "Invalid product price"
