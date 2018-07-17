#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 15:12:42 2018

@author: rahulkumar
"""

import pandas as pd
df = pd.read_csv('/Users/rahulkumar/Downloads/All Activities.csv')
df = df.drop('Path' ,axis=1)

features = pd.DataFrame(df['Application'])

from datetime import datetime
# sleep: 12-5, 6-9: breakfast, 10-14: lunch, 14-17: dinner prep, 17-21: dinner, 21-23: deserts!
times_of_day = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5 ]
time_of_day = lambda x: times_of_day[datetime.strptime(x, "%d/%m/%Y, %H:%M:%S %p").hour]
df['time_of_day'] = df['Start Date'].map(time_of_day)



year = lambda x: datetime.strptime(x, "%d/%m/%Y, %I:%M:%S %p").year
features['year'] = df['Start Date'].map(year)

month = lambda x: datetime.strptime(x, "%d/%m/%Y, %I:%M:%S %p").month
features['month'] = df['Start Date'].map(month)


day = lambda x: datetime.strptime(x, "%d/%m/%Y, %I:%M:%S %p").day
features['day'] = df['Start Date'].map(day)

hour = lambda x: datetime.strptime(x, "%d/%m/%Y, %I:%M:%S %p").hour
features['hour'] = df['Start Date'].map(hour)


minute = lambda x: datetime.strptime(x, "%d/%m/%Y, %I:%M:%S %p").minute
features['minute'] = df['Start Date'].map(minute)

second = lambda x: datetime.strptime(x, "%d/%m/%Y, %I:%M:%S %p").second
features['second'] = df['Start Date'].map(second)

week = lambda x: datetime.strptime(x, "%d/%m/%Y, %I:%M:%S %p").weekday()
features['week'] = df['Start Date'].map(week)


day_of_week = lambda x: datetime.strptime(x,"%d/%m/%Y, %I:%M:%S %p").weekday()
features['day_of_week'] = df['Start Date'].map(day_of_week)

# please read docs on how week numbers are calculate
week_number = lambda x: datetime.strptime(x, "%d/%m/%Y, %I:%M:%S %p" ).strftime('%V')
features['week_number'] = df['Start Date'].map(week_number)






















