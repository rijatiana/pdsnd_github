import time
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city.lower() not in CITY_DATA:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n')   
    if city.lower() in CITY_DATA:
        city = CITY_DATA[city.lower()]
    else:
        print('Would you like to see data for Chicago, New York, or Washington?.')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month_inp = ''
    while month_inp.lower() not in MONTH_DATA:
        month_inp = input('\n Which month - January, February, March, April, May, or June? or "all" for no month filter\n')
        if month_inp.lower() not in MONTH_DATA:
            print('Which month - January, February, March, April, May, or June?')
        else:
            month = month_inp.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_inp = ''
    while day_inp.lower() not in DAY_DATA:
        day_inp = input("\n Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?or 'all' for no day filter\n")
        if day_inp.lower() not in DAY_DATA:
            print("\n name of the day please or 'all' for all the day?\n\n")
        else:
            day = day_inp.lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # convert to dataframe
    df = pd.read_csv(city)

    # convert the Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time and create columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
 
    # filter by month
    if month != 'all':
        month = MONTH_DATA.index(month)

        df = df.loc[df['month'] == month]

    # filter by day
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is: " + MONTH_DATA[common_month].title())

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types is: \n" + str(user_types))

    # TO DO: Display counts of gender
    for city in CITY_DATA:
        if city == 'chicago.csv' or city == 'new_york_city.csv':
            gender = df['Gender'].value_counts()
            print("\nThe count of user gender is: \n" + str(gender))
    
    # TO DO: Display earliest, most recent, and most common year of birth
            earliest = df['Birth Year'].min()
            most_recent = df['Birth Year'].max()
            most_common = df['Birth Year'].mode()[0]
            print('\nEarliest birth is: {}\n'.format(earliest))
            print('Most recent birth is: {}\n'.format(most_recent))
            print('Most common birth is: {}\n'.format(most_common) )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def five_row(df):
    display=''
    DISPLAY_DATA = ['yes', 'no']   
    a = 0
    b = 5     
    while display.lower() not in DISPLAY_DATA:
        display = input('Would you like to view 5 more rows?\n')   
    if display.lower() not in DISPLAY_DATA:
        print('Would you like to see more 5 rows?.')  
          #############################
    if display.lower()== 'yes':
        print(df[df.columns[0:-1]].iloc[a:b])
        display_more= ''
        while display_more.lower()!= 'no':
            display_more = input('\nWould you like to view 5 more rows?'
                                     'Type \'yes\' or \'no\'.\n')
            if display_more.lower() == 'yes':
                a += 5
                b += 5
                print(df[df.columns[0:-1]].iloc[a:b])
            elif display_more.lower() == 'no':
                break
            else:
                print('Would you like to see more 5 rows?.')
                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        five_row(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

#author:  Rijatiana