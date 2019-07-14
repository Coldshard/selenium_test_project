from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage(object):
	@pytest.fixture(scope="function", autouse=True)
	def test_guest_can_go_to_login_page(self, browser):
		link = "http://selenium1py.pythonanywhere.com"
		page = MainPage(browser, link)
		page.open()
		page.go_to_login_page()
		login_page = LoginPage(browser, browser.current_url)
		login_page.should_be_login_page()

	def test_guest_should_see_login_link(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
		page = MainPage(browser, link)
		page.open()
		page.should_be_login_link()

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
	page = MainPage(browser, link)
	page.open()
	page.go_to_cart_page()
	cart_page = CartPage(browser, browser.current_url)
	cart_page.should_not_be_items_in_cart()
	cart_page.should_be_empty_cart_text()
