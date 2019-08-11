# Sypht--code--Test

Difference Between Dates:

## Instructions to run the script:
                       
                       # dayscalculator.py -s  startdate -e  enddate

Input date format: DD/MM/YYY

Example: daycalculator.py -s 20/05/2010 -e 11/08/2019


## Conditions to consider:
             
• A date defined by three integer values: y (year), m (month) and d (day).

•	Input of two dates in the format: date1 = (d1, m1, y1) and date2 = (d2, m2, y2).

•	Precondition: Date1 lies before date2.
Note that this just simplifies the explanation but is actually no constraint because the dates can be easily swapped before passed as input to any algorithm.

•	Date1 is also called the preceding date while date2 is also called the subsequent date.

•	Example dates are given in form DD/MM/YYYY e.g.  09/08/2019.

### A) Function[isLeapYear] to detect if the current year is a leap year. A leap year is divisible by 4 but not divisible by 100, with the exception that if it's divisible by 400 it's again a leap year.


### B) Function [check date]:
If date1[start date] lies before date2[End date]. First check the year: If y1 < y2 date1 lies before date2. If y1 > y2 then not. More interesting is the case when y1 equals y2: Then we have to look at the months: if m1 < m2, date1 precedes date2; if m1 > m2, then date1 is after date2. Again, if m1 == m2, we have finally to check d1 against d2


### C) Lookup table is used which holds the accumulated days of all whole months. The month is used as the index for access. 

E.g. --- For March, we get 59 because January and February (which are the preceding full months of March) have together 59 days (31+28). As you might guess now, we will use actually two lookup table, one for leap years and the other for non-leap years as the values differ starting from February. Do not get confused by the fact we start counting the months from 1 (January) while the arrays are started from Zero. Here are both tables:

              noofDaysTillMonth = [ 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
              noofDaysTillMonthLeapYear =  [ 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]


### D)Assume we just want to get the difference from 01-01 of any year to the origin, thus only full years. Well, what we have need is the number of leap years in this duration - this gives us the number of additional days to add. Because the origin year is 1, we can derive following formula:
                    
                    Formulae: numOfLeapsYear  = (year-1) / 4 - (year-1) / 100 + (year-1) / 400

We must subtract one because we start at origin year 1 - so e.g. for year 4, there is no leap year in between. To calculate the number of days, multiply the number of years with 365 and add the value of numOfLeapsYear because this is exactly the number of additional days of the leap years.

To add the remaining days of the given date, use again the lookup tables to add the remaining duration of the whole months and finally the remaining days.

           Example: Get the difference from 1089-02-18 to the origin
           o	numOfLeapsYear = (1089-1) / 4 - (1089-1) / 100 + (1089-1) / 400 = 264.
           o	Number of days between 1089-1-1 to origin: 
              Output = 365 * (1089-1) + numOfLeapsYear = 365 * (1089-1) + 264 = 397384.
           o	Add the remaining in years 1089: Result = Output + 49 = 397384 + 49 = 397433.



## Explanation

The code is written in the form of try-exception blocks so that any sort of error can be handled properly. In the code, argparse module is deployed to make the code reproduceable and of user-friendly command-line interfaces as the module automatically generates help and usage messages and issues errors when invalid inputs are passed.

The argparse module creates ArgumentParser object that can parse the command line input into required Python data types. Information is given to ArgumentParser by calling add_argument method. Finally when the parse_args() method is called all of the information that is stored will be used.



In the startdate variable, the date part of the start date is stored by splitting at the first ‘/’ using split function. Similarly, enddate is also filled.


Then the startdate is to be checked if it is before the enddate or not. For this purpose, checkDate function is called passing both the dates. In the function, first both the years of startdate and enddate are checked if the former is before the latter. If it is false, then the years are checked if they are same and the months are checked if the month of startdate is prior to that of enddate or not. If this is also false, then it is checked if both the dates are of same year, month but the date part of startdate is prior to that of the enddate or not. If this is also false, then a message is returned saying start date should be before the end date. 


If checkDate function returns true in any of the above cases, getDaysOffset function is called passing the startdate to know the number of dates between the startdate and the reference date taken as 0/00/0000. In the getDaysOffset function, isLeapYear function is called to know if the year prior to the start year is a leap year or not. If this is true, then the number of days in the prior month of the startdate increases by one if it is not January. For this, noofDaysTillMonthLeapYear function is called to get the number of days in that particular year till the previous month. Similar process is followed if the previous year is not a leap year and the noofDaysTillMonth function is called to get the number of days. By using these methods, the number of days between the reference considered and startdate, enddate is found.


The above obtained days are to be subtracted to know the difference between both the dates and the resultant is printed out.


