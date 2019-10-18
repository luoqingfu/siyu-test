import unittest

from PageObject.my_other import my_other_page
from Public.Decorator import setupclass, teardownclass



class testMyOther(unittest.TestCase, my_other_page):
    @classmethod
    @setupclass
    def setUpClass(self):
        self.d.app_stop_all()
        self.d.app_start("com.wujie.siyu")

    @classmethod
    @teardownclass
    def tearDownClass(self):
        self.d.app_stop("com.wujie.siyu")


    """测试钱包元素"""
    def test_01_wallet(self):
        self.click_my()
        self.click_wallet()
        assert self.check_yue ==True



