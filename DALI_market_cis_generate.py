
from icalendar import Calendar, Event
import sxtwl
import datetime
from zoneinfo import ZoneInfo
import uuid

def is_san_yue_jie_market_day(day):
    # 三月街：农历初二/九/十六/二十三 大理三月街
    return day.getLunarDay() in [2, 9, 16, 23]

def get_san_yue_jie_market_information():
    return "三月街", "三月街", "农历初二/九/十六/二十三"

## 生肖相冲方法
SHENG_XIAO = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
DI_ZHI = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

# 地支相冲关系：子午冲、丑未冲、寅申冲、卯酉冲、辰戌冲、巳亥冲
# 这个字典表示每个地支所冲的地支索引（0-11）
CHONG_RELATION = {
    0: 6,   # 子(0) 冲 午(6)
    1: 7,   # 丑(1) 冲 未(7)
    2: 8,   # 寅(2) 冲 申(8)
    3: 9,   # 卯(3) 冲 酉(9)
    4: 10,  # 辰(4) 冲 戌(10)
    5: 11,  # 巳(5) 冲 亥(11)
    6: 0,   # 午(6) 冲 子(0)
    7: 1,   # 未(7) 冲 丑(1)
    8: 2,   # 申(8) 冲 寅(2)
    9: 3,   # 酉(9) 冲 卯(3)
    10: 4,  # 戌(10)冲 辰(4)
    11: 5   # 亥(11)冲 巳(5)
}

def get_chong_shengxiao(day):
    # 获取日柱的地支（索引0-11）
    day_gz = day.getDayGZ()
    day_zhi_index = day_gz.dz
    
    # 通过相冲关系字典，找到所冲的地支索引
    chong_zhi_index = CHONG_RELATION.get(day_zhi_index)
    
    # 根据地支索引获取对应的生肖
    # 因为地支和生肖的顺序是完全对应的（子对鼠，丑对牛...亥对猪）
    # 所以可以直接用这个索引从生肖列表里取
    return chong_zhi_index
    # chong_shengxiao = SHENG_XIAO[chong_zhi_index]
    
    # return chong_shengxiao
##

def is_shuang_lang_jie_market_day(day):
    # 双廊街 冲虎/冲猴 双廊古镇农贸市场
    return get_chong_shengxiao(day) in [2, 8]

def get_shuang_lang_jie_market_information():
    return "双廊街", "大理双廊古镇农贸市场", "农历冲虎/冲猴"

def is_gu_cheng_bei_men_market_day(day):
    # 古城北门市场
    return True

def get_gu_cheng_bei_men_market_information():
    return "古城北门市场", "大理古城北门菜市场", "每天"

def is_xi_zhou_jie_market_day(day):
    # 喜洲街 周六周日早上10点到12点
    return day.getWeek() in [0, 6]

def get_xi_zhou_jie_market_information():
    return "喜洲街", "大理喜洲古镇", "周六周日早上10点到12点"

def is_yin_qiao_jie_market_day(day):
    # 银桥街 农历初五/十三/二十/二十八
    return day.getLunarDay() in [5, 13, 20, 28]

def get_yin_qiao_jie_market_information():
    return "银桥街", "大理银桥镇农贸市场", "农历初五/十三/二十/二十八"

def is_long_jie_market_day(day):
    # 龙街 农历初二/九/十六/二十三
    return day.getLunarDay() in [2, 9, 16, 23]

def get_long_jie_market_information():
    return "龙街", "大理喜洲作邑村", "农历初二/九/十六/二十三"

def is_wan_qiao_jie_market_day(day):
    # 湾桥街 农历初四/十一/十八/二十五
    return day.getLunarDay() in [4, 11, 18, 25]

def get_wan_qiao_jie_market_information():
    return "湾桥街", "大理湾桥镇农贸市场", "农历初四/十一/十八/二十五"

def is_wa_se_jie_market_day(day):
    # 挖色街  公历每月5/10/15/20/25/30
    return day.getSolarDay() in [5, 10, 15, 20, 25, 30]

def get_wa_se_jie_market_information():
    return "挖色街", "大理挖色农贸市场", "公历每月5/10/15/20/25/30"

def is_hai_dong_jie_market_day(day):
    # 海东街 农历初一/八/十五/二十一/二十六
    return day.getLunarDay() in [1, 8, 15, 21, 26]

def get_hai_dong_jie_market_information():
    return "海东街", "大理海东镇向阳街", "农历初一/八/十五/二十一/二十六"

def is_feng_yi_jie_market_day(day):
    # 凤仪街 公历每月5/10/15/20/25/30
    return day.getSolarDay() in [5, 10, 15, 20, 25, 30]

def get_feng_yi_jie_market_information():
    return "凤仪街", "大理凤仪镇凤中街", "公历每月5/10/15/20/25/30"

def is_xia_guan_market_day(day):
    # 下关集市 周日
    return day.getWeek() == 0

def get_xia_guan_market_information():
    return "下关集市", "大理下关美登桥新桥农贸市场", "周日"

def is_tai_xing_market_day(day):
    # 泰兴市场 每天
    return True

def get_tai_xing_market_information():
    return "泰兴市场", "大理泰兴市场", "每天"

def is_wei_shan_jie_market_day(day):
    # 巍山街 公历 5,10
    return day.getSolarDay() in [5, 10]

def get_wei_shan_jie_market_information():
    return "巍山街", "大理巍山县城", "公历每月5/10"

def is_sha_xi_gu_zhen_market_day(day):
    # 沙溪古 每周五上午8:00-12:00
    return day.getWeek() == 5

def get_sha_xi_gu_zhen_market_information():
    return "沙溪古镇", "大理沙溪古镇", "每周五上午8:00-12:00"

def is_gu_cheng_chuang_dan_chang_market_day(day):
    # 古城床单厂 每周六日
    return day.getWeek() in [0, 6]

def get_gu_cheng_chuang_dan_chang_market_information():
    return "古城床单厂", "大理古城床单厂", "每周六日"

def is_cang_shan_zhi_wu_yuan_market_day(day):
    # 苍山植物园集市 每周日10:00-22:00
    return day.getWeek() == 0

def get_cang_shan_zhi_wu_yuan_market_information():
    return "苍山植物园集市", "大理苍山植物园", "每周日10:00-22:00"

def is_xiao_yuan_zi_market_day(day):
    # 小院子集市 每周六日11:00-22:00
    return day.getWeek() in [0, 6]

def get_xiao_yuan_zi_market_information():
    return "小院子集市", "大理古城小院子中区", "每周六日11:00-22:00"

def is_lv_yu_market_day(day):
    # 绿玉农贸市场 每天下午
    return True

def get_lv_yu_market_information():
    return "绿玉农贸市场", "大理古城南门", "每天下午"

def is_xi_zhou_market_day(day):
    # 喜洲菜市场 每天下午
    return True

def get_xi_zhou_market_information():
    return "喜洲菜市场", "大理喜洲古镇", "每天下午"

def is_da_guan_yi_market_day(day):
    # 大关邑综合农贸市场 每天上午
    return True

def get_da_guan_yi_market_information():
    return "大关邑综合农贸市场", "大理下关兴盛北路", "每天上午"

def is_guan_yin_tang_market_day(day):
    # 观音塘菜市场 每天
    return True

def get_guan_yin_tang_market_information():
    return "观音堂菜市场", "大理观音塘菜市场", "每天"

def is_yi_hao_qiao_market_day(day):
    # 一号桥农贸市场 每天
    return True

def get_yi_hao_qiao_market_information():
    return "一号桥农贸市场", "大理一号桥农贸市场", "每天"

def is_tai_yi_xiang_market_day(day):
    # 泰义乡市场 周四
    return day.getWeek() == 4

def get_tai_yi_xiang_market_information():
    return "太邑乡农贸市场", "大理太邑乡太邑街", "周四"

def generate_market_events(start_year, end_year):
    
    cal = Calendar()
    cal.add('prodid', '-//Chinese Almanac//CN')
    cal.add('version', '2.0')
    
    sx = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
    dz = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    
    current_solar_date = datetime.date(start_year, 1, 1)
    end_solar_date = datetime.date(end_year, 12, 31)
    delta = datetime.timedelta(days=1)
    china_time_zone = ZoneInfo('Asia/Shanghai')

    while current_solar_date <= end_solar_date:
        day = sxtwl.fromSolar(current_solar_date.year, current_solar_date.month, current_solar_date.day)
        if is_san_yue_jie_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_san_yue_jie_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_shuang_lang_jie_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_shuang_lang_jie_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        

        if is_xi_zhou_jie_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            start_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 10, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            end_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 12, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            event.add('dtstart', start_time)
            event.add('dtend', end_time)
            summary, location, description = get_xi_zhou_jie_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_yin_qiao_jie_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_yin_qiao_jie_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_long_jie_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_long_jie_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_wan_qiao_jie_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_wan_qiao_jie_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_wa_se_jie_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_wa_se_jie_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)
        
        if is_hai_dong_jie_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_hai_dong_jie_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_feng_yi_jie_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_feng_yi_jie_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_xia_guan_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_xia_guan_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        

        if is_wei_shan_jie_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_wei_shan_jie_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_sha_xi_gu_zhen_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            start_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 8, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            end_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 12, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            event.add('dtstart', start_time)
            event.add('dtend', end_time)
            summary, location, description = get_sha_xi_gu_zhen_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_gu_cheng_chuang_dan_chang_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_gu_cheng_chuang_dan_chang_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_cang_shan_zhi_wu_yuan_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            start_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 10, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            end_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 22, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            event.add('dtstart', start_time)
            event.add('dtend', end_time)
            summary, location, description = get_cang_shan_zhi_wu_yuan_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_xiao_yuan_zi_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            start_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 11, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            end_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 22, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            event.add('dtstart', start_time)
            event.add('dtend', end_time)
            summary, location, description = get_xiao_yuan_zi_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        

        if is_tai_yi_xiang_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_tai_yi_xiang_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_gu_cheng_bei_men_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_gu_cheng_bei_men_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_tai_xing_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_tai_xing_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_lv_yu_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            start_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 13, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            end_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 18, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            event.add('dtstart', start_time)
            event.add('dtend', end_time)
            summary, location, description = get_lv_yu_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_xi_zhou_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            start_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 8, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            end_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 12, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            event.add('dtstart', start_time)
            event.add('dtend', end_time)
            summary, location, description = get_xi_zhou_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_da_guan_yi_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            start_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 8, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            end_time = datetime.datetime(current_solar_date.year, current_solar_date.month, current_solar_date.day, 12, 0, 0, tzinfo=ZoneInfo("Asia/Shanghai"))
            event.add('dtstart', start_time)
            event.add('dtend', end_time)
            summary, location, description = get_da_guan_yi_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_guan_yin_tang_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_guan_yin_tang_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)

        if is_yi_hao_qiao_market_day(day):
            event = Event()
            event.add('uid', f'{str(uuid.uuid4())}@老干部')
            event.add('dtstamp', datetime.datetime.now())
            event.add('dtstart', current_solar_date)
            event.add('dtend', current_solar_date + delta)
            summary, location, description = get_yi_hao_qiao_market_information()
            event.add('summary', summary)
            event.add('location', location)
            event.add('description', description)
            cal.add_component(event)


        current_solar_date += delta
    
    return cal

calendar = generate_market_events(2025, 2025)
with open('大理集市日历.ics', 'wb') as f:
    f.write(calendar.to_ical())
print("Dali market calendar generated successfully.")