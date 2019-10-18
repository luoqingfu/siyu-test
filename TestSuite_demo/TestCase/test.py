from Public.ReadConfig import ReadConfig


class testT(ReadConfig):
    def test(self):
        se = self.get_testdata('user_name')
        print(se[0])


if __name__ == '__main__':
    testT().test()
