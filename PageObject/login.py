from time import sleep

from Public.Decorator import *


class login_page(BasePage):
    @teststep
    def input_username(self, text):
        log.i('输入用户名:%s'% text)
        self.d(resourceId='com.wujie.siyu:id/et_phone').send_keys(text)

    @teststep
    def input_password(self, text):
        log.i('输入密码:%s', text)
        self.d(resourceId='com.wujie.siyu:id/et_password').send_keys(text)

    @teststep
    def click_register_btn(self):
        log.i('点击注册按钮')
        self.d(resourceId='com.wujie.siyu:id/tv_register').click()

    @teststep
    def click_login_btn(self):
        log.i('点击登录按钮')
        self.d(resourceId='com.wujie.siyu:id/stv_login').click()

    @teststep
    def get_info(self):
        info = self.d(resourceId='com.wujie.siyu:id/btn_get_code').info
        info = info['clickable']
        log.i('获取的信息是%s' % info)
        return info

    @teststep
    def click_resetpwd_btn(self):
        sleep(2)
        log.i('点击重置密码按钮')
        self.d(resourceId='com.wujie.siyu:id/tv_forgetPwd').click()

