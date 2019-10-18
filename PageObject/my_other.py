from Public.Decorator import teststep, log


class my_other_page():

    @teststep
    def click_my(self):
        log.i('点击我的')
        self.d.xpath('//*[@resource-id="com.wujie.siyu:id/main_me_tab"]').click()

    @teststep
    def click_wallet(self):
        log.i('点击钱包')
        self.d(resourceId="com.wujie.siyu:id/me_item_wallet").click()

    @teststep
    def check_bill(self):
        log.i('检查账单元素')
        if self.d(text="账单").exists:
            return True
        else:
            return False

    @teststep
    def check_yue(self):
        log.i('检查余额元素是否存在')
        if self.d(text="我的金币余额").exists and self.d(resourceId="com.wujie.siyu:id/tv_wallet_gold_num").exists:
            return True
        else:
            return False

