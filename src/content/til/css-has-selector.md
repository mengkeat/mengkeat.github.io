---
title: "CSS :has() Pseudo-class"
description: "The :has() pseudo-class allows you to style an element based on its descendants. It's like 'parent selectors' in CSS!"
pubDate: 2024-08-24
tags: ["css", "web-development"]
category: "CSS"
---

# CSS :has() Pseudo-class

The `:has()` pseudo-class allows you to style an element based on its descendants. It's like "parent selectors" in CSS!

## Example

```css
/* Style a card that contains an image */
.card:has(img) {
  border: 2px solid blue;
}

/* Style a form that has invalid inputs */
form:has(input:invalid) {
  border-color: red;
}
```

This is incredibly powerful for conditional styling!