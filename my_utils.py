def get_column(file_name, query_column, query_value, result_column = 1):
    result = []

    f = open(file_name, 'r')

    #get all the headers
    header_line = f.readline().strip()
    headers = header_line.split(',')


    columns = {}
    #put them in a dict
    for header, i in zip(headers, range(0, len(headers)+1)):
        columns[header] = i 

    #If result column is an int, just use that, if not use our dictionary to get the index    
    if type(result_column) == int:
        result_index = result_column
    else:
        result_index = columns[result_column]

    for l in f: 
        A = l.rstrip().split(',')

        if A[query_column] == query_value: 
            result.append(A[result_index])

    f.close()
    return result



