"""
    准备数据  模拟请求下发  处理响应结果
"""

import requests

# 支持城市清单查询

url = 'http://apis.juhe.cn/springTravel/citys'
data = {"key": "string"}

response = requests.get(url=url, json=data)

result = response.json()
print(result)

# 取值测试
print(result['reason'])   # success
print(result['result'])
# [{'province_id': '1', 'province': '安徽', 'citys': [{'city_id': '10001', 'city': '合肥'}]},
# {'province_id': '2', 'province': '北京', 'citys': [{'city_id': '10017', 'city': '北京'}]}]
print(result['result'][0]['province'])   # 安徽
print(result['result'][0]['citys'][0]['city'])  # 合肥

# 普通判断
expect_msg = "success!"
result_msg = result['reason']

if expect_msg == result['reason']:
    print('用例成功')
else:
    print('用例失败')

# 断言判断

assert expect_msg == result['reason'], '断言失败'


# 返回结果示例
"""
    {
    "reason": "success!",
    "result": [
        {
            "province_id": "1",
            "province": "安徽",
            "citys": [
                {
                    "city_id": "10001",
                    "city": "合肥"
                },
                {
                    "city_id": "10002",
                    "city": "芜湖"
                },
                {
                    "city_id": "10003",
                    "city": "蚌埠"
                },
                {
                    "city_id": "10004",
                    "city": "淮南"
                },
                {
                    "city_id": "10005",
                    "city": "马鞍山"
                },
                {
                    "city_id": "10006",
                    "city": "淮北"
                },
                {
                    "city_id": "10007",
                    "city": "铜陵"
                },
                {
                    "city_id": "10008",
                    "city": "安庆"
                },
                {
                    "city_id": "10009",
                    "city": "黄山"
                },
                {
                    "city_id": "10010",
                    "city": "滁州"
                },
                {
                    "city_id": "10011",
                    "city": "阜阳"
                },
                {
                    "city_id": "10012",
                    "city": "宿州"
                },
                {
                    "city_id": "10013",
                    "city": "六安"
                },
                {
                    "city_id": "10014",
                    "city": "亳州"
                },
                {
                    "city_id": "10015",
                    "city": "池州"
                },
                {
                    "city_id": "10016",
                    "city": "宣城"
                }
            ]
        },
        {
            "province_id": "2",
            "province": "北京",
            "citys": [
                {
                    "city_id": "10017",
                    "city": "北京"
                }
            ]
        },
        {
            "province_id": "3",
            "province": "重庆",
            "citys": [
                {
                    "city_id": "10018",
                    "city": "重庆"
                }
            ]
        }
    ],
    "error_code": 0
}
"""