# 查询出行防疫政策
import requests

url = 'http://apis.juhe.cn/springTravel/query'
data = {"key": "string",
        "from": "10191",   # 出发城市 id  苏州
        "to": "10349"     # 到达城市 id  温州
        }

response = requests.post(url=url, json=data)

result = response.json()
print(result)

print(result['reason'])   # success
print(result['result']['from_info']['risk_level'])  # 1
print(result['result']['from_info']['out_desc'])
# "出苏无需核酸阴性证明，原则上非必要不出省，不得前往中高风险区及其所在的设区市。"

print(result['result']['to_info']['risk_level'])  # 1
print(result['result']['to_info']['high_in_desc'])
# "1.疫情高风险地区，经综合评估，可对其所在城市来浙返浙人员实行“7+7”健康管理措施，
# 即先实施7天居家健康观察，第1天和第7天分别进行一次核酸检测；对居家健康观察期满核酸检测阴性者，
# 继续实施7天日常健康监测，期满再进行一次核酸检测。
# 2.疫情中风险地区，所在街道或县（市、区）来浙返浙人员，一律核验3天内核酸检测阴性证明；
# 对无法提供相关证明的，立即引导到指定场所接受核酸检测；
# 对结果为阴性者实施7天日常健康监测，期满进行一次核酸检测。
# 3.入境人员需14天集中隔离+7天居家健康观察+7天健康监测。"
print(result['result']['to_info']['low_in_desc'])
# "低风险地区进温州无需持核酸阴性证明及隔离，需持健康码绿码。"

# 普通判断
expect_msg = "success!"
result_msg = result['reason']

if expect_msg == result['reason']:
    print('用例成功')
else:
    print('用例失败')

# 断言判断

assert expect_msg == result['reason'], '断言失败'


"""
{
    "reason": "success!",
    "result": {
        "from_info": {
            "province_id": "16",
            "city_id": "10191",
            "city_name": "苏州",
            "health_code_desc": "支付宝扫一扫，进入小程序",
            "health_code_gid": "https://www.sdk.cn/details/jgRaEkelBp7R85ZmYq",
            "health_code_name": "苏康码\r\r\n",
            "health_code_picture": "https://cdn.juhekeji.com/spring_travel/e681692d49d50d8eb9d2bade122a8654.png",
            "health_code_style": "1",
            "high_in_desc": "1.中高风险地区人员须持7日内核酸检测阴性证明，第一时间主动报备，配合做好信息登记、核酸检测、集中隔离医学观察等防控工作。\n2.根据江苏省要求：对有中高风险地区所在设区市（直辖市为区）旅居史的来苏返苏人员，持有7日内核酸检测阴性证明（或能出示包括7日内核酸检测阴性证明的健康码），可以自由有序流动；对不能提供7日内核酸检测阴性证明的人员，要进行核酸检测，其所在社区应加强健康管理。",
            "low_in_desc": "3.低风险地区人员进苏州无需持核酸阴性证明及隔离，需持健康码绿码。",
            "out_desc": "出苏无需核酸阴性证明，原则上非必要不出省，不得前往中高风险区及其所在的设区市。",
            "province_name": "江苏",
            "risk_level": "1"
        },
        "to_info": {
            "province_id": "31",
            "city_id": "10349",
            "city_name": "温州",
            "health_code_desc": "支付宝扫一扫，进入小程序",
            "health_code_gid": "https://www.sdk.cn/details/vjxQ9bLPEp70bqnKOZ",
            "health_code_name": "浙江健康码",
            "health_code_picture": "https://cdn.juhekeji.com/spring_travel/ad9ef3f794107b400aed52e0e721b578.png",
            "health_code_style": "1",
            "high_in_desc": "1.疫情高风险地区，经综合评估，可对其所在城市来浙返浙人员实行“7+7”健康管理措施，即先实施7天居家健康观察，第1天和第7天分别进行一次核酸检测；对居家健康观察期满核酸检测阴性者，继续实施7天日常健康监测，期满再进行一次核酸检测。\n2.疫情中风险地区，所在街道或县（市、区）来浙返浙人员，一律核验3天内核酸检测阴性证明；对无法提供相关证明的，立即引导到指定场所接受核酸检测；对结果为阴性者实施7天日常健康监测，期满进行一次核酸检测。\n3.入境人员需14天集中隔离+7天居家健康观察+7天健康监测。",
            "low_in_desc": "低风险地区进温州无需持核酸阴性证明及隔离，需持健康码绿码。",
            "out_desc": "出行无需核酸阴性证明，非必要避免前往中高风险地区。",
            "province_name": "浙江",
            "risk_level": "1"
        },
        "from_covid_info": {
            "city_id": "10191",
            "city_name": "苏州",
            "today_confirm": "0",
            "total_confirm": "87",
            "total_heal": "87",
            "total_dead": "0",
            "updated_at": "2021-01-20 10:07:33",
            "is_updated": "0"
        },
        "to_covid_info": {
            "city_id": "10349",
            "city_name": "温州",
            "today_confirm": "0",
            "total_confirm": "504",
            "total_heal": "503",
            "total_dead": "1",
            "updated_at": "2021-01-20 10:07:33",
            "is_updated": "0"
        },
        "tc_tag": "1",
        "fc_tag": "1",
        "t_tag": "1",
        "f_tag": "1"
    },
    "error_code": 0
}
"""