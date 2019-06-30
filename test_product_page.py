from .pages.product_page import ProductPage
import pytest

params = [f'offer{x}' for x in range(10)]

@pytest.mark.parametrize('param', params)
def test_guest_can_add_product_to_cart(browser, param):
	
	link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={param}'
	page = ProductPage(browser, link)
	page.open()
	page.should_be_product_page()
	page.add_product_to_cart()			# жмем кнопку добавить в корзину 
	page.solve_quiz_and_get_code()
	page.should_be_success_message()	  # проверяем что есть сообщение с нужным текстом
	page.should_be_valid_cart_name()
	page.should_be_valid_cart_price()
