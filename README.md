# Size Sorting

This is a method to help developers quickly sort lists with adaptability for better efficiency.

## Implementation Approach f(list)
1. Input list
2. Select average value, divide into two lists: one large, one small
3. If one of the lists is empty, output
4. Output: Concatenate the three lists. If one does not contain 1-2 values, recurse

## Testing(8GB)
| Size   | log10(n) | Time |
|--------|----------|------|
| 5000   | 2        | 0.013|
| 100000 | 2        | 0.15 |
| 1999999| 2        | 4.18 |
