def getTimeDetails():

    today = date.today()

    today = str(today)
    year, month, day = today.split("-")

    year = int(year)
    month = int(month)
    day = int(day)

    season = 1

    if month >= 4 and month <=6:
        season = 2
    elif month >=7 and month <=9:
        season = 3
    elif season >=10 and month <=12:
        season = 4
    time = datetime.now().hour

    return time, day, month, year, season