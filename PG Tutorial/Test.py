#matrix multiplication

def multiply_m(a,b):
    arows, acols = len(a), len(a[0])
    brows, bcols = len(b), len(b[0])

    result = [[j for j in range(bcols)]for i in range(arows)]

    if acols == brows:
        for i in range(arows):
            for j in range(bcols):
                for k in range(brows):
                    result[i][j] += a[i][k] * b[k][j]

    else:
        return "error"

    return result
    

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[1],
     [2],
     [3]]

print(multiply_m(A,B))



result = [[sum(a * b for a, b in zip(A_row, B_col)) 
                        for B_col in zip(*B)]
                                for A_row in A]
 
for r in result:
    print(r)