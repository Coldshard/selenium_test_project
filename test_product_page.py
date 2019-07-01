from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest

# params = [f'offer{x}' for x in range(10)]

# @pytest.mark.parametrize('param', params)
# def test_guest_can_add_product_to_cart(browser, param):
	# link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={param}'
	# page = ProductPage(browser, link)
	# page.open()
	# page.should_be_product_page()
	# page.add_product_to_cart()			# жмем кнопку добавить в корзину 
	# page.solve_quiz_and_get_code()
	# page.should_be_success_message()	  # проверяем что есть сообщение с нужным текстом
	# page.should_be_valid_cart_name()
	# page.should_be_valid_cart_price()

# def test_guest_cant_see_success_message(browser):
	# link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
	# page = ProductPage(browser, link)
	# page.open()
	# page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()
	
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_cart_page()
	cart_page = CartPage(browser, browser.current_url)
	cart_page.should_not_be_items_in_cart()
	cart_page.should_be_empty_cart_text()
