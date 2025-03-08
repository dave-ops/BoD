# capture output from a command

```
@echo off
setlocal EnableDelayedExpansion

REM Method 1: Using FOR loop to capture command output
for /f "tokens=*" %%a in ('npm version patch') do (
    set "result=%%a"
)

REM Display the captured result
echo The captured output is: %result%

REM Method 2: Alternative using a temporary variable
set "command_output="
for /f "delims=" %%i in ('ipconfig') do (
    set "command_output=!command_output! %%i"
)

REM Display the second captured result
echo IPConfig output: %command_output%

endlocal
pause
```