# 1
from datetime import datetime
from datetime import timedelta

start_date = '2018-01-02'
end_date = '2018-01-07'
def date_range():
    days = []
    start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
    current_dt = start_date_dt
    while current_dt <= end_date_dt:
        days.append(current_dt.strftime('%Y-%m-%d'))
        current_dt += timedelta(days=1)
    return(days)

# 2
def date_range():
    days = []
    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
        current_dt = start_date_dt
        start_date_dt<end_date_dt
        while current_dt <= end_date_dt:
            days.append(current_dt.strftime('%Y-%m-%d'))
            current_dt += timedelta(days=1)
        return days
    except ValueError:
        return days

# 3
def date_check(stream):
    for date in stream:
        try:
            datetime.strptime(date, '%Y-%m-%d')
            print(True)
        except ValueError:
            print(False)

# 4
def dates_before(date):
    date_dt = datetime.strptime(date, '%Y-%m-%d')
    one_day = timedelta(days=1)
    one_month_before = date_dt - one_day
    if date_dt.day == 1:
        while one_month_before.day != date_dt.day:
            print(one_month_before.strftime('%Y-%m-%d'))
            one_month_before -= one_day
            if one_month_before.day == date_dt.day:
                print(one_month_before.strftime('%Y-%m-%d'))
    else:
        while one_month_before.month == date_dt.month:
            print(one_month_before.strftime('%Y-%m-%d'))
            one_month_before -= one_day

# 5
from datetime import date
def days(request):
    if request == 'today':
        return date.today().strftime('%Y-%m-%d')
    if request == 'last monday':
        today_date = date.today()
        day_of_week = date.today().weekday()
        while day_of_week != 0:
            day_of_week -= 1
            today_date -= timedelta(days=1)
        print(today_date.strftime('%Y-%m-%d'))
    if request == 'last day':
        today_date = date.today()
        yesterday_date = date.today() - timedelta(days=1)
        month_today = date.today().month
        while today_date.month == month_today:
            today_date += timedelta(days=1)
            yesterday_date += timedelta(days=1)
        print(yesterday_date.strftime('%Y-%m-%d'))

# 6
def weeks():
    i = 0
    start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
    while start_date_dt <= end_date_dt:
        print(start_date_dt.strftime('%Y-%m-%d'),start_date_dt.weekday())
        start_date_dt += timedelta(days=1)
        if start_date_dt.weekday() == 0:
            i += 1
            print('week', i)
