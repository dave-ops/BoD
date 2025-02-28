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
git reset --soft HEAD~1
```

### example:
```
// If you're on 'feature/old-name' and want to rename it
git branch -m feature/new-name

// If you're on 'main' and want to rename 'feature/old-name'
git branch -m feature/old-name feature/new-name
```

## Problem: Accidentally Committed Large File
If you've committed a large file by mistake and are unable to push due to file size limits, follow these steps:
```
pip install git-filter-repo
git filter-repo --invert-paths --path installs/<file>.msi --force
git remote add origin git@github.com:dave-ops/sol-judicator-nextjs.git
```

4. Force Push to Update Remote after cleaning the history:
```bash
git push -f origin init-with-mongodb
```

## connect Repo from CLI
```
set repo="https://github.com/dave-ops/grok-cs"
git remote add origin %repo%
git remote set-url origin %repo%
git checkout -b main
git push origin main --force
git status
```

## remove files after gitignore update
```
git rm -r --cached .
git add .
git commit -m "remove ignored files from repository"
git push origin main
echo done.
```

## undo staged files in a commit
```
git reset --soft HEAD^1
```

## attach a new folder to an existing git repo
```
set repo="https://github.com/dave-ops/grok-cs"
git init
git remote add origin %repo%
git remote set-url origin %repo%
git checkout -b main
git add .
git commit -m "adding init code"
git push origin main --force
git status
```
