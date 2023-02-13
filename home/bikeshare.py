import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES =['new york', 'chicago', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    month = ''
    day =''
    while True:
      city = input("Would you like to see data for Chicago, New York, or Washington\n").lower()
      if city not in CITIES:
        print("Invalid input please try again.")
        continue
      else:
        break

    #get user input for filter type (day, month, not at all) 
    while True:
      filterType = input("Would you like to filter the data by month, day, or not at all\n").lower()
      if filterType not in ('month', 'day', 'not at all'):
        print("Invalid input please try again.")
        continue
      else:
        break
        
    #get user input for month (all, january, february, ... , june)
    if (filterType in ('month', 'not at all')):
        while True:
         month = input("Which month - January, February, March, April, May, or June?\n").lower()
         if month not in MONTHS:
            print("Invalid input please try again.")
            continue
         else:
            break

    #get user input for day of week (all, monday, tuesday, ... sunday)
    if (filterType in ('day', 'not at all')):
        while True:
         day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?.\n").lower()
         if day not in DAYS:
            print("Invalid input please try again.")
            continue
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
    """
    # load city data based on the selected city 
    df = pd.read_csv(CITY_DATA[city])
    
    # convert start time to datatime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #create month, day, and hour columns in dataframe
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    #filter by month if the user select a month
    if month !='':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]
        
    #filter by day if the user select a day
    if day !='':
        df = df[ df['day'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    print('\nthe most common month is')
    print(df['month'].value_counts().idxmax())

    #display the most common day of week
    print('\nthe most common day is')
    print(df['day'].value_counts().idxmax())

    #display the most common start hour
    print('\nthe most common hour is')
    print(df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    print('\nthe most common start station is')
    print(df['Start Station'].value_counts().idxmax())

    #display most commonly used end station
    print('\nthe most common end station is')
    print(df['End Station'].value_counts().idxmax())

    #display most frequent combination of start station and end station trip
    print('\nthe most frequent combination of start station and end station trip is')
    print(df.groupby(['Start Station', 'End Station']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    print('\nthe total travel time is')
    print(df['Trip Duration'].sum() / 3600.0)


    #display mean travel time
    print('\nthe mean travel time is')
    print(df['Trip Duration'].mean() / 3600.0)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    print('\nthe counts of user types is')
    print(df['User Type'].value_counts())
    
    if city in ('new york', 'chicago'):
    #Display counts of gender
        print('\nthe counts of gender is')
        print(df['Gender'].value_counts())
    
    #Display earliest, most recent, and most common year of birth
        print('\nthe earliest year of birth is')
        print(int(df['Birth Year'].min()))
        print('\nthe most recent year of birth is')
        print(int(df['Birth Year'].max()))
        print('\nthe most common year of birth is')
        print(int(df['Birth Year'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("Would you like to see the raw data ? 'yes' or 'no'\n") 
    
    #convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i + 5]) 
            
            #appropriately subset/slice your dataframe to display next five rows
            raw = input("Would you like to see the more raw data ? 'yes' or 'no'\n").lower() 
            
            #convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()