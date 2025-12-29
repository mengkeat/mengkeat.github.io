---
title: "Python Walrus Operator (:=)"
description: "Assignment expressions allow you to assign and return a value in the same expression. Super useful in list comprehensions!"
pubDate: 2024-08-23
tags: ["python", "til"]
category: "Python"
---

# Python Walrus Operator (:=)

The walrus operator `:=` allows you to assign and return a value in the same expression. Super useful in list comprehensions and while loops!

## Example

```python
# Before
data = [1, 2, 3, 4, 5]
squared = []
for x in data:
    if x > 2:
        y = x * x
        squared.append(y)

# After with walrus operator
data = [1, 2, 3, 4, 5]
squared = [y for x in data if (y := x * x) > 4]
```

This makes code more concise and readable!
