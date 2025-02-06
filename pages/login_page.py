import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):

    @allure.step("Вход в личный кабинет пользователя")
    def authorization(self, mail, password):
        self.find_element(LoginLocators.LOGIN_IN_ACCOUNT).click()
        self.write_in_field(LoginLocators.EMAIL_INPUT, mail)
        self.write_in_field(LoginLocators.PASSWORD_INPUT, password)
        self.find_element(LoginLocators.LOGIN_BTN).click()