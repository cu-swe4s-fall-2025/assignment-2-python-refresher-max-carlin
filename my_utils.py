'''Useful functions for parsing CSV files.

    * get_column - returns a list of all values for a specified column,
    only for rows where a column matches another value.
'''
import sys


def get_column(file_name, query_column, query_value, result_column='Year'):
    '''Extract values from a column in a CSV file.

    Parameters
    ----------
    file_name : str
        The path to the CSV file.
    query_column : int
        Index of the column to test for a match to query_value.
    query_value : str
        Value of the query_column index.
    result_column : str
        Column to return values from.
    '''
    result = []

    f = None

    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)

    # Strip the first line to get the headers
    header_line = f.readline().strip()

    # Strip the header line by commas
    headers = header_line.split(',')

    # Dictionary to hold each column header and it's index
    columns = {}

    # Append each header and index to our empty dictionary ({'header' : index})
    for i, header in enumerate(headers):
        columns[header] = i

    # Get the column header through the index of our result column.
    try:
        result_index = columns[result_column]
    except:
        print('Column not found!')
        f.close()
        sys.exit(1)

    # For each line in our file
    for line in f:

        # Strip the line and split by commas
        A = line.rstrip().split(',')

        # If query column matches the query value collect the result
        if A[query_column] == query_value:
            try:
                # Originally floats in strings
                result.append(int(float(A[result_index])))
            except:
                print("Could not convert to integer or index is out of range.")

    f.close()
    return result
