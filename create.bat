@echo off

set project_name=%1
set flag=%2

if "%1"=="" (
    echo "error"
)  else (
    if "%2"=="" (
        echo "no parameter"
    ) else (
        echo "parameter %2%"
    )
)