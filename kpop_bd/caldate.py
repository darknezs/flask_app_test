import datetime
def nextBd(datas):
    # now = datetime.datetime.now()
    now = datetime.datetime(2024, 1,1)
    now_m = now.strftime("%m")
    now_d = now.strftime("%d")

    for i in range(len(datas)):
        datas[i]['birthday'] = str(datas[i]['birthday']).replace(str(datas[i]['birthday'])[:4],str(int(str(datas[i]['birthday'])[:4])-543))


    sorted_data = sorted(datas, key=lambda x: datetime.datetime.strptime(x['birthday'], '%Y-%m-%d %H:%M:%S').strftime('%m-%d'))
    # print(sorted_data)
    next_bd_list = []
    today_bd_list = []
    for data in sorted_data:
        format = '%Y-%m-%d'
        datetime_str = datetime.datetime.strptime(data['birthday'][:-9], format)
        if (int(now_m) == int(datetime_str.strftime("%m"))) and int(now_d) == int(datetime_str.strftime("%d")):
            print("today_bd ==> ", data) #today_bd
            today_bd_list.append(data)
            print(today_bd_list)
            return today_bd_list
        elif (int(now_m) < int(datetime_str.strftime("%m"))) or (int(now_m) == int(datetime_str.strftime("%m")) and (int(now_d) < int(datetime_str.strftime("%d")))):
            print("elif next_bd == >", data)
            next_bd_list.append(data)
            if len(next_bd_list) == 2:
                return next_bd_list
    if len(next_bd_list) == 0:
        next_bd_list = sorted_data[0:3]
        print("next_bd == >", next_bd_list)
        print(next_bd_list)
        return next_bd_list
'''
if m=m and d=d //
    > today_bd//
else if (m.now() < m) or ((m.now() == m) and (d.now < d))
'''








# z = datetime.datetime(1997, 1, 17)
# r = datetime.datetime(2006, 3, 17)
# y = datetime.datetime(2020, 8, 17)
# p = datetime.datetime(2006, 12, 1)
# q = datetime.datetime(2006, 12, 3)

# arr = [now,y,z,r,p,q]

# thai_months = {
#     'มกราคม': 'January', 'กุมภาพันธ์': 'February', 'มีนาคม': 'March',
#     'เมษายน': 'April', 'พฤษภาคม': 'May', 'มิถุนายน': 'June',
#     'กรกฎาคม': 'July', 'สิงหาคม': 'August', 'กันยายน': 'September',
#     'ตุลาคม': 'October', 'พฤศจิกายน': 'November', 'ธันวาคม': 'December'
# }

# arr.sort(key = lambda d: (d.month, d.day))
# now = datetime.datetime.now()
# data = [{'name':'lia','y':'2000','m':'5','d':'5'},
#         {'name':'zzz','y':'2010','m':'12','d':'1'},
#         {'name':'zzz','y':'2010','m':'12','d':'12'}]

# for person in data:
#     if int(now.strftime("%m")) < int(person['m']):
#         print(person['m'],person['d'])
#         break  


# # for day in arr:
# #     if now > day:
# #         print(day)

# '''
# # print(x.strftime("%B"))
# %d	Day of month 01-31	= 31
# %m	Month as a number 01-12	= 12
# %Y	Year, full version	= 2018
# '''