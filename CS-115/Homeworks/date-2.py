'''
Created on Benjamin Singleton
@author:   11/21/2019
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. 

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """Returns a new object with the same month, day, year
           as the calling object (self)."""
        dnew=Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        """Decides if self and d2 represent the same calender date,
           whether or not they are in the same place in memory."""
        return self.year == d2.year and self.month == d2.month and \
               self.day == d2.day

    def tomorrow(self):
        """Returns the next day to the date"""
        if self.isLeapYear()==True and self.day==28 and self.month==2:
            self.day+=1
        elif self.isLeapYear()==True and self.day==29 and self.month==2:
            self.day=1
            self.month=3
        elif self.day==DAYS_IN_MONTH[self.month] and self.month!=12:
            self.day=1
            self.month+=1
        elif self.day==DAYS_IN_MONTH[self.month] and self.month==12:
            self.day=1
            self.month=1
            self.year+=1
        else:
            self.day+=1
        self=Date(self.month, self.day, self.year)

    def yesterday(self):
        """Returns the previous day to teh date"""
        if self.day==1 and self.month==1:
            #print("One")
            self.day=31
            self.month=12
            self.year-=1
        elif self.isLeapYear()==True and self.month==3 and self.day==1:
            self.day=29
            self.month=2
        elif self.day==1:
            self.month-=1
            self.day=DAYS_IN_MONTH[self.month]
        else:
            self.day-=1

    def addNDays(self, N):
        """Adds N day to the date"""
        print(self)
        for i in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        """Subtracts N days from the date"""
        print(self)
        for i in range(N):
            self.yesterday()
            print(self)

    def isBefore(self, d2):
        """Returns true if self is before d2, otherwise returns false"""
        if self.day == d2.day and self.month == d2.month and self.year == d2.year:
            return False
        elif self.year<d2.year:
            return True
        elif self.year>d2.year:
            return False
        elif self.month<d2.month:
            return True
        elif self.month>d2.month:
            return False
        elif self.day<d2.day:
            return True
        else:
            return False

    def isAfter(self, d2):
        """Returns true if self is after d2, otherwise returns false"""
        if self.day == d2.day and self.month == d2.month and self.year == d2.year:
            return False
        elif self.isBefore(d2)==True:
            return False
        else:
            return True

    def diff(self, d2):
        """Returns the difference between self and d2"""
        date1=self.copy()
        date2=d2.copy()
        if self.day == d2.day and self.month == d2.month and self.year == d2.year:
            return False
        elif self.isBefore(d2)==False:
            count=0
            while True:
                date1.yesterday()
                count+=1
                if date1.day == date2.day and date1.month == date2.month and date1.year == date2.year:
                    return count
        else:
            count=0
            while True:
                date1.tomorrow()
                count+=1
                if date1.day == date2.day and date1.month == date2.month and date1.year == date2.year:
                    return count*-1
    
    def dow(self):
        """Returns what day of the week a given date is"""
        Dict={0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
        Dict2={0:"Sunday", 6:"Monday", 5:"Tuesday", 4:"Wednesday", 3:"Thursday", 2:"Friday", 1:"Saturday"}
        known=Date(11,3,2019) #Sunday
        date=self.copy()
        if date.isAfter(known):
            val=known.diff(date)
            if val<0:
                val=val*-1
            val=val%7
            return Dict[val]
        else:
            val=known.diff(date)
            if val<0:
                val=val*-1
            val=val%7
            return Dict2[val]
