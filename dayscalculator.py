import argparse

#No of days in a year till starting of every month
noofDaysTillMonth = [ 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334 ]
noofDaysTillMonthLeapYear = [ 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335 ]

#Check Leap Year
def isLeapYear(year):
  try:
    return ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)))
  except Exception as ex:
    message =str(ex).split('\n')[0]
    raise Exception(message)

#Check Start Date is previous to End Date
#startdate[dd,mm,yyyy], enddate[dd,mm,yyyy]
def checkDate(startdate, enddate):
  try:
    if (int(startdate[2]) < int(enddate[2])):
      return True
    elif ((int(startdate[2]) == int(enddate[2])) and (int(startdate[1]) < int(enddate[1]))):
      return True
    elif ((int(startdate[1]) == int(enddate[1])) and (int(startdate[0]) < int(enddate[0]))):
      return True
    else:
      return False
  except Exception as ex:
    message =str(ex).split('\n')[0]
    raise Exception(message)

#Calculate number of days for give date from 00/00/0000
#splitdate[dd,mm,yyyy]
def getDaysOffset(splitdate):
  try:
    year = int(splitdate[2]) - 1
    month = int(splitdate[1]) - 1
    day = int(splitdate[0])
    numOfLeapsYear = int(year / 4 - year / 100 + year / 400)
    if (isLeapYear(int(splitdate[2]))):
      return year * 365 + numOfLeapsYear + noofDaysTillMonthLeapYear[month] + day - 1
    else:
      return year * 365 + numOfLeapsYear + noofDaysTillMonth[month] + day - 1
  except Exception as ex:
    message =str(ex).split('\n')[0]
    raise Exception(message)

def main():
  try:
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--startdate', help='Start Date', required=True)
    parser.add_argument('-e', '--enddate', help='End Date', required=True)
    args = parser.parse_args()
    startdate = args.startdate.split("/")
    enddate = args.enddate.split("/")
    if checkDate(startdate,enddate):
      totaldays_startdate = getDaysOffset(startdate)
      totaldays_enddate = getDaysOffset(enddate)
      noofdays = totaldays_enddate - totaldays_startdate - 1
      print ("Total no of days between " + args.startdate  + " and " + args.enddate + " is " + str(noofdays))
    else:
      print ("Start date " + args.startdate + " should be previous to end date " + args.enddate)
  except Exception as ex:
    message =str(ex).split('\n')[0]
    raise Exception(message)

main()