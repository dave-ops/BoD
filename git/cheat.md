# git cheat sheet

> [home](../README.md)

## get ssh cert
```
ls ~/.ssh
ssh-keygen -t rsa -b 4096 -C "david.moley@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
```

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
set repo_name=grok-desktop
set repo="https://github.com/dave-ops/%repo_name%"
git init
git remote add origin %repo%
git remote set-url origin %repo%
git checkout -b main
git add .
git commit -m "adding init code"
git push origin main --force
git status
git rm -r --cached .
git add .
git commit -m "remove ignored files from repository"
git push origin main
echo done.
```

## cherry-pick
```
git checkout main
git cherry-pick 78f6684f6a6db5307728a0be5166b510499050ff --strategy=recursive -X subtree=src/Decompressors
```

1. cherry-pick by wildcard
```bash
git cherry-pick 2716d264faeadd07f6b40980bbc0eb9cabf8c2fd -- $(git diff-tree --no-commit-id --name-only -r 2716d264faeadd07f6b40980bbc0eb9cabf8c2fd | grep "Decompressor.cs$")
```

### purge files from history by rewriting history
1. 
```bat
set commit=5b095f2294460a09f0549f4449c13a3335debb85
set wildcard="Decompressor.cs$"
for /f "tokens=*" %i in ('git diff-tree --no-commit-id --name-only -r %commit% | findstr %wildcard%') do git cherry-pick %commit% -- %i
```
2. git-filter (untested)
```sh
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch appsettings.json" --prune-empty --tag-name-filter cat -- --all
```