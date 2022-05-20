# 查询核酸检测机构
import requests

url = 'http://apis.juhe.cn/springTravel/hsjg'
data = {"key": "string",
        "city_id": "10191"}

response = requests.post(url=url, json=data)

result = response.json()
print(result)

print(result['reason'])   # success
print(result['result'][data][0])
#  {
#                 "city_id": "10191",
#                 "name": "张家港市第一人民医院",
#                 "province": "江苏",
#                 "city": "苏州",
#                 "phone": "0512-56919560",
#                 "address": "江苏省苏州市张家港市暨阳西路68号"
#             }

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
        "data": [
            {
                "city_id": "10191",
                "name": "张家港市第一人民医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-56919560",
                "address": "江苏省苏州市张家港市暨阳西路68号"
            },
            {
                "city_id": "10191",
                "name": "张家港市疾病预防控制中心",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-58234356",
                "address": "江苏省苏州市张家港市"
            },
            {
                "city_id": "10191",
                "name": "张家港市中医医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-56380976",
                "address": "江苏省苏州张家港市康乐路4号"
            },
            {
                "city_id": "10191",
                "name": "昆山迪安医学检验实验室有限公司",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-86166555",
                "address": "江苏省苏州市昆山市花桥镇金洋路15号金融园15号"
            },
            {
                "city_id": "10191",
                "name": "昆山市第一人民医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-55233057",
                "address": "江苏省苏州市昆山市前进西路91号"
            },
            {
                "city_id": "10191",
                "name": "昆山市疾病预防控制中心",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-57370701",
                "address": "江苏省苏州市昆山市同丰西路458号"
            },
            {
                "city_id": "10191",
                "name": "昆山市中医医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-57310000",
                "address": "江苏省苏州市昆山市玉山镇朝阳西路189号"
            },
            {
                "city_id": "10191",
                "name": "苏州大学附属第二医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "18962113358",
                "address": "江苏省苏州市姑苏区三香路1055号"
            },
            {
                "city_id": "10191",
                "name": "苏州大学附属第一医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "13606136542",
                "address": "江苏省苏州市姑苏区十梓街188号"
            },
            {
                "city_id": "10191",
                "name": "苏州大学附属儿童医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-80691235",
                "address": "江苏省苏州市工业园区钟南街92号"
            },
            {
                "city_id": "10191",
                "name": "苏州高新区人民医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-69585026",
                "address": "江苏省苏州高新区华山路95号"
            },
            {
                "city_id": "10191",
                "name": "苏州工业园区疾病防治中心",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-67614200",
                "address": "江苏省苏州市工业园区苏虹西路200号"
            },
            {
                "city_id": "10191",
                "name": "苏州明基医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-80838800",
                "address": "江苏省苏州市虎丘区竹园路181号"
            },
            {
                "city_id": "10191",
                "name": "苏州珀金埃尔默医学检验所有限公司",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-53378788",
                "address": "江苏省苏州市太仓市太平北路115号"
            },
            {
                "city_id": "10191",
                "name": "苏州市第九人民医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-82881138",
                "address": "江苏省苏州市吴江区太湖新城芦荡路2666号"
            },
            {
                "city_id": "10191",
                "name": "苏州市第五人民医院检验中心",
                "province": "江苏",
                "city": "苏州",
                "phone": "13013807540",
                "address": "江苏省苏州市相城区广前路10号"
            },
            {
                "city_id": "10191",
                "name": "苏州市独墅湖医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-67505206",
                "address": "江苏省苏州市工业园区崇文路9号"
            },
            {
                "city_id": "10191",
                "name": "苏州市疾病预防控制中心",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-68261772",
                "address": "江苏省苏州市姑苏区三香路72号"
            },
            {
                "city_id": "10191",
                "name": "苏州市立医院医学检验科（南区）",
                "province": "江苏",
                "city": "苏州",
                "phone": "15950093311",
                "address": "江苏省苏州市吴中区枫津路40号"
            },
            {
                "city_id": "10191",
                "name": "苏州市吴江区疾病预防控制中心",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-63160221",
                "address": "江苏省苏州市吴江区高新路551号"
            },
            {
                "city_id": "10191",
                "name": "苏州市吴江区中医医院（苏州市吴江区第二人民医院）",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-63655930",
                "address": "江苏省苏州市吴江区平望镇通运路73号"
            },
            {
                "city_id": "10191",
                "name": "苏州市吴中区疾病预防控制中心",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-65620235",
                "address": "苏省苏州市吴中区太湖西路269号1楼"
            },
            {
                "city_id": "10191",
                "name": "苏州市相城区疾病预防控制中心",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-66181776",
                "address": "江苏省苏州市相城区"
            },
            {
                "city_id": "10191",
                "name": "苏州相城人民医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-69571800",
                "address": "江苏省苏州市相城区"
            },
            {
                "city_id": "10191",
                "name": "太仓市第一人民医院",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-53101356",
                "address": "江苏省苏州市太仓市常胜南路58号"
            },
            {
                "city_id": "10191",
                "name": "常熟市医学检验所",
                "province": "江苏",
                "city": "苏州",
                "phone": "0512-52901521",
                "address": "江苏省苏州市常熟市青墩塘路36号"
            }
        ]
    },
    "error_code": 0
}
"""