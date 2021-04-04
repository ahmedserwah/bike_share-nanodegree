import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while True:
        cites =['washington','new york city','chicago']
        city=input("enter the city name in lower case:").lower()
        if city not in cites :
            print ('enter the city name correctly')   
        else:
         break
      
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        MONTH_DATA=['all','january',' february ','march','april ','may','june']
        month=input("enter word all or a month between jan to june:").lower()
        if month!='all' and month not in MONTH_DATA:
         print ("make sure you typed a vaild month")
        else:
         break
         
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        days=['all','satrday','sunday','monday','tuesday','wednesday','thursday']
        day=input('enter a vaild day name or type word all:').lower()
        if day!='all'and day not in days :
            print("make sure you typed it correctly")
        else:
            break
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
    " load data file into a dataframe 
    """
     #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
def Show_Raw_Data(df):
    start_loc = 0
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()   
    while True:
        if view_data  =='no':
            break
        print(df.iloc[start_loc :start_loc+ 5])
        view_display = input("Do you wish to continue?: ").lower()
        start_loc += 5

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print("the most common month:",common_month)

    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print("the most common day:",common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour= df['hour'].mode()[0]
    print("the most common hour:",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     # TO DO: display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print('the most  commonly used start station is :',start_station)
    # TO DO: display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print('the most  commonly used end station is : ',end_station)
    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = (df['Start Station']+ df['End Station']).mode()[0]
    print('the most frequent combination is : ',most_common_start_end_station)                        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()  
    print("total time duration is :",total_time)

    # TO DO: display mean travel time
    average_time=df['Trip Duration'].mean()
    print("average time duraiton is :",average_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types  
    print("user types is:",df['User Type'].value_counts())                                 
   
# TO DO: Display counts of gender
    if 'Gender' in df:   
        print( "counts gender:",df['Gender'].value_counts())
    else:
     print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
     
                                
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year_of_birth=(df['Birth Year'].min())
        print(earliest_year_of_birth)
        most_recent=(df['Birth Year'].max())
        print(most_recent)
        most_common_year=(df['Birth Year'].mode()[0])
        print(most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        Show_Raw_Data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
