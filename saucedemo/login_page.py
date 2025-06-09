from playwright.sync_api import Page


xpaths = {
        'inp_username': "//input[@id='user-name']",
        'inp_password': "//input[@id='password']",
        'btn_login': "//input[@id='login-button']",
}

class LoginPage:
    
    def __init__(self, page: Page):
        self.page = page


    def fill_login_form(self, username: str = 'standard_user', password: str = 'secret_sauce'):
        self.page.fill(xpaths['inp_username'], username)
        self.page.fill(xpaths['inp_password'], password)
        self.page.click(xpaths['btn_login'])
        

