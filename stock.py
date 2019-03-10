# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 22:09:14 2018

@author: Sarah
"""
import datetime
#goal 1 create a list of dates for the next ex dividend date
#goal 1.1 get today's date
#goal 1.2 get the next viable exdividend date(s)
print("Getting date")

strToday = str( datetime.datetime.today().strftime('%Y-%m-%d'))

#strToday = str(datetime.datetime.today() )
print(strToday)
today = datetime.datetime.today() 
year, month, day = (int(x) for x in strToday.split('-'))    
weekno = datetime.date(year, month, day).weekday()
weeknoTom = weekno + 1;
#goal 1 create a list of dates for the next ex dividend date
#Monday - 0 - 1 - get Tuesday's
#Tuesday - 1 - 2 - get Wednesday's
#Wednesday - 2 -3 - get Thursday's
#Thursday - 3 -4 - get Friday's
#Friday - 4 - 5 -get Saturday's, Sunday's, and Monday's
#Saturday - 5 - 6 - get Tuesday's
#Sunday -6 - 7 - get Tuesday's

def isHoliday(curDate, curYear):
    #print("in isHoliday")
    year, month, day = (int(x) for x in curDate.split('-'))    
    answer = datetime.date(year, month, day).weekday()
    #print(curDate)
    #print(answer)
    #check if Week end
    if(answer>4):
        return "true"
    #New Year's Day
    elif(curDate == curYear + '-01-01'):
        return "true"
    #Martin Luther King Jr. Day
    elif(curDate == curYear + '-01-15'):
        return "true"
    #President's Day
    elif(curDate == curYear + '-02-19'):
        return "true"
    #Good Friday ----- NOTE THIS DATE CHANGES YEAR TO YEAR
    elif(curDate == curYear + '-03-30'):
        return "true"
    #Memorial Day
    elif(curDate == curYear + '-05-28'):
        return "true"
    #WARNING 
    elif(curDate == curYear + '-01-15'):
        print("EARLY CLOSE 1 pm")
        return "false"
    #Independence Day
    elif(curDate == curYear + '-07-04'):
        return "true"
    #Labor Day
    elif(curDate == curYear + '-09-03'):
        return "true"
    #Thanksgiving Day
    elif(curDate == curYear + '-11-22'):
        return "false"
    #WARNING Christmas Eve
        return "true"
    #WARNING
    elif(curDate == curYear + '-11-23'):
        print("EARLY CLOSE 1 pm")
    elif(curDate == curYear + '-01-15'):
        print("EARLY CLOSE 1 pm")
        return "false" 
    #Christmas Day
    elif(curDate == curYear + '-12-25'):
        return "true"
    else:
        return "false"
        



strCurYr = datetime.datetime.strftime(today,'%Y')
lstDatesToCheck = []
lstDates = []
daysFromToday = 1

result = "true"
#check for Holidays
while result == "true":   
    dayToCheck = today + datetime.timedelta(daysFromToday)
    daysFromToday += 1
    strToCheck =  datetime.datetime.strftime(dayToCheck,'%Y-%m-%d')
    lstDatesToCheck.append(strToCheck)
    result = isHoliday(strToCheck,strCurYr)
print("Upcoming exdividend dates")
print(lstDatesToCheck)   
    
#at this point all the exdividend dates should be collected in lstDatesToCheck

# importing module
import sqlite3
 
# connecting to the database 
connection = sqlite3.connect("myTable.db")
dictMonth = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
numDaystoCheck = len(lstDatesToCheck)
print("Number of Days to check: ", numDaystoCheck)

strRootSite = "https://www.nasdaq.com/dividend-stocks/dividend-calendar.aspx?date="
from bs4 import BeautifulSoup
import requests
daysleft = 0
lstExDividendDayWeb = []
#add websites to a list of form https://www.nasdaq.com/dividend-stocks/dividend-calendar.aspx?date=2019-Mar-11
for exDividendDay in lstDatesToCheck: 
    print(exDividendDay)
    year = exDividendDay[0:4]
    day = exDividendDay[8:10]
    month = dictMonth[exDividendDay[5:7]]
    print(year + month + day)
    site = strRootSite + year + '-'+ month + '-' + day
    lstExDividendDayWeb.append(site)
    print(site)
    
print(lstExDividendDayWeb)

   




































