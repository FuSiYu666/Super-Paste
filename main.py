import pyperclip
import pyautogui
import keyboard
import time
import ipaddress

print("����[��]��������󽫿�ʼǿ��ճ��")


def simulate_keyboard_output(text):
    lines = text.split('\n')  # ���зָ�����ı�
    for line in lines:
        stripped_line = line.strip()  # ȥ����β�ո�
        pyautogui.typewrite(stripped_line)  # ģ��������ȥ���ո��Ĵ���
        pyautogui.press("enter")  # ģ����̰��»س���
        time.sleep(0.1)  # ͣ��0.1��

def on_keypress(event):
    if event.name == "up":  # �����ϼ�
        print("����󽫿�ʼǿ��ճ��")
        print(5)
        time.sleep(1)  # ����ʱ
        print(4)
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("����ճ��......")
        clipboard_text = pyperclip.paste()  # ��ȡ�������ı�
        simulate_keyboard_output(clipboard_text)  # ģ���������������ı�
        print("ճ����ɣ�\n \n����[��]��������󽫿�ʼǿ��ճ��")

keyboard.on_press(on_keypress)  # ���������¼�

keyboard.wait()  # �������������¼�


