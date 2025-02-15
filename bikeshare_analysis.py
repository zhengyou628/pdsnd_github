import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Ask the user to choose a city, month, and day to filter the data.

    Returns:
        (str) city - chosen city ('chicago', 'new york city', 'washington')
        (str) month - chosen month ('january' ~ 'june', or 'all')
        (str) day - chosen day ('monday' ~ 'sunday', or 'all')

    Notes:
        - Keeps asking until the user enters a valid input.
        - If 'all' is chosen, no filter is applied.
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city
    while True:
        city = input("Which city would you like to analyze? (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        print("Invalid input. Please enter one of the given cities.")
    
    # Get user input for month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Which month? (all, january, february, ... , june): ").lower()
        if month in months or month == 'all':
            break
        print("Invalid input. Please enter a valid month or 'all'.")
    
    # Get user input for day
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Which day? (all, monday, tuesday, ... sunday): ").lower()
        if day in days or day == 'all':
            break
        print("Invalid input. Please enter a valid day or 'all'.")
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    
    if month != 'all':
        month_index = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['month'] == month_index]
    
    if day != 'all':
        df = df[df['day_of_week'] == day]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    print(f"Most common month: {df['month'].mode()[0]}")
    print(f"Most common day of week: {df['day_of_week'].mode()[0]}")
    print(f"Most common start hour: {df['Start Time'].dt.hour.mode()[0]}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    print(f"Most commonly used start station: {df['Start Station'].mode()[0]}")
    print(f"Most commonly used end station: {df['End Station'].mode()[0]}")
    df['route'] = df['Start Station'] + " to " + df['End Station']
    print(f"Most common trip: {df['route'].mode()[0]}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    print(f"Total travel time: {df['Trip Duration'].sum()} seconds")
    print(f"Mean travel time: {df['Trip Duration'].mean()} seconds")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    print("User Type Counts:")
    print(df['User Type'].value_counts())
    
    if 'Gender' in df:
        print("\nGender Counts:")
        print(df['Gender'].value_counts())
    
    if 'Birth Year' in df:
        print("\nBirth Year Statistics:")
        print(f"Earliest year: {int(df['Birth Year'].min())}")
        print(f"Most recent year: {int(df['Birth Year'].max())}")
        print(f"Most common year: {int(df['Birth Year'].mode()[0])}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays 5 rows of raw data at a time upon user request."""
    row_index = 0
    while True:
        raw_data = input("\nWould you like to see 5 rows of raw data? Enter yes or no: ").lower()
        if raw_data != 'yes':
            break
        print(df.iloc[row_index: row_index + 5])
        row_index += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
