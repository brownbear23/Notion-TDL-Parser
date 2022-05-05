from datetime import datetime


def get_current_day_weekday():
    return datetime.today().strftime("%b %-d, %Y (%a)  %H:%M")


def get_date_time(date_time_input):
    # 2022-02-14T23:00:00.000+09:00
    date = date_time_input.split("T")[0]
    if len(date_time_input.split("T")) > 1:
        time = date_time_input.split("T")[1].split(".")[0]
        return datetime.strptime(date + " " + time, '%Y-%m-%d %H:%M:%S')
    return datetime.strptime(date, '%Y-%m-%d')
