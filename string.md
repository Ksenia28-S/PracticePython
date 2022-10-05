# String

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
