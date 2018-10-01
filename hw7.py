import numpy as np
from scipy.optimize import minimize

# 1
Z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
r = []
for i in range(len(Z)-3):
    r.append([Z[i], Z[i + 1], Z[i + 2], Z[i + 3]])
    i += 1
print(r)

# 2
C = [[1, 0, 0],[1, 0, 0]]
rank = np.linalg.matrix_rank(C)


# 3
def f(x):
    return x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]
def cons1(x):
    return x[0]*x[1]*x[2]*x[3]-30
def cons2(x):
    sum_sq = 60
    for i in range(4):
        sum_sq = sum_sq-x[i]**2
    return sum_sq

bound = (2.0, 6.0)
bnds = (bound, bound, bound, bound)
con1 = {'type': 'ineq', 'fun': cons1}
con2 = {'type': 'eq', 'fun': cons2}
cons = [con1, con2]

solution = minimize(f, [1, 5, 5, 1], method='SLSQP', bounds=bnds, constraints=cons)
print(solution)
