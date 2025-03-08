@echo off
setlocal EnableDelayedExpansion

REM Original string
set "mystring=Hello World"

REM Replace a letter (e.g., replace 'l' with 'x')
set "modified=%mystring:l=x%"
echo Original: %mystring%
echo Replaced 'l' with 'x': %modified%

REM Remove the first letter
set "no_first_letter=%mystring:~1%"
echo Without first letter: %no_first_letter%

REM Remove first letter and keep specific length (e.g., 4 characters after skipping 1)
set "substring=%mystring:~1,4%"
echo First letter removed, next 4 chars: %substring%

endlocal
pause