# -*- coding: utf-8 -*-
from base.BasePage import BasePage


class Goods(BasePage):
    
    def click_goods_menu(self):
        BasePage.into_frame(self, 'menu-frame')
        BasePage.click(self, 'link_text=>商品列表')
    
    def all_category(self):
        BasePage.select_by_text(self, 'name=>cat_id', '智能硬件')
        
    def search_button(self):
        BasePage.click(self, "xpath=>//input[@value=' 搜索 ']")
       
    def out_frame(self):
        BasePage.out_frame(self)     
        
    def into_frame(self):
        BasePage.into_frame(self, 'main-frame')
        
    def input_by_keword(self):
        BasePage.input(self, 'name=>keyword', '包包爱宝宝')
        
    def add_goods_button(self):
        BasePage.click(self, "xpath=>//a[@href='goods.php?act=add']")
    
    def goods_name(self):
        BasePage.input(self, 'name=>goods_name', '包包爱宝宝')
        
    def submit(self):
        BasePage.click(self, "xpath=>//input[@value=' 确定 ']")
        
    def get_src_path(self):
        result = BasePage.get_value_by_attribute(self, "xpath=>//*[@id='listDiv']/table[1]/tbody/tr[3]/td[5]/img", 'src')
        return result
    
    def only_onclick(self):
        BasePage.click(self, 'xpath=>//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[5]/img')
        
    def get_goods_id(self):
        goods_id = BasePage.get_value_by_attribute(self, "xpath=>//*[@id='listDiv']/table[1]/tbody/tr[3]/td[1]/input", 'value')
        return goods_id
