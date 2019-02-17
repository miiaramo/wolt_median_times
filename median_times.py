#!/usr/bin/env python3 
""" Coding task for Wolt's engineering internships 2019. 

This tool finds median pickup times for restaurants in a city
on a specific day and time interval which are all specified by user.
"""

__author__ = "Miia Rämö"

import pandas as pd
import sys
import dateutil.parser

def get_date(x):
    """ Gets date as a string from given ISO format. """

    dates = dateutil.parser.parse(x)
    return str(dates.day) + "-" + str(dates.month) + "-" + str(dates.year)

def get_hour(x):
    """ Gets hour as an int from given ISO format. """

    dates = dateutil.parser.parse(x)
    return dates.hour

def median_times(parameters):
    """ Returns a DataFrame containing median pickup times for locations. """

    # Import data to DataFrames
    locations = pd.read_csv(parameters["locations"])
    pickup_times = pd.read_csv(parameters["pickup_times"])

    # Parse ISO timestamps for easier handling
    pickup_times["hour"] = pickup_times["iso_8601_timestamp"].apply(get_hour)
    pickup_times["date"] = pickup_times["iso_8601_timestamp"].apply(get_date)
    pickup_times = pickup_times.drop("iso_8601_timestamp", axis=1)
    
    # Filter DataFrame with user specified boundaries
    desired_data = pickup_times[pickup_times["date"] == parameters["date"]]
    desired_data = desired_data[desired_data["hour"] >= int(parameters["start"])]
    desired_data = desired_data[desired_data["hour"] <= int(parameters["end"])]
    desired_data = desired_data.drop("hour", axis=1)

    median_times = desired_data.groupby("location_id").median()
    median_times = median_times.rename(columns={"pickup_time":"median_pickup_time"}).astype(int)

    return median_times

def parse_parameters(user_input):
    """ Parses command line parameters and desired source files as a dictionary. """

    interval = user_input[2].split('-')
    parameters = {
        "city":user_input[0], 
        "date":user_input[1], 
        "start":interval[0], 
        "end":interval[1], 
        "filename":user_input[3]
    }

    # Filenames for different cities are specified in file "files.csv"
    files = pd.read_csv("files.csv")
    files = files.set_index(files["city"]).drop("city", axis=1)
    parameters["locations"] = files.loc[parameters["city"]]["locations"]
    parameters["pickup_times"] = files.loc[parameters["city"]]["pickup_times"]

    return parameters
    
def write_to_file(df, filename):
    """ Writes given DataFrame to csv file. """

    df.to_csv(filename)

def main():
    user_input = sys.argv[1:]
    try:
        parameters = parse_parameters(user_input)
        times = median_times(parameters)
        write_to_file(times, parameters["filename"])
    except:
        print("A problem occured.")
        print("Check your command line parameters.")
        print("Correct format: \"city_name D-M-YYYY HH-HH output_file_name\"")
 
if __name__ == "__main__":
    main()