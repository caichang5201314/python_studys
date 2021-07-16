import unittest
from time import sleep
from unittest import TestCase

from automation.dao.MySQLHelper import MySQLHelper
from automation.pageobject.Goods import Goods
from automation.pageobject.Login import Login
from automation.utils.Logger import Logger

logger = Logger('TestGoods').getlog()


class TestGoods(TestCase, Goods, Login):

    @classmethod
    def setUpClass(cls):
        cls.data = MySQLHelper()

    def setUp(self):
        Login.open(self)
        Login.input_username(self)
        Login.input_password(self)
        Login.login_button(self)
        Goods.into_menu(self)
        Goods.click(self)
        Goods.out(self)
        Goods.into_main(self)

    @unittest.skip('111')
    def test_addGoods(self):
        Goods.click_add(self)
        Goods.goods_name(self)
        Goods.goods_category(self)
        Goods.submit(self)

    @unittest.skip('222')
    def test_search_goods(self):
        Goods.keyword(self)
        Goods.search_button(self)

    @unittest.skip('222')
    def test_unsale(self):
        Goods.keyword(self)
        Goods.search_button(self)
        sleep(1)
        # Goods.click_yes_gif(self)
        src_property = Goods.get_images(self)
        logger.info(src_property)

        if src_property == 'yes.gif':
            src_property = 1  # 1为上架
        else:
            src_property = 0

        query = "select goods_name,is_on_sale from ecs_goods where goods_name like '%尧海王%'"
        result = self.data.select(query, 'one')

        if result[1] == src_property:
            Goods.click_yes_gif(self)
            logger.info(result[1])
            sleep(2)
            sql = "select goods_name,is_on_sale from ecs_goods where goods_name like '%尧海王%'"
            result = self.data.select(sql, 'one')
            self.assertEqual(result[1], 0)
            # if result[1] == 1:
            #     logger.info('测试通过')
            #     print('测试通过')
            # else:
            #     logger.info('测试不通过')
            #     print('测试不通过')
        else:
            logger.info('页面有变更或sql有错误')

    def test_view(self):
        Goods.keyword(self)
        Goods.search_button(self)
        Goods.click_view_image(self)


    def tearDown(self):
        Goods.close_browser(self)

    @classmethod
    def tearDownClass(cls):
        cls.data.close()
