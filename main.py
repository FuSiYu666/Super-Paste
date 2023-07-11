import pyperclip
import pyautogui
import keyboard
import time

print("按下上键，五秒后将开始强力复制")


def simulate_keyboard_output(text):
    lines = text.split('\n')  # 按行分割代码文本
    for line in lines:
        stripped_line = line.strip()  # 去除首尾空格
        pyautogui.typewrite(stripped_line)  # 模拟键盘输出去除空格后的代码
        pyautogui.press("enter")  # 模拟键盘按下回车键
        time.sleep(0.1)  # 停留0.1秒

def on_keypress(event):
    if event.name == "up":  # 按下上键
        print("五秒后将开始强力复制")
        time.sleep(5)  # 等待5秒
        clipboard_text = pyperclip.paste()  # 获取剪贴板文本
        simulate_keyboard_output(clipboard_text)  # 模拟键盘输出剪贴板文本

keyboard.on_press(on_keypress)  # 监听键盘事件

keyboard.wait()  # 持续监听键盘事件


