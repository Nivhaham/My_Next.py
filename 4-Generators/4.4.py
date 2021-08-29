def gen_secs():
    while True:
        gen_sec = (f"{secs:02}" for secs in range(60))
        for i in gen_sec:
            yield i


def gen_minutes():
    while True:
        gen_mins = (f"{mins:02}" for mins in range(60))
        for i in gen_mins:
            yield i


def gen_hours():
    while True:
        gen_hours = (f"{hours:02}" for hours in range(24))
        for i in gen_hours:
            yield i


def gen_time():
    hours = gen_hours()
    mins = gen_minutes()
    secs = gen_secs()
    curr_hour, curr_mins, curr_secs = next(hours), next(mins), next(secs)
    time_format = curr_hour + ":" + curr_mins + ":" + curr_secs
    for i in range(3600):
        yield time_format
        curr_secs = next(secs)
        if curr_secs == "00":
            curr_mins = next(mins)
        if curr_secs == "00" and curr_mins == "00":
            curr_hour = next(hours)

        time_format = curr_hour + ":" + curr_mins + ":" + curr_secs


def gen_years(year=2021):
    while True:
        yield year
        year += 1


def gen_days_month(month, leap_year=True):
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    day = 1
    while True:
        yield str(day) + "/" + str(month)
        # private case of last day of the year.
        if month == 12 and days_in_month[month] == day:
            month = 1
            day = 0
        # leap year
        if month == 2 and leap_year and days_in_month[month] == day:
            day += 1
            yield day
        # last day of a month
        if days_in_month[month] <= day:
            month += 1
            day = 1
        else:
            day += 1


def gen_date():
    years, days_month = gen_years(), gen_days_month(1)
    curr_day_month, curr_year = next(days_month), next(years)
    time_format = str(curr_day_month) + "/" + str(curr_year)

    for i in range(300):
        yield time_format
        if curr_day_month == "31/12":
            curr_year = next(years)
        curr_day_month = next(days_month)

        time_format = str(curr_day_month) + "/" + "/" + str(curr_year)


def check_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True


def main():
    for gd in gen_date():
        for gt in gen_time():
            print(gd + "  " + gt)


if __name__ == '__main__':
    main()
