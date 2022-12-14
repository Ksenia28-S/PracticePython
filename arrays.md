# Arrays

+ [Squares of sorted array](#squares-of-sorted-array)
+ [Merge two sorted arrays](#merge-two-sorted-arrays)

## Squares of sorted array
Дан отсортированный список в неубавющем порядке. Вернуть элементы этого списка возведенные в квадрат в неубывающем порядке.
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
На входе два отсортированных массива (списка). На выходе получить 1 отсортированный массив.
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
