def get_column(file_name, query_column, query_value, result_column):
    result = []

    f = open(file_name, 'r')


    for l in f: 
        A = l.rstrip().split(',')

        if A[query_column] == query_value: 
            result.append(A[result_column])

    f.close()
    return result



