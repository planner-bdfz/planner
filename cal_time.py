from dateutil.relativedelta import relativedelta

def cal_time(time, start):
    if start:
        sin_str = str(time - relativedelta(days=7))[0:10]
    else:
        sin_str = str(time + relativedelta(days=7))[0:10]
    res = sin_str[8:10] + "-" + sin_str[5:7] + "-" + sin_str[0:4]
    return res