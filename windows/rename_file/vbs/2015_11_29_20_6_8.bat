rem off the command show
echo off

rem show current direcotry
echo %cd%

rem for /f "tokens=*" %%f in ('dir /b /s /a-d') do echo %%~tf %%f

setlocal enabledelayedexpansion

rem find all jpg file in current path
for %%c in (*.jpg) do (echo %%~tc
rem save every jpg file name and show it
set originalName=%%c
echo !originalName!
rem save the jpg file modify time and show it 
set pictime=%%~tc
set pictime=!pictime:~0,19!
echo !pictime!
rem replace the space and : - to _ character
set pictime=!pictime: =_!
set pictime=!pictime::=_!
set pictime=!pictime:-=_!
rem show the new name and original name
echo after replace special char: !pictime!
echo !originalName!
rem rename the file 
ren "!originalName!"  !pictime!.jpg
)
   
pause