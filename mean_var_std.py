import numpy as np

def calculate(list_of_numbers):
    """
    Takes a list of 9 numbers, converts it to a 3 X 3 matrix and returns a dictionary containing the
    mean, variance, standard deviation, max, min, and sum for the rows, columns and list itself.
    """
    if len(list_of_numbers) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        numpy_list = np.array(list_of_numbers)
        list_to_matrix = numpy_list.reshape(3, 3)

        calculations = {
            'mean': [list(list_to_matrix.mean(axis=0)), list(list_to_matrix.mean(axis=1)), numpy_list.mean()],
            'variance': [list(list_to_matrix.var(axis=0)), list(list_to_matrix.var(axis=1)), numpy_list.var()],
            'standard deviation': [list(list_to_matrix.std(axis=0)), list(list_to_matrix.std(axis=1)), numpy_list.std()],
            'max': [list(list_to_matrix.max(axis=0)), list(list_to_matrix.max(axis=1)), numpy_list.max()], 
            'min': [list(list_to_matrix.min(axis=0)), list(list_to_matrix.min(axis=1)), numpy_list.min()],
            'sum': [list(list_to_matrix.sum(axis=0)), list(list_to_matrix.sum(axis=1)), numpy_list.sum()]
        }

    return calculations