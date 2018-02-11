from datetime import date
from pandas import read_html

"""
This function returns tables from Weather Underground's daily history page

Returns: Dictionary containing
    summary = Summary stats (the date's, and historic, avg, min, max)
    light = Sunrise and sunset stats
    moon = Moon phase
    hours = Hour-by-hour breakdown of the day with tons of stats

iata = String. Airport code
year = Int. Four-digit year
month = Int. One or two digit month number
day = Int. One or two digit month number
"""

def airportWeatherHist(iata, year, month, day):
    # make sure it is a valid date
    date(year = year, month = month, day = day)

    # make sure the variables are the right types
    IATA = str(iata)
    year = int(year)
    month = int(month)
    day = int(day)

    # get the data
    url = 'http://www.wunderground.com/history/airport/K' + iata + '/' + str(year) + '/' + str(month) + '/' + str(day) + '/DailyHistory.html?cm_ven=localwx_history'
    wuList = read_html(url)

    wuDict = dict(summary = wuList[0],
                  light = wuList[2],
                  moon = wuList[3],
                  hour = wuList[4])

    return wuDict