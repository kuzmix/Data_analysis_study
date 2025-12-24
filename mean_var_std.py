import numpy as np

def calculate(values:list):
    if len(values)<9:
        raise ValueError('List must contain nine numbers.')
    matrix = np.array(values)
    matrix.resize((3,3))
    result = {'mean': axis_operations(matrix.mean),
              'variance': axis_operations(matrix.var),
              'standard deviation': axis_operations(matrix.std),
              'max': axis_operations(matrix.max),
              'min': axis_operations(matrix.min),
              'sum': axis_operations(matrix.sum)}
    return result

def axis_operations(func):
    results = [func(axis=0).tolist(), func(axis=1).tolist(), func().item() ]
    return results
