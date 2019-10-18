import random
from time import sleep

from Public.Decorator import *


class my_page(BasePage):

    @teststep
    def click_my(self):
        log.i('点击我的tab')
        self.d.implicitly_wait(10)
        self.d(resourceId='com.wujie.siyu:id/main_me_tab').click()

    @teststep
    def click_focus(self):
        log.i('点击关注')
        self.d.implicitly_wait(10)
        self.d(resourceId='com.wujie.siyu:id/tv_user_attentions').click()

    @teststep
    def check_focuslist_touxiang(self):
        log.i('检查关注列表-头像',self.d(resourceId='com.wujie.siyu:id/avatar_layout').exists)
        if self.d(resourceId='com.wujie.siyu:id/avatar_layout').exists:
            return True
        else:
            return False


    @teststep
    def check_focuslist_username(self):
        log.i('检查关注列表-昵称')
        if self.d.xpath('//*[@resource-id="com.wujie.siyu:id/tv_userName"]').exists:
            return True
        else:
            return False

    @teststep
    def check_focuslist_tab(self):
        log.i('检查关注列表-标签')
        if self.d(resourceId='com.wujie.siyu:id/tags_view').exists:
            return True
        else:
            return False

    @teststep
    def check_focuslist_jianjie(self):
        log.i('检查关注列表-简介')
        if self.d.xpath('//*[@resource-id="com.wujie.siyu:id/tv_gender"]').exists:
            return True
        else:
            return False

    @teststep
    def check_focuslist_find(self):
        log.i('检查关注列表-去找ta')
        if self.d(resourceId='com.wujie.siyu:id/find_him_layout').exists:
            return True
        else:
            return False

    @teststep
    def click_userinfo(self):
        log.i('进入个人信息页面')
        self.d.xpath('//*[@resource-id="com.wujie.siyu:id/rly"]/android.widget.LinearLayout[1]').click()

    @teststep
    def check_userinfo_touxiang(self):
        log.i('个人信息头像')
        if self.d(resourceId='com.wujie.siyu:id/rl_avatar').exists:
            return True
        else:
            return False

    @teststep
    def check_guanzhu(self):
        log.i('检查关注')
        if self.d(resourceId='com.wujie.siyu:id/ll_attention').exists:
            return True
        else:
            return False

    @teststep
    def check_tab(self):
        log.i('检查用户标签')
        if self.d(resourceId='com.wujie.siyu:id/ll_level').exists:
            return True
        else:
            return False

    @teststep
    def check_fans(self):
        log.i('检查粉丝')
        if  self.d(resourceId='com.wujie.siyu:id/ll_fans').exists:
            return True
        else:
            return False

    @teststep
    def check_photo(self):
        log.i('检查用户相片')
        if self.d(resourceId='com.wujie.siyu:id/photo_fl_data').exists:
            return True
        else:
            return False

    @teststep
    def check_shouhu(self):
        log.i('检查守护榜')
        if self.d.xpath('//android.widget.ScrollView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]')\
            .exists:
            return True
        else:
            return False

    @teststep
    def check_gift(self):
        log.i('检查礼物')
        if self.d(resourceId='com.wujie.siyu:id/gift_number').exists:
            return True
        else:
            return False

    @teststep
    def check_car(self):
        log.i('检查座驾')
        if self.d(resourceId='com.wujie.siyu:id/car_layout').exists:
            return True
        else:
            return False

    @teststep
    def check_magic(self):
        log.i('检查魔法')
        if self.d(resourceId='com.wujie.siyu:id/magic_tv_number').exists:
            return True
        else:
            return False

    @teststep
    def move_to_bot(self):
        log.i('移动到底部')
        self.d.swipe(535, 2033, 672, 231, 0.1)
        # self.d.touch.down(0.511, 0.733)
        # time.sleep(2)
        # self.d.touch.move(0.628, 0.274)
        # self.d.touch.up()

    @teststep
    def click_more(self):
        log.i('点击更多')
        self.d(resourceId='com.wujie.siyu:id/iv_more').click()

    @teststep
    def check_jubao(self):
        log.i('点击举报')
        self.d(resourceId='com.wujie.siyu:id/iv_more').click()
        self.d(resourceId='com.wujie.siyu:id/ll_more').click()
        self.d.xpath('//*[@text="涉及诈骗、辱骂违规信息"]').click()
        self.d(text="确认").click()
        info = self.d(text="确认").info
        info = info['clickable']
        log.i('获取的信息是%s' % info)
        return info


    @teststep
    def go_back(self):
        log.i('返回上一页')
        self.d.xpath('//android.widget.RelativeLayout').click()
        return self.d(resourceId='com.wujie.siyu:id/iv_avatar').exists


    @teststep
    def goto_find(self):
        log.i('点击去找ta')
        self.d(resourceId='com.wujie.siyu:id/tv_user_where').click()

    @teststep
    def check_inroom(self):
        log.i('检查是否进入了直播间')
        if self.d(resourceId='com.wujie.siyu:id/tv_user_where').exists:
            return True
        else:
            return False

    @teststep
    def click_roommore(self):
        log.i('点击roommore')
        self.d(resourceId='com.wujie.siyu:id/room_more').click()

    @teststep
    def click_exitroom(self):
        log.i('点击退出房间')
        self.d(text="退出房间").click()

    @teststep
    def check_exitroom(self):
        log.i('检查是否退出房间%s'%self.d(resourceId="com.wujie.siyu:id/room_send_gift_layout").exists())
        if self.d(resourceId="com.wujie.siyu:id/room_send_gift_layout").exists():
            return True
        else:
            return False

    @teststep
    def goto_home(self):
        log.i('移动到顶部')
        self.d.swipe(672, 231, 535, 2033, 0.1)
        log.i('去ta窝')
        self.d(resourceId="com.wujie.siyu:id/tv_user_room").click()

    @teststep
    def click_car(self):

        log.i('点击送ta一辆')
        self.d.xpath('//*[@resource-id="com.wujie.siyu:id/car_recycler_view"]/android.widget.FrameLayout[1]').click()

    @teststep
    def check_shop(self):
        log.i('检查是否进入装扮商城')
        if self.d(text="装扮商城").exists:
            return True
        else:
            return False

    @teststep
    def check_car1(self):
        log.i('检查座驾')
        self.d(resourceId="com.wujie.siyu:id/car_indicator").click()
        if self.d(resourceId="com.wujie.siyu:id/tv_car_name", text="招财猫").exists:
            return True
        else:
            return False

    @teststep
    def check_tire(self):
        log.i('检查头饰')
        self.d(resourceId="com.wujie.siyu:id/car_indicator").click()
        if self.d(text="浪里个浪").exists:
            return True
        else:
            return False

    @teststep
    def check_background(self):
        log.i('检查背景')
        self.d(resourceId="com.wujie.siyu:id/car_indicator").click()
        if self.d(text="型男黑").exists:
            return True
        else:
            return False

    @teststep
    def check_focuson(self):
        log.i('检查关注是否可点击')
        if self.d(resourceId="com.wujie.siyu:id/attention_layout").exists:
            return True
        else:
            return False

    @teststep
    def click_chat(self):
        log.i('检查私聊')
        self.d(resourceId="com.wujie.siyu:id/send_msg_layout").click()

    @teststep
    def click_user(self):
        log.i('点击右上角')
        self.d(resourceId="com.wujie.siyu:id/iv_add_black_list").click()


    @teststep
    def click_jiaruheimingd(self):
        log.i('点击加入黑名单')
        self.d(resourceId="com.wujie.siyu:id/tv_add_black_list").click()
        self.d(resourceId="com.wujie.siyu:id/btn_ok").click()
        sleep(1)
        #self.d(resourceId="com.wujie.siyu:id/tv_add_black_list").get_text()
        log.i('toast信息为%s'%self.d.toast.get_message(1.0, 2.0, "default message"))
        return self.d.toast.get_message(1.0, 2.0, "default message")

    @teststep
    def click_yichuheimingdan(self):
        log.i('移除黑名单')
        sleep(3)
        self.d(resourceId="com.wujie.siyu:id/tv_add_black_list").click()
        self.d(resourceId="com.wujie.siyu:id/btn_ok").click()
        log.i('toast信息为%s' % self.d.toast.get_message(1.0, 2.0, "default message"))
        return self.d.toast.get_message(3.0, 4.0, "default message")

    @teststep
    def click_fans(self):
        log.i('点击粉丝')
        if self.d.xpath('//*[@resource-id="com.wujie.siyu:id/recycler_view"]/android.widget.RelativeLayout[1]').exists:
            return True
        else:
            return False

    @teststep
    def click_home_page(self):
        log.i('点击个人主页')
        self.d(resourceId="com.wujie.siyu:id/iv_user_info_more").click()
        sleep(1)

    @teststep
    def click_edit(self):
        log.i('点击编辑个人资料')
        self.d(resourceId="com.wujie.siyu:id/iv_edit").click()

    @teststep
    def click_edit_nickname(self):
        log.i('点击个人昵称')
        self.d(resourceId="com.wujie.siyu:id/layout_nick").click()
        sleep(1)

    @teststep
    def sendkey_nickname(self, nickname):
        log.i('输入随机昵称%s'% nickname)
        #self.d.xpath('//*[@resource-id="com.wujie.siyu:id/layout_coordinator"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').clear_text()
        #self.d.xpath('//*[@resource-id="com.wujie.siyu:id/layout_coordinator"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]').send_keys(nickname,clear=True)
        self.d.send_keys(nickname, clear=True)
    @teststep
    def click_savenickname(self):
        log.i('点击保存')
        self.d(text="保存").click()
        sleep(1)

    @teststep
    def get_nickname(self):
        log.i('获取用户昵称')
        nickname = self.d(resourceId="com.wujie.siyu:id/layout_nick").get_text()
        log.i('获取用户昵称为%s'% nickname)
        return nickname

    @teststep
    def click_sign(self):
        log.i('点击个性签名')
        self.d.xpath('//*[@resource-id="com.wujie.siyu:id/layout_addinfo"]/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]').click()
        sleep(1)

    @teststep
    def senk_sign(self, sign):
        log.i('输入个性签名')
        self.d.send_keys(sign, clear=True)

    @teststep
    def click_save_sign(self):
        log.i('点击保存个性签名')
        self.d.xpath('//*[@text="保存"]').click()

    def get_random_number(self,list):
        return int(random.uniform(*list))
    """给出集合，从中随机抽取一个"""
    def get_random_list(self, list):
        return random.choice(list)
    """随机选取字母。0：代表大小写字母。-1：代表小写字母。1：代表大写字母"""
    def get_random_letter(self, letter_size=0):
        list_lowercase = []
        list_majuscule = []
        #小写字母集合
        for i in range(65, 91):
            list_lowercase.append(chr(i))
        #大写字母集合
        for i in range(97, 123):
            list_majuscule.append(chr(i))
        #大小写全部字母
        letter = list_lowercase+list_majuscule
        if letter_size == 0:
            return self.get_random_list(letter)
        elif letter_size == -1:
            return self.get_random_list(list_lowercase)
        elif letter_size == -2:
            return self.get_random_list(list_majuscule)
