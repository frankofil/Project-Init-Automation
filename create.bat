@echo off

set project_name=%1
set flag=%2
cd /d %~dp0

if "%1"=="" (
    echo "Error 01: no repository name"
)  else (
    if "%2"=="-public" (
        python create.py %project_name% %flag%
    ) else (
            python create.py %project_name% 
        )
    )