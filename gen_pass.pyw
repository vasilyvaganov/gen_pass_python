import wx
import wx.adv
import random
import pyperclip
import webbrowser
from winreg import *
import locale
import os
import ctypes
import configparser
config = configparser.ConfigParser()

def createConfig(path):
    try:                                            # file search
        file = open('settings.ini')
    except IOError as e:                            # creates a new one if there is no file
        config.add_section("settings")
        config.set("settings", "warning", "0")

        with open(path, "w") as config_file:
            config.write(config_file)
    else:
        with file:
            pass

if __name__ == "__main__":
    path = "settings.ini"
    createConfig(path)

if not os.path.exists(path):
        createConfig(path)


#region tray_program()
TRAY_TOOLTIP = 'Gen Pass' 
aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize")
keyname = EnumValue(aKey, 2)
print(keyname[1])
if keyname[1] == 1:
    TRAY_ICON = 'resourses/ico_dark.png' 
elif keyname[1] == 0:
    TRAY_ICON = "resourses/ico_white.png"
lang = locale.getdefaultlocale()[0][:2]
if lang == "ru":
    exit_1 = "Закрыть"
    open_file_1 = "Открыть файл gen_pass.txt"
    open_command_1 = "Открыть основную утилиту"
    warning_1 = "Отсутствует файл gen_pass.exe"
    warning_2 = "Внимание!"
    warning_3 = "Все пароли сохраняются в документ под названием gen_pass.txt только локально для вашего удобства и никуда не отправляются!"
elif lang == "en" or lang != "en" and lang!= "ru":
    exit_1= "Exit"
    open_file_1 = "Open file gen_pass.txt"
    open_command_1 = "Open the main utility"
    warning_1 = "File missing gen_pass.exe"
    warning_2 = "Attention!"
    warning_3 = "All passwords are saved in a document called gen_pass.txt only locally for your convenience and are not sent anywhere!"

def warning():
    ctypes.windll.user32.MessageBoxW(0, warning_3, warning_2, 16)

def start():
    path = "settings.ini"
    config.read('settings.ini')
    warningv = config['settings']['warning']
    if warningv == "0" and lang == "ru":
        config.set("settings", "warning", "1")
        with open(path, "w") as config_file:
            config.write(config_file)
            warning()
    if warningv == "0" and lang == "en":
        config.set("settings", "warning", "1")
        with open(path, "w") as config_file:
            config.write(config_file)
            warning()
    elif warningv == "1" and lang == "ru" or lang == "en":
        pass
start()

def gen_pass_for_tray():

    path = 'gen_pass.txt'
    Big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    Low = 'qwertyuiopasdfghjklzxcvbnm'
    Num = '1234567890'
    Spe = '!@#$%^&amp;*()'
    BI = True
    LO = True
    NU = True
    PS = True
    Password_len = 10
    Password_cou = 1
    print('\n')
    Pass_Symbol = []
    if BI == True:
        Pass_Symbol.extend(list(Big))
    if LO == True:
        Pass_Symbol.extend(list(Low))
    if NU == True:
        Pass_Symbol.extend(list(Num))
    if PS == True:
        Pass_Symbol.extend(list(Spe))
    random.shuffle(Pass_Symbol)
    psw = []
    for yx in range(Password_cou):
        psw.append(''.join([random.choice(Pass_Symbol)
                   for x in range(Password_len)]))
    print('\n'.join(psw))
    print('\n')
    pyperclip.copy('\n'.join(psw))
    
    file = open(path, "a")
    file.write('\n')
    file.write('\n'.join(psw))
    file.write('\n')
    file.close()

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, open_file_1, self.on_hello)
        create_menu_item(menu, open_command_1, self.on_hello1)
        menu.AppendSeparator()
        create_menu_item(menu, exit_1, self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon(path)
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):      
        gen_pass_for_tray()

    def on_hello(self, event):
                open("gen_pass.txt", "a")
                webbrowser.open("gen_pass.txt")

    def on_hello1(self, event):
        try:                                            # file search
                        os.startfile("utility.exe")
        except IOError as e:                            # creates a new one if there is no file
            ctypes.windll.user32.MessageBoxW(0, warning_1, warning_2, 16)
            pass
    
    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        self.frame.Close()

class App(wx.App):
    def OnInit(self):
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True

def main():
    app = App(False)
    app.MainLoop()


if __name__ == '__main__':
    main()
#endregion tray_program()
