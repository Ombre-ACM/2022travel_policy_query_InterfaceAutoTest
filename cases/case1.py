import unittest

from ddt import ddt, file_data, data, unpack

from request_key.keys import Key


@ddt
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.key = Key()
        cls.url = 'http://apis.juhe.cn/springTravel'

    # 支持城市清单查询
    def test_01(self):
        url = self.url + '/cities'
        data = {"key": "string"}
        response = self.key.do_get(url=url, json=data)
        result = response.json()
        print(result)

        expect_msg = "success!"
        result_msg = result['reason']

        self.assertEqual(expect_msg, result_msg, '断言失败')

    # 查询出行防疫政策
    @file_data('../data/02.yaml')
    def test_02(self):
        url = self.url + '/query'
        response = self.key.do_post(url=url, json=data)
        result = response.json()
        print(result)

        print(result['result']['from_info']['risk_level'])
        print(result['result']['from_info']['out_desc'])

        print(result['result']['to_info']['risk_level'])
        print(result['result']['to_info']['high_in_desc'])
        print(result['result']['to_info']['low_in_desc'])

        expect_msg = "success!"
        result_msg = result['reason']

        self.assertEqual(expect_msg, result_msg, '断言失败')

    # 查询核酸检测机构
    @file_data('../data/03.yaml')
    def test_03(self):
        url = self.url + '/hsjg'
        response = self.key.do_post(url=url, json=data)
        result = response.json()
        print(result)

        print(result['reason'])
        print(result['result'][data][0])

        expect_msg = "success!"
        result_msg = result['reason']

        self.assertEqual(expect_msg, result_msg, '断言失败')

    # 查询风险疫情地区
    def test_04(self):
        url = self.url + '/risk'
        data = {"key": "string"}
        response = self.key.do_post(url=url, json=data)
        result = response.json()
        print(result)

        print(result['reason'])
        print(result['result']['high_count'])
        print(result['result']['middle_count'])
        print(result['result']['high_list'][0]['area_name'])

        # 打出所有高风险地区名字
        max_num = len(result['result']['high_list'])
        for i in range(0, max_num):
            print(result['result']['high_list'][i]['area_name'])

        max_num2 = len(result['result']['middle_list'])
        for i in range(0, max_num2):
            print(result['result']['middle_list'][i]['area_name'])

        expect_msg = "success!"
        result_msg = result['reason']

        self.assertEqual(expect_msg, result_msg, '断言失败')

        
if __name__ == '__main__':
    unittest.main()

