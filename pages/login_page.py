from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    def __init__(self, page: Page): 
        self.page = page
         # XPath locator for Sign in link
        #self.signin = "(//a[@class='c2wr2i0 mnneh15 mnneh159 mnneh1p mnneh165 mnneh1h jkru9p0 qzdt2k0' and @href='/oauth/login?returnUrl=%2F'' and @title='Sign in'])[1]"
        self.sign_in = page.locator("//a[@class='nav__button-secondary btn-secondary-emphasis ml-3 btn-md']")
        self.usrname = page.locator("#username")
        self.pswd = page.locator("#password")
        self.log_in = page.locator("//button[@class='btn__primary--large from__button--floating']")
        self.profile = page.locator("//h3[@class='profile-card-name text-heading-large']")

    def login(self, username: str, password: str):
     self.navigate("https://www.linkedin.com/")   # go to JobsDB HK homepage
     self.sign_in.click()
     self.usrname.fill(username)
     self.pswd.fill(password)
     self.log_in.click()
     text = self.profile.text_content()
     return text
     
    # Now interact with the popup login page
     