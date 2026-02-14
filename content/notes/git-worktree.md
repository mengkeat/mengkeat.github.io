---
title: "Git Worktree for Multiple Branches"
description: "git worktree lets you check out multiple branches simultaneously in different directories. Perfect for comparing code or working on multiple features!"
pubDate: 2024-08-22
tags: ["git", "til"]
category: "Git"
---

# Git Worktree for Multiple Branches

`git worktree` lets you check out multiple branches simultaneously in different directories. Perfect for comparing code or working on multiple features!

## Basic Usage

```bash
# Create a new worktree for a branch
git worktree add ../feature-branch feature-branch

# List all worktrees
git worktree list

# Remove a worktree
git worktree remove ../feature-branch
```

This is a game-changer for working on multiple features at once!
