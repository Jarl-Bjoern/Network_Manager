# -*- coding: utf-8 -*-
# Rainer C. B. Herold
# Version 0.1 02.01.2021
# Version 1.0 04.01.2021
# Version 1.1 24.01.2021
# Version 1.2 12.09.2022

try:
    from os import getcwd, name as osname
    from os.path import join
    from re import findall, split as rsplit
    from subprocess import getoutput, PIPE, run, Popen
    from time import sleep
    from tkinter import END as tkEND, Frame, Label, Listbox, messagebox, Tk
    from tkinter.ttk import Button, Style
    if (osname == 'nt'):
        from win32api import GetSystemMetrics
        from win32con import SW_HIDE, WM_CLOSE
        from win32console import GetConsoleWindow
        from win32gui import PostMessage, ShowWindow
except ModuleNotFoundError as e: input("The module {e} was not found.\n\nPlease enter with return")