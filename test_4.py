# 查询风险疫情地区

import requests

url = 'http://apis.juhe.cn/springTravel/risk'
data = {"key": "string"}

response = requests.get(url=url, json=data)

result = response.json()
print(result)

print(result['reason'])   # success
print(result['result']['high_count'])  # 9
print(result['result']['middle_count'])  # 83
print(result['result']['high_list'][0]['area_name'])  # "北京市 大兴区 天宫院街道"

# 打出所有高风险地区名字
max_num = len(result['result']['high_list'])
for i in range(0, max_num):
    print(result['result']['high_list'][i]['area_name'])


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
        "updated_date": "2021-01-28 15:00:00",
        "high_count": "9",
        "middle_count": "83",
        "high_list": [
            {
                "type": "2",
                "province": "北京市",
                "city": "大兴区",
                "county": "天宫院街道",
                "area_name": "北京市 大兴区 天宫院街道",
                "communitys": [
                    "融汇社区"
                ],
                "county_code": "110115010"
            },
            {
                "type": "1",
                "province": "河北省",
                "city": "石家庄市",
                "county": "藁城区",
                "area_name": "河北省 石家庄市 藁城区",
                "communitys": null,
                "county_code": "130109"
            },
            {
                "type": "1",
                "province": "河北省",
                "city": "石家庄市",
                "county": "新乐市",
                "area_name": "河北省 石家庄市 新乐市",
                "communitys": null,
                "county_code": "130184"
            },
            {
                "type": "1",
                "province": "河北省",
                "city": "邢台市",
                "county": "南宫市",
                "area_name": "河北省 邢台市 南宫市",
                "communitys": null,
                "county_code": "130581"
            },
            {
                "type": "1",
                "province": "吉林省",
                "city": "通化市",
                "county": "东昌区",
                "area_name": "吉林省 通化市 东昌区",
                "communitys": null,
                "county_code": "220502"
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "哈尔滨市",
                "county": "利民开发区",
                "area_name": "黑龙江省 哈尔滨市 利民开发区",
                "communitys": [
                    "裕田街道"
                ],
                "county_code": null
            },
            {
                "type": "1",
                "province": "黑龙江省",
                "city": "绥化市",
                "county": "望奎县",
                "area_name": "黑龙江省 绥化市 望奎县",
                "communitys": null,
                "county_code": "231221"
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "绥化市",
                "county": "海伦市",
                "area_name": "黑龙江省 绥化市 海伦市",
                "communitys": [
                    "永富镇东大村",
                    "永富镇众发村"
                ],
                "county_code": "231283"
            }
        ],
        "middle_list": [
            {
                "type": "2",
                "province": "北京市",
                "city": "顺义区",
                "county": "赵全营镇",
                "area_name": "北京市 顺义区 赵全营镇",
                "communitys": [
                    "联庄村"
                ],
                "county_code": "110113116"
            },
            {
                "type": "2",
                "province": "北京市",
                "city": "顺义区",
                "county": "北石槽镇",
                "area_name": "北京市 顺义区 北石槽镇",
                "communitys": [
                    "北石槽村"
                ],
                "county_code": "110113115"
            },
            {
                "type": "2",
                "province": "河北省",
                "city": "石家庄市",
                "county": "长安区",
                "area_name": "河北省 石家庄市 长安区",
                "communitys": [
                    "简筑家园小区",
                    "前进村",
                    "普和小区南院",
                    "建明小区",
                    "保利花园D区",
                    "河北省胸科医院公寓北区"
                ],
                "county_code": "130102"
            },
            {
                "type": "2",
                "province": "河北省",
                "city": "石家庄市",
                "county": "高新区",
                "area_name": "河北省 石家庄市 高新区",
                "communitys": [
                    "赵村新区小区",
                    "同祥城小区C区",
                    "和合美家小区"
                ],
                "county_code": null
            },
            {
                "type": "2",
                "province": "河北省",
                "city": "石家庄市",
                "county": "裕华区",
                "area_name": "河北省 石家庄市 裕华区",
                "communitys": [
                    "晶彩苑小区",
                    "东方明珠小区",
                    "卓东小区",
                    "十二化建小区16、17号楼",
                    "河北城建学校家属院",
                    "海天阳光园小区"
                ],
                "county_code": "130108"
            },
            {
                "type": "2",
                "province": "河北省",
                "city": "石家庄市",
                "county": "栾城区",
                "area_name": "河北省 石家庄市 栾城区",
                "communitys": [
                    "卓达太阳城希望之洲小区"
                ],
                "county_code": "130111"
            },
            {
                "type": "2",
                "province": "河北省",
                "city": "石家庄市",
                "county": "正定县",
                "area_name": "河北省 石家庄市 正定县",
                "communitys": [
                    "冯家庄村",
                    "东平乐村"
                ],
                "county_code": "130123"
            },
            {
                "type": "2",
                "province": "河北省",
                "city": "石家庄市",
                "county": "平山县",
                "area_name": "河北省 石家庄市 平山县",
                "communitys": [
                    "防疫站小区",
                    "访驾庄村"
                ],
                "county_code": "130131"
            },
            {
                "type": "2",
                "province": "河北省",
                "city": "石家庄市",
                "county": "赵县",
                "area_name": "河北省 石家庄市 赵县",
                "communitys": [
                    "任庄村"
                ],
                "county_code": "130133"
            },
            {
                "type": "2",
                "province": "河北省",
                "city": "邢台市",
                "county": "隆尧县",
                "area_name": "河北省 邢台市 隆尧县",
                "communitys": [
                    "烟草家园（烟草公司家属院）"
                ],
                "county_code": "130525"
            },
            {
                "type": "2",
                "province": "河北省",
                "city": "保定市",
                "county": "定州市",
                "area_name": "河北省 保定市 定州市",
                "communitys": [
                    "西城区庞白土新民居北区"
                ],
                "county_code": "130682"
            },
            {
                "type": "2",
                "province": "河北省",
                "city": "廊坊市",
                "county": "固安县",
                "area_name": "河北省 廊坊市 固安县",
                "communitys": [
                    "英国宫5期"
                ],
                "county_code": "131022"
            },
            {
                "type": "2",
                "province": "吉林省",
                "city": "长春市",
                "county": "公主岭市",
                "area_name": "吉林省 长春市 公主岭市",
                "communitys": [
                    "范家屯镇全域"
                ],
                "county_code": "220184"
            },
            {
                "type": "2",
                "province": "吉林省",
                "city": "通化市",
                "county": "医药高新区",
                "area_name": "吉林省 通化市 医药高新区",
                "communitys": [
                    "奕达小区"
                ],
                "county_code": null
            },
            {
                "type": "2",
                "province": "吉林省",
                "city": "松原市",
                "county": "宁江区",
                "area_name": "吉林省 松原市 宁江区",
                "communitys": [
                    "善友镇新屯村"
                ],
                "county_code": "220702"
            },
            {
                "type": "2",
                "province": "吉林省",
                "city": "松原市",
                "county": "经济技术开发区",
                "area_name": "吉林省 松原市 经济技术开发区",
                "communitys": [
                    "新农小区7号楼"
                ],
                "county_code": null
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "哈尔滨市",
                "county": "道里区",
                "area_name": "黑龙江省 哈尔滨市 道里区",
                "communitys": [
                    "工农街道",
                    "建国街道"
                ],
                "county_code": "230102"
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "哈尔滨市",
                "county": "道外区",
                "area_name": "黑龙江省 哈尔滨市 道外区",
                "communitys": [
                    "巨源镇",
                    "新一街道"
                ],
                "county_code": "230104"
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "哈尔滨市",
                "county": "香坊区",
                "area_name": "黑龙江省 哈尔滨市 香坊区",
                "communitys": [
                    "香坊大街街道办事处香中社区古香街12号",
                    "大庆路街道办事处电塔小区101栋7单元",
                    "和平路街道办事处风华社区石化小区9栋6单元",
                    "上东社区万象上东小区E栋2单元",
                    "新成街道"
                ],
                "county_code": "230110"
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "哈尔滨市",
                "county": "呼兰区",
                "area_name": "黑龙江省 哈尔滨市 呼兰区",
                "communitys": [
                    "兰河街道",
                    "呼兰街道",
                    "公园路街道",
                    "腰堡街道",
                    "建设路街道",
                    "康金街道",
                    "萧乡街道",
                    "长岭街道",
                    "孟家乡"
                ],
                "county_code": "230111"
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "哈尔滨市",
                "county": "利民开发区",
                "area_name": "黑龙江省 哈尔滨市 利民开发区",
                "communitys": [
                    "利民街道",
                    "裕强街道",
                    "南京路街道",
                    "利业街道",
                    "对青山镇",
                    "乐业镇"
                ],
                "county_code": null
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "齐齐哈尔市",
                "county": "昂昂溪区",
                "area_name": "黑龙江省 齐齐哈尔市 昂昂溪区",
                "communitys": [
                    "大五福玛村"
                ],
                "county_code": "230205"
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "大庆市",
                "county": "龙凤区",
                "area_name": "黑龙江省 大庆市 龙凤区",
                "communitys": [
                    "世纪唐人中心小区2栋1单元"
                ],
                "county_code": "230603"
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "绥化市",
                "county": "北林区",
                "area_name": "黑龙江省 绥化市 北林区",
                "communitys": [
                    "气象小区一期",
                    "客运站家属楼",
                    "盛世华庭公寓",
                    "世纪方舟四期",
                    "博学公寓",
                    "园丁1区",
                    "农机局家属楼",
                    "世福汇"
                ],
                "county_code": "231202"
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "绥化市",
                "county": "安达市",
                "area_name": "黑龙江省 绥化市 安达市",
                "communitys": [
                    "新兴街道圣世家园小区",
                    "铁西街道淮阳人家小区",
                    "安虹街道金税小区",
                    "安虹街道民政高层小区",
                    "安虹街道审计局家属楼小区",
                    "东城街道润达学府苑小区",
                    "东城街道华庭二期小区",
                    "东城街道工商银行家属楼小区（含工商银行办公区）"
                ],
                "county_code": "231281"
            },
            {
                "type": "2",
                "province": "黑龙江省",
                "city": "绥化市",
                "county": "海伦市",
                "area_name": "黑龙江省 绥化市 海伦市",
                "communitys": [
                    "永富镇思源村",
                    "永富镇同发村",
                    "丰山乡丰庆村",
                    "丰山乡丰山村",
                    "丰山乡丰荣村",
                    "福民乡永兴村",
                    "伦河镇锦秀嘉园小区"
                ],
                "county_code": "231283"
            },
            {
                "type": "2",
                "province": "上海市",
                "city": "上海市",
                "county": "黄浦区",
                "area_name": "上海市 上海市 黄浦区",
                "communitys": [
                    "昭通路居民区（福州路以南区域）",
                    "中福世福汇大酒店",
                    "贵西小区"
                ],
                "county_code": "310101"
            },
            {
                "type": "2",
                "province": "上海市",
                "city": "上海市",
                "county": "宝山区",
                "area_name": "上海市 上海市 宝山区",
                "communitys": [
                    "友谊路街道临江新村（一、二村）小区"
                ],
                "county_code": "310113"
            }
        ]
    },
    "error_code": 0
}
"""