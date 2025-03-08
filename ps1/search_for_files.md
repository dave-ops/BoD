# search
```
Get-ChildItem -Recurse -Include *.md | Where-Object { $_.FullName -notlike "*node_modules*" } | Select-String "vm-reverse-proxy-admin"
```