import time
import pandas as pd
import numpy as np
from itertools import islice

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
    city = input("What city data are you interested in? (chicago, new york city, washington): \n").lower()
    cities = ["chicago", "new york city", "washington"]
    while city not in cities:
        print("Wrong input! \nTry again.")
        city = input("What city data are you interested in? (chicago, new york city, washington): \n").lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month are you interested in? (all, january, february, ... , june): \n").lower()
    months = ["all", "january", "february", "march", "april", "may", "june"]
    while month not in months:
        print("Wrong input! \nTry again.")
        month = input("Which month are you interested in? (all, january, february, ... , june): \n").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day of the week are you intereted in? (all, monday, tuesday, ... sunday): \n").lower()
    days_in_a_week = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    while day not in days_in_a_week:
        print("Wrong input! \nTry again.")
        day = input("Which day of the week are you intereted in? (all, monday, tuesday, ... sunday): \n").lower()
    
    print('-'*40)
    return city, month, day


def read_data(city):
    """ Checks if user is interested in the raw data, if yes, prints five lines data. It keeps on doing this until the user is no longer interested.

    Args:
        (str) city - name of the city to analyze
    Prints:
        (str) excerpts of raw data
    """
    should_read = input("Do you want to view excerpts of the raw data? Type 'yes' or 'no' \n").lower()
    N = 5
    replies = ["yes", "no"]

    while should_read not in replies:
        print("Wrong input! \nTry again.")
        should_read = input("Do you want to view excerpts of the raw data? Type 'yes' or 'no' \n").lower()
        
    while should_read == 'yes':
        with open(CITY_DATA[city], "r") as file:
            if file == "":
                print("End of file")
                break
                       
            print('\nLoading raw data....\n')
            print('\nHere you go!\n')
            start_time = time.time()
            
            # Slices the file to show the first N lines
            lines = islice(file, N)
            for line in lines:
                print(line)
        
        print("\nThis took %s seconds." % (time.time() - start_time))
        should_read = input("Do you want to view more excerpts of the raw data? Type 'yes' or 'no' \n").lower()
        N += 5
        
        print('-'*40)

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
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1 
        df = df[df["month"] == month]
        
    if day != "all":
        df = df[df["day_of_week"] == day.title()]
        
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # The question, "the most common month", is only valid if the user requests for all the available months
    if month == "all":
        most_common_month = df["month"].mode()[0]
        months = ["January", "February", "March", "April", "May", "June"]
        most_common_month = months[most_common_month-1]
        print("The most common month:", most_common_month)
         

    # TO DO: display the most common day of week
    # The question, "the most common day of the week", is only valid if the user requests for all the available months
    if day == "all":
        most_common_day_of_week = df["day_of_week"].mode()[0]
        print("The most common day of the week:", most_common_day_of_week)
    
    # TO DO: display the most common start hour
    most_common_start_hour = df["Start Time"].dt.hour.mode()[0]
    print("The most common start hour:", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print(popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print(popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["station_combination"] = df["Start Station"]+ " & " + df["End Station"]
    most_frequent_station_combination = df["station_combination"].mode()[0]
    print(most_frequent_station_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = np.sum(df["Trip Duration"])
    print("The total travel time is: ", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = np.mean(df["Trip Duration"])
    print("The mean travel time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("\nThe number of users for each user type: ")
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender_count = df["Gender"].value_counts()
        print("\nThe number of users per gender: ")
        print(gender_count)  

    except KeyError:
        print("\nThe number of users per gender: Not Available")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = np.min(df["Birth Year"])
        print("\nThe earliest year of birth: ", earliest_birth_year)

        latest_birth_year = np.max(df["Birth Year"])
        print("\nThe most recent year of birth: ", latest_birth_year)

        popular_birth_year = df["Birth Year"].mode()[0]
        print("\nThe most common year of birth: ", popular_birth_year)

    except KeyError:
        print("Users' year of birth not available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        read_data(city)
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
