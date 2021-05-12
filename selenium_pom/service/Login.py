# -*- coding: utf-8 -*-
from selenium_pom.base.BasePage import BasePage


class Login(BasePage):
    
    #根据name来输入内容
    def input_username(self):
        BasePage.input(self, 'name=>username', 'caichang')
       
    def input_password(self):
        BasePage.input(self, 'name=>password', 'caichang1') 
    
    def click_login_button(self):
        BasePage.click(self, 'class_name=>btn-a')
        
    def into_frame(self):
        BasePage.into_frame(self, 'header-frame')
        
    def click_logout(self):
        BasePage.mouse_hover(self, 'link_text=>个人设置')
        BasePage.click(self, 'link_text=>退出')

