# -*- coding:utf-8 -*-

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str='UTC+0:00'):
    tz_day = datetime.strptime(dt_str[:18],'%Y-%m-%d %H:%M:%S')
    hours_1 = re.match(r'^UTC(\+?-?\d+):',tz_str)
    tz_utc = tz_day.replace(tzinfo=timezone.utc)
    tz_s = tz_utc.timestamp()
    hours = int(hours_1.group(1))
    t = tz_s - hours * 60 * 60 
    print (t)
    return t



# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1


print('ok')
