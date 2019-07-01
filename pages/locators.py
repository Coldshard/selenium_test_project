from selenium.webdriver.common.by import By

class BasePageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	CART_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default:nth-child(1)")

class MainPageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
	ADD_TO_CART_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
	PAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
	PAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	CART_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
	CART_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

class CartPageLocators(object):
	ITEMS_LINK = (By.CSS_SELECTOR, ".basket-items")
	EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#content_inner p")
