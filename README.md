[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# Printing Forest Fires

> Prints CO2 emissions caused by forest fires in a given country.

This software prints CO2 emissions caused by forest fires in a given country. `run.sh` calls on `print_fires` using command line arguments. It calls a `get_column` function that parses through a .csv file to return the column of interest and the fire emissions in that column. Specific operations can be performed on the returned column, returning the mean, median, or standard deviation. 

## Installation

Clone the repository and run `print_fires.py` or `run.sh`. 

## Usage Examples

You can run the `print_fires.py` file directly using command line arguments: 

`python print_fires.py --country 'United States of America' --country_column 0 --fires_column 'Forest fires' --file_name 'Agrofood_co2_emission.csv'`

Or with an optional operation to perform:
`python print_fires.py --country 'United States of America' --country_column 0 --fires_column 'Forest fires' --file_name 'Agrofood_co2_emission.csv' --operation 'mean'`

Where `country` is a string of the country name of interest, `country_column` is the index of the column that country is in, `fires_column` is a string of the type of fires you would like to examine, and `file_name` is the path to the CSV data file. The function will then print CO2 emissions from fires as integers (rounded from original floats). 

If the file does not exist, or is inaccessible, an error will be raised. If the column of interest does not exist, an error will be raised. 

The `run.sh` file contains examples of successful and failed attempts.

## Continuous Integration
The repository has automated tests that run on any push or pull request to the master branch. It checks for: 
- Unit tests (`test_my_utils.py`)
- Functional tests (`run.sh`)
- Style checks using pycodestyle 



