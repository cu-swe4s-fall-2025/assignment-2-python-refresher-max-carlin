'''Useful functions for parsing CSV files.

    * get_column - returns a list of all values for a specified column,
    only for rows where a column matches another value.
    * mean - returns the mean of a list of numbers.
    * median - returns the median of a list of numbers.
    * standard_deviation - returns the standard deviation of a list of numbers.
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

    Returns
    -------
    result : list
        The list of integers for values from the desired column.
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
    except Exception:
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
            except IndexError:
                print("Index is out of range.")
                sys.exit(1)
            except Exception:
                print('Could not convert to integer.')
                sys.exit(1)

    f.close()
    return result


def mean(array):
    '''Returns the mean value of an array of numbers.

    Parameters
    ----------
    array : list
        Array of numbers to calculate the mean from.

    Returns
    -------
    mean : float
        The mean value of the array.
    '''

    try:
        mean = sum(array) / len(array)
    except ZeroDivisionError:
        print("Error: Array has length zero.")
        sys.exit(1)

    return mean


def median(array):
    '''Finds the median value of an array of integers.

    Parameters
    ----------
    array : list
        A list of integers to find the median of.

    Returns
    -------
    median : float
        The median value of the array.
    '''
    # First need to sort the array
    sorted_array = sorted(array)

    # If modulus is not zero
    if (len(sorted_array) % 2) != 0:
        # Array length is odd, take middle value
        i = int(len(sorted_array) / 2)
        med = sorted_array[i]
        return med

    # If modulus is zero, array lenght is even
    elif (len(sorted_array) % 2) == 0:

        # Get indices of two middle values
        i_1 = int(len(sorted_array) / 2)
        i_2 = int((len(sorted_array) / 2) - 1)

        try:
            med = (sorted_array[i_1] + sorted_array[i_2]) / 2
        except IndexError:
            print('Error: Empty array!')
            sys.exit(1)

        return med


def standard_deviation(array):
    '''Finds the standard deviation of an array of integers.

    Parameters
    ----------
    array : list
        A list of integers to find the standard deviation of.

    Returns
    -------
    std : float
        The standard deviation of the array.
    '''
    # First, get the mean
    array_mean = mean(array)

    # Will hold the sum of our residuals
    residual_sum = 0

    # Get the residuals for each value
    for val in array:
        residual = (val - array_mean)**2
        residual_sum += residual

    # Calculate standard deviation
    std = (residual_sum / len(array))**0.5

    return std
