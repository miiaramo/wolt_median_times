# Wolt meadian times
Coding task for Wolt's Engineering Internships in 2019.

[The task is described here](https://github.com/woltapp/summer2019)

### How to use the tool

- Run the file 'median_times.py' in terminal with python3.
- Set parameters (city, date, time interval and output file name) in the following format as command line parameters
```
city_name D-M-YYYY HH-HH output_file_name
```
- If path is not specified for output file, it will be saved in the same folder with the python file.

### Example of usage

```
python3 median_times.py Helsinki 10-1-2019 10-12 mediantimes.csv
```
Where 
  - Helsinki is the city of which's locations we are interested in.
  - 10-1-2019 is the date we are interested in.
  - 10-12 is the time interval.
  - mediantimes.csv is the name for our output file.
