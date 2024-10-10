import time
import pandas as pd
import numpy as np
import calendar
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
    cities = ['chicago', 'new york city', 'washington']
    city = ''
    while city not in cities:
        city = input('Input city (chicago, new york city, washington): ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    month = input('Input month: ').lower()
    while month not in months:
        month = input('Input month: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Input day of week: ').lower()
    while day not in days:
        day = input('Input day of week: ').lower()
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()
    
    # check month different all
    if month != 'all':
        # look for the index of the months list to get the int correspondingly
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # Create the new dataframe by flitering the month
        df = df[df['Month'] == month]
        # check day different all
        if day != 'all':
            # Create the new dataframe by filtering day of week
            df = df[df['Day'] == day.title()]   
    df['Hour'] = df['Start Time'].dt.hour
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    Kommon_month = df['Month'].mode()[0]
    print(Kommon_month)
    # TO DO: display the most common day of week
    Kommon_day = df['Day'].mode()[0]
    print(Kommon_day)
    # TO DO: display the most common start hour
    Kommon_hour = df['Hour'].mode()[0]
    print(Kommon_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    Kommon_start_station = df['Start Station'].mode()[0]
    Kommon_end_station = df['End Station'].mode()[0]
    df['Travel map'] = df['Start Station'] + ' => '+ df['End Station']

    # TO DO: display most commonly used start station
    print('Most commonly used start station: ', Kommon_start_station)

    # TO DO: display most commonly used end station
    print('Most commonly used end station: ', Kommon_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip: ', df['Travel map'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Count of user types: ', user_type_counts)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('Count of gender: ', gender_counts)
    except:
        print('No gender data available for the city mentioning')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_birth = int(df['Birth Year'].min())
        recent_year_birth = int(df['Birth Year'].max())
        Kommon_year_birth = int(df['Birth Year'].mode()[0])
        print('Earliest year of birth: ', earliest_year_birth)
        print('Recent year of birth: ', recent_year_birth)
        print('Cammon year of birth: ', Kommon_year_birth)
    except:
        print('No birth data available for your city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        """Display 5 rows data when user press"""
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        start_loc = 0
        while view_data == 'yes':
            start_loc += 5
            print(df.head(start_loc))
            view_data = input("Do you wish to continue?: ").lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
