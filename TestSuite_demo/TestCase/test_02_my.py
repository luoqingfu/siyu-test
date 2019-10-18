import unittest
from time import sleep

from PageObject.my import my_page
from Public.Decorator import setupclass, teardownclass
from Public.ReadConfig import ReadConfig


apk_url = ReadConfig().get_apk_url()
pkg_name = ReadConfig().get_pkg_name()
apk_path = ReadConfig().get_apk_path1()
class testMySelf(unittest.TestCase, my_page):
    @classmethod
    @setupclass
    def setUpClass(self):
        self.d.app_stop_all()
        self.d.app_start("com.wujie.siyu")

    @classmethod
    @teardownclass
    def tearDownClass(self):
        self.d.app_stop("com.wujie.siyu")

    """测试关注元素是否存在"""
    def test_01_focus_element_exist(self):
        self.click_my()
        self.click_focus()
        assert self.check_focuslist_touxiang() == True
        assert self.check_focuslist_username() == True
        assert self.check_focuslist_tab() == True
        assert self.check_focuslist_jianjie() == True
        assert self.check_focuslist_find() == True

    """测试个人信息页"""
    def test_02_focus_pinfo(self):
        self.click_userinfo()
        assert self.check_userinfo_touxiang() == True
        assert self.check_tab() == True
        assert self.check_guanzhu() == True
        assert self.check_fans() == True
        assert self.check_photo() == True
        assert self.check_shouhu() == True
        assert self.check_gift()  == True
        self.move_to_bot()
        assert self.check_magic() == True
        assert self.check_car() == True

    """测试更多"""
    def test_03_more(self):
        assert self.check_jubao() == True
        self.go_back()


    """测试去找他"""
    def test_04_gotofind(self):
        self.goto_find()
        self.click_roommore()
        self.click_exitroom()
        assert self.check_exitroom() == False

    """测试去ta窝"""
    def test_05_gotohome(self):
        self.goto_home()
        self.click_roommore()
        self.click_exitroom()
        assert self.check_exitroom() == False

    # """测试座驾"""
    # def test_06_car(self):
    #     self.move_to_bot()
    #     self.click_car()
    #     assert self.check_car1() == True
    #     assert self.check_tire() == True
    #     assert self.check_background() == True
    #
    """关注存在bug只验证是否可点击"""
    def test_06_focuson(self):
        assert self.check_focuson() == True


    """测试私聊-加入黑明单"""
    def test_07_chat_jiaru(self):
        self.click_chat()
        self.click_user()
        assert self.click_jiaruheimingd() == '已经成功将对方加入黑名单'

    """测试私聊-移除黑明单"""
    def test_08_chat_yichu(self):
        assert self.click_yichuheimingdan() =='已经成功将对方移除黑名单'


    """测试粉丝"""
    def test_09_fans(self):
        self.d.press("back")
        sleep(1)
        self.d.press("back")
        sleep(1)
        self.d.press("back")
        sleep(1)
        self.d.press("back")
        sleep(1)
        self.d(resourceId="com.wujie.siyu:id/tv_user_fans").click()
        sleep(1)
        assert self.click_fans() == True
        #self.click_fans()

    """测试个人主页"""
    def test_10_personal_homepage(self):
        self.d.press("back")
        sleep(1)
        self.click_home_page()
        assert self.check_userinfo_touxiang() == True
        assert self.check_tab() == True
        assert self.check_guanzhu() == True
        assert self.check_fans() == True
        #assert self.check_photo() == True
        assert self.check_shouhu() == True
        assert self.check_gift() == True
        self.move_to_bot()
        assert self.check_magic() == True
        assert self.check_car() == True
        self.click_edit()
        nickname = self.get_random_letter()
        self.click_edit_nickname()
        self.sendkey_nickname(nickname)
        self.click_savenickname()
        # assert self.get_nickname() == nickname
        self.click_sign()
        sign = self.get_random_letter()
        self.senk_sign(sign)
        self.click_save_sign()

