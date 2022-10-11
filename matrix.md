# Matrix


## Diagonal sum
Дана квадратная матрица. Вывести сумму элементов на главной и побочной диагоналях.
```python
def diagonalSum(mat):
    result = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == j or i == len(mat[0]) - 1 - j:
                result += mat[i][j]
    return result
```
