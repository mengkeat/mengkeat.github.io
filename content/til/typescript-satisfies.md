---
title: "TypeScript 'satisfies' Operator"
description: "The satisfies operator ensures type safety while preserving the exact type. Better than type assertions because it catches errors at compile time!"
pubDate: 2024-08-21
tags: ["typescript", "til"]
category: "TypeScript"
---

# TypeScript 'satisfies' Operator

The `satisfies` operator ensures type safety while preserving the exact type. Better than type assertions because it catches errors at compile time!

## Example

```typescript
// Using satisfies
const config = {
  apiUrl: "https://api.example.com",
  timeout: 5000,
} satisfies {
  apiUrl: string;
  timeout: number;
};

// config still has exact types, not just the interface
config.timeout = 10000; // This works!
```

This gives you both type safety and type inference!
