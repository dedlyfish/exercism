from datetime import date
import calendar

days = { 'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday':4, 'Saturday': 5, 'Sunday': 6 }
weeks = {'1st': 1,'2nd': 2,'3rd': 3,'4th': 4,'5th': 5}

def meetup_day(year, month, day_of_week, week):
    cal = calendar.Calendar()
    month_cal = list(cal.itermonthdays2(year, month))
    c = 0
    day = 0
    if week in weeks:
        for i,j in month_cal:
            if j==days[day_of_week] and i>0:
                c += 1
                if c == weeks[week]:
                    day = i
                    break
    if week == 'last':
    	for i,j in list(reversed(month_cal)):
    		if j==days[day_of_week] and i>0:
    			day = i
    			break
    if week == 'teenth':
    	month_cal = list(filter(lambda x: x[0] > 0, month_cal))
    	for i in range(13,20):
    		if month_cal[i-1][1] == days[day_of_week]:
    			day = i
    			break

    return date(year, month, day)
