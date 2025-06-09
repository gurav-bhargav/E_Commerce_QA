from playwright.sync_api import Page, expect 
from .home_page import Home_Page

xpaths = {
    'txt_product_name' : "//div[@data-test='inventory-item-name']",
    'txt_product_price' : "//div[@data-test='inventory-item-price']",
    'btn_remove' : "//button[contains(text(), 'Remove')]",
    'btn_checkout' : "//button[@id='checkout']",
}

class Cart_Page:

    def __init__(self, page: Page):
        self.page = page 

    def validate_product_name_price(self):
        expect(self.page.locator(xpaths['txt_product_name'])).to_have_text(Home_Page.selected_product_name)
        expect(self.page.locator(xpaths['txt_product_price'])).to_have_text(Home_Page.selected_product_price)

    def checkout(self):
        self.page.click(xpaths['btn_checkout'])

    


    
