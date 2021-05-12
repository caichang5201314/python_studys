# -*- coding: utf-8 -*-
from selenium_pom.service.Login import Login


class LoginCase(Login):

    def test_login(self):
        Login.open_url(self)
        Login.input_username(self)
        Login.input_password(self)
        Login.click_login_button(self)

    
    def test_logout(self):
        self.test_login()
        Login.into_frame(self)
        Login.click_logout(self)   


case = LoginCase()
case.test_login()