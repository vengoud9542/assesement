a = input()
b = input()

am = int(a[4:6])
bm = int(b[4:6])

ay = int(a[0:4])
by = int(b[0:4])

import calendar
if ay >= 1900 and by <= 2100:
    for each_year in range(ay, (by+1)):
        for month in range(am, (bm + 1)):
            cal = calendar.monthcalendar(each_year, month)
            first_week  = cal[0]
            second_week = cal[1]
            third_week  = cal[2]
            fourth_week  = cal[3]
            if first_week[calendar.SATURDAY]:
                d = first_week[calendar.SATURDAY]

                if d%5 == 0:
                    if len(str(d)) == 1:
                        d = '0' + str(d)
                    s = str(each_year) + '' + str(month) + '' + str(d)
                    if int(s) >= int(a) and int(s) <= int(b):
                        print(s)

            if second_week[calendar.SATURDAY]:
                d = second_week[calendar.SATURDAY]
                if d%5 == 0:
                    if len(str(d)) == 1:
                        d = '0' + str(d)
                    if len(str(month)) == 1:
                        month = '0' + str(month)
                    s = str(each_year) + '' + str(month) + '' + str(d)
                    if int(s) >= int(a) and int(s) <= int(b):
                        print(s)

            if third_week[calendar.SATURDAY]:
                d = third_week[calendar.SATURDAY]
                if d%5 == 0:
                    if len(str(d)) == 1:
                        d = '0' + str(d)
                    if len(str(month)) == 1:
                        month = '0' + str(month)
                    s = str(each_year) + '' + str(month) + '' + str(d)
                    if int(s) >= int(a) and int(s) <= int(b):
                        print(s)
            
            if fourth_week[calendar.SATURDAY]:
                d = fourth_week[calendar.SATURDAY]
                if d%5 != 0:
                    if len(str(d)) == 1:
                        d = '0' + str(d)
                    if len(str(month)) == 1:
                        month = '0' + str(month)
                    s = str(each_year) + '' + str(month) + '' + str(d)
                    if int(s) >= int(a) and int(s) <= int(b):
                        print(s)
            
            if first_week[calendar.SATURDAY] == 0:
                fifth_week  = cal[4]
                d = fifth_week[calendar.SATURDAY]
                if d%5 != 0:
                    if len(str(d)) == 1:
                        d = '0' + str(d)
                    if len(str(month)) == 1:
                        month = '0' + str(month)
                    s = str(each_year) + '' + str(month) + '' + str(d)
                    if int(s) >= int(a) and int(s) <= int(b):
                        print(s)