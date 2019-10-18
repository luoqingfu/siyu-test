import unittest
from time import sleep

from PageObject.login import login_page
from Public.Decorator import setupclass, teardownclass
from Public.ReadConfig import ReadConfig


apk_url = ReadConfig().get_apk_url()
pkg_name = ReadConfig().get_pkg_name()
apk_path = ReadConfig().get_apk_path1()
username = ReadConfig().get_testdata('user_name')
pwd = ReadConfig().get_testdata('password')
class testLogin(unittest.TestCase, login_page):
    @classmethod
    @setupclass
    def setUpClass(self):
        self.local_install(apk_path)
        self.d.app_stop_all()
        self.d.app_start("com.wujie.siyu")

    @classmethod
    @teardownclass
    def tearDownClass(self):
        self.d.app_stop("com.wujie.siyu")

    """测试注册"""
    def test_01_register(self):
        self.d.wait_activity('com.yizhuan.cutesound.ui.login.LoginActivity', timeout=10)
        self.d.watcher("始终允许").when(text="始终允许").click(text="始终允许")
        self.click_register_btn()
        self.input_username(username[0])
        sleep(2)
        info = self.get_info()
        self.d.press("back")
        self.d.press("back")
        assert info == True

    """重置密码"""
    def test_02_resetpwd(self):
        self.click_resetpwd_btn()
        self.input_username(username[0])
        sleep(2)
        info = self.get_info()
        self.d.press("back")
        self.d.press("back")
        assert info == True

    """测试登录"""
    def test_03_login(self):
        self.d.wait_activity('com.yizhuan.cutesound.ui.login.LoginActivity', timeout=10)
        sleep(2)
        self.input_username(username[0])
        self.input_password(pwd[0])
        self.click_login_btn()
        self.d.wait_activity('com.yizhuan.cutesound.MainActivity', timeout=10)
        assert self.d(resourceId='com.wujie.siyu:id/main_home_tab').exists() == True


