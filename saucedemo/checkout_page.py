from playwright.sync_api import Page, expect 

xpaths = {
    'inp_field' : "//input[@id='{id}']",
    'btn_finish' : "//button[@id='finish']",
    'txt_order_complete' : "//h2[contains(text(), 'Thank you for your order!')]",
}

class Checkout_Page:

    def __init__(self, page: Page):
        self.page = page 

    def fill_form(self):
        self.page.fill(xpaths['inp_field'].format(id='first-name'), 'Test')
        self.page.fill(xpaths['inp_field'].format(id='last-name'), 'User')
        self.page.fill(xpaths['inp_field'].format(id='postal-code'), '425002')
        self.page.click(xpaths['inp_field'].format(id='continue'))
        self.page.click(xpaths['btn_finish'])

    def validate_order_completion(self):
        expect(self.page.locator(xpaths['txt_order_complete'])).to_be_visible()


    


    
