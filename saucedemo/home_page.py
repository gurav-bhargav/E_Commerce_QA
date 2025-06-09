from playwright.sync_api import Page, expect
from utils.logger import log_message

xpaths = {
    'txt_heading' : "//div[contains(text(), 'Swag Labs')]",
    'txt_products' : "//span[contains(text(), 'Products')]",
    'select_sorting_option' : "//select[@data-test='product-sort-container']",
    'first_item_name': "(//div[@data-test='inventory-item'])[1]//div[contains(text(), '{name}')]",
    'btn_of_product_of_name' : "//div[contains(text(), '{name}')]/ancestor::div[@data-test='inventory-item-description']//button",
    'txt_product_price' : "//div[contains(text(), '{name}')]/ancestor::div[@data-test='inventory-item-description']//div[@data-test='inventory-item-price']",
    'btn_cart': "//a[@data-test='shopping-cart-link']",

}

class Home_Page:
    selected_product_price = '0'
    selected_product_name = ''

    def __init__(self, page: Page):
        self.page = page

    def validate_home_page(self):
        expect(self.page.locator(xpaths['txt_products'])).to_be_visible()

    def select_sorting_option(self, option):
        self.page.select_option(xpaths['select_sorting_option'], option)

    def validate_order_of_items(self, order):
        name_by_za = 'Test.allTheThings() T-Shirt (Red)'
        name_by_price_low_to_high = 'Sauce Labs Onesie'
        name_by_price_high_to_low = 'Sauce Labs Fleece Jacket'
        name_of_product = ''
        if order == 'Name (Z to A)':
            name_of_product = name_by_za
        elif order == 'Price (low to high)':
            name_of_product = name_by_price_low_to_high
        elif order == 'Price (high to low)':
            name_of_product = name_by_price_high_to_low
            
        expect(self.page.locator(xpaths['first_item_name'].format(name=name_of_product))).to_be_visible()

    def add_product_named(self, name_of_product):
        # log_message('info', f'{xpaths['btn_of_product_of_name'].format(name_of_product)} is xpath of product') 
        self.page.click(xpaths['btn_of_product_of_name'].format(name=name_of_product))
        Home_Page.selected_product_name = name_of_product
        Home_Page.selected_product_price = self.page.locator(xpaths['txt_product_price'].format(name=name_of_product)).text_content()
        log_message('info', 'Selected product price is : '+Home_Page.selected_product_price)

    
    def navigate_to_cart(self):
        self.page.click(xpaths['btn_cart'])

    
    





