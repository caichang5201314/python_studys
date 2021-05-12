# -*- coding: utf-8 -*-
from time import sleep

from case.LoginCase import LoginCase
from dao.MySQLHelper import MySQLHelper
from service.Goods import Goods
from utils.Config import Config
from utils.Logger import Logger


logger =Logger('GoodsCase').getlog()

class GoodsCase(LoginCase, Goods):
    file = '../conf/config.ini'
    def __init__(self):
        self.config = Config(self.file)
        
    def get_db(self):
        my = MySQLHelper()
        my.host=self.config.get_value(self.file, 'mysql', 'host')
        my.user=self.config.get_value(self.file, 'mysql', 'user')
        my.password=self.config.get_value(self.file, 'mysql', 'password')
        my.database=self.config.get_value(self.file, 'mysql', 'database')
        my.port=int(self.config.get_value(self.file, 'mysql', 'port'))
        return my

    # 进入商品列表的公共方法
    def common(self):
        LoginCase.test_login(self)
        Goods.click_goods_menu(self)
        Goods.out_frame(self)
        Goods.into_frame(self)
    
    # 按照分类下拉且输入关键字,2者组合查询
    def search(self):
        self.common()
        Goods.input_by_keword(self)
        Goods.all_category(self)
        Goods.search_button(self)
    
    # 添加商品
    def add_goods(self):
        self.common()
        Goods.add_goods_button(self)
        Goods.goods_name(self)
        Goods.all_category(self)
        Goods.submit(self)
        
        sql="select * from ecs_goods where goods_name='包包爱宝宝'"
        logger.info('你执行的sql是:['+sql+']')
        result = self.get_db().select(sql, 'one')
        logger.info('执行结果是:%s' %str(result))
        if result[3]=='包包爱宝宝':
            print('ok')
            logger.info('测试通过')
        else:
            print('fail')
        
        
        
    
    # 下架
    def goods_ground(self):
        self.search()
        sleep(2)
        
        goods_id = Goods.get_goods_id(self)
        print(goods_id)
        #点击之前
        before=Goods.get_src_path(self)
        before_sql = "select is_on_sale from ecs_goods where goods_id=%d" %int(goods_id)
        before_result = self.get_db().select(before_sql, 'one')
        print(before_result)
        #点击
        
        Goods.only_onclick(self)
        sleep(2)
        
        #点击之后
        after=Goods.get_src_path(self)
        after_sql = "select is_on_sale from ecs_goods where goods_id=%d" %int(goods_id) 
        after_result = self.get_db().select(after_sql, 'one')
        print(after_result)
        #判断点击前后的结果,必须均不一致
        if before!=after and after_result[0]==0 and before_result[0]!=after_result[0]:
            print('ok')
        else:
            print('fail')
        


g = GoodsCase()
g.add_goods()
