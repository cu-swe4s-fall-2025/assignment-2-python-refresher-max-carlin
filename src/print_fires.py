'''Printing CO2 Emissions

This script allows the user to print the CO2 emissions caused by forest fires
in any available country. It accepts .csv files. It requires a country,
the column index of the country, the column header to extract from,
and the path to the file to extract from.

It contains the following custom function:
    * get_column - returns a list of the column values of interest.
'''

from my_utils import get_column
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=(
            "Prints forest fires given a country, a column number,"
            "the name of the column, and the CSV file to pull from."),
        prog='print_fires')

    parser.add_argument('--country',
                        type=str,
                        help='Country of interest.',
                        required=True)

    parser.add_argument('--country_column',
                        type=int,
                        help='The column index of the country.',
                        required=True)

    parser.add_argument('--fires_column',
                        type=str,
                        help='Column header to extract from.',
                        required=True)

    parser.add_argument('--file_name',
                        type=str,
                        help='The path to the file to extract from.',
                        required=True)

    args = parser.parse_args()

    # Run the get_column function to retrieve the desired column.
    fires = get_column(args.file_name,
                       args.country_column,
                       args.country,
                       args.fires_column)

    # Print the list of forrest fire CO2 emmissions.
    print(fires)
