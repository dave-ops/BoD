# git cheat sheet

> [home](../README.md)

## clean
```
git clean -f -x -d
```

## rename branch
```
git branch -m new-branch-name
git branch -m old-branch-name new-branch-name
```

## remove files after gitignore update
```
git rm -r --cached .
git add .
git commit -m "remove ignored files from repository"
git push origin main
echo done.
```

## unstage files post commit pre push
```
git reset --soft HEAD^1
```

### example:
```
// If you're on 'feature/old-name' and want to rename it
git branch -m feature/new-name

// If you're on 'main' and want to rename 'feature/old-name'
git branch -m feature/old-name feature/new-name
```

