# Arrays

+ [Squares of sorted array](#squares-of-sorted-array)
+ [Merge two sorted arrays](#merge-two-sorted-arrays)
+ [Diagonal sum](#diagonal-sum)
+ [Compress](#compress)

## Sqares of sorted array

```python
def squares(s):
    result = []
    neg = []
    pos = []
    i = 0
    while i <= len(s) - 1 and s[i] <= 0:
        neg.append(s[i]**2)
        i += 1
    while i <= len(s) - 1:
        pos.append(s[i]**2)
        i += 1
    return merge(neg[::-1], pos)
```

## Merge two sorted arrays

```python
def merge(first, second):
    result = []
    while first and second:
        if first[0] > second[0]:
            result.append(second.pop(0))
        else:
            result.append(first.pop(0))
    result.extend(first or second)
    return result
```
## Diagonal sum

```python
def diagonalSum(mat):
    result = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == j or i == len(mat[0]) - 1 - j:
                result += mat[i][j]
    return result
```
## Compress
```python
def compress(chrs):
    res = ""
    i, j = 0, 0
    while i < len(chrs):
        count = 0
        while j < len(chrs) and chrs[i] == chrs[j]:
            count += 1
            j += 1
        if count > 1:
            res += str(chrs[i])+str(count)
        else:
            res += str(chrs[i])
        i = j
    return res
```
