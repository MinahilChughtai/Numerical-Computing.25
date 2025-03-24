import numpy as np
import pandas as pd

def forward_difference_table(x, y):
    n = len(y)
    table = np.zeros((n, n))
    table[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]
    
    return table

def newtons_forward_interpolation(x, y, x_val):
    n = len(y)
    h = x[1] - x[0]
    p = (x_val - x[0]) / h
    table = forward_difference_table(x, y)
    
    result = y[0]
    fact = 1
    p_term = 1
    
    for i in range(1, n):
        p_term *= (p - (i - 1))
        fact *= i
        result += (p_term * table[0][i]) / fact
    
    return result

def newtons_backward_interpolation(x, y, x_val):
    n = len(y)
    h = x[1] - x[0]
    p = (x_val - x[-1]) / h
    table = forward_difference_table(x, y)
    
    result = y[-1]
    fact = 1
    p_term = 1
    
    for i in range(1, n):
        p_term *= (p + (i - 1))
        fact *= i
        result += (p_term * table[n - i - 1][i]) / fact
    
    return result

# Given Data
years = np.array([2015, 2016, 2017, 2018, 2019])
yields = np.array([3.5, 17, 3.9, 4.1, 4.3])

# Forward Interpolation for 2016.5
estimated_forward = newtons_forward_interpolation(years, yields, 2016.5)

# Backward Interpolation for 2018.5
estimated_backward = newtons_backward_interpolation(years, yields, 2018.5)

# Displaying the results
df_table = pd.DataFrame(forward_difference_table(years, yields))
df_table.columns = [f"Δ^{i}y" for i in range(len(years))]
df_table.index = years

print("Forward Difference Table:")
print(df_table.fillna(''))
print(f"\nEstimated yield for 2016.5 using Forward Interpolation: {estimated_forward:.4f} tons/ha")
print(f"Estimated yield for 2018.5 using Backward Interpolation: {estimated_backward:.4f} tons/ha")
