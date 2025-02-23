# git cheat sheet

## rename branch
```
git branch -m new-branch-name
git branch -m old-branch-name new-branch-name
```

### example:
```
// If you're on 'feature/old-name' and want to rename it
git branch -m feature/new-name

// If you're on 'main' and want to rename 'feature/old-name'
git branch -m feature/old-name feature/new-name
```