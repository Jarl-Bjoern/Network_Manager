# -*- coding: utf-8 -*-
# Rainer C. B. Herold
# Version 0.1 02.01.2021
# Version 1.0 04.01.2021
# Version 1.1 24.01.2021
# Version 1.2 12.09.2022

# Modules
from HF import *

# Variables
if (osname == 'nt'):
    X,Y = GetSystemMetrics(0), GetSystemMetrics(1)
    Position_X, Position_Y = int((X - 800) / 2), int((Y - 600) / 2)
    ID_CMD = GetConsoleWindow()
Program_Close = False

# Arrays
Array_NICS, Array_Status = [], []

# Windows_CMD_Hide
if (osname == 'nt'): ShowWindow(ID_CMD, SW_HIDE)

# Functions
def Program_Destroy():
    global Program_Close

    Program_Close = True
    try: PostMessage(ID_CMD, WM_CLOSE, 0, 0)
    except: pass

# GUI
def GUI():
    # GUI_MainWindow
    mainWindow = Tk(className=" N E T Z W E R K - M A N A G E R")
    mainWindow.geometry(f"800x600+{str(Position_X)}+{str(Position_Y)}")
    mainWindow.configure(bg='Black')
    mainWindow.resizable(False, False)
    mainWindow.iconbitmap(join(getcwd(), 'icon_NM.ico'))

    # Style
    Design = Style()
    Design.theme_use('clam')
    Design.configure('btn.TButton', font=('Arial', 13), background='Black', foreground='Turquoise', borderwidth=1, bordercolor='Black')
    Design.map('btn.TButton', background=[('active', 'Black')], foreground=[('active', 'LightBlue')])

    # Frames
    Frame_Head = Frame(mainWindow, bg='Gray', borderwidth=2)
    Frame_Head.place(relx=-0.5, rely=0.01)
    Frame_Rahmen = Frame(mainWindow, bg='Gray', borderwidth=2, padx=8600)
    Frame_Rahmen.place(relx=0.5, rely=0.96, anchor='center')
    Frame_Bottom = Frame(Frame_Rahmen, bg='Black', borderwidth=1, padx=8600)
    Frame_Bottom.pack()

    # Empty_Fields
    Label_BD1 = Label(Frame_Bottom, text=" ", bg='Black').grid(row=0, column=2)
    Label_BD2 = Label(Frame_Bottom, text=" ", bg='Black', padx=251).grid(row=0, column=4)
    Label_BD3 = Label(Frame_Bottom, text="  ", bg='Black').grid(row=0, column=6)

    # Header
    Label_Design = Label(Frame_Head, text=" ", bg='Black', padx=800, pady=5, borderwidth=5).grid(row=0, column=0)
    Label_Head = Label(Frame_Head, text="N E T Z W E R K - M A N A G E R  ", bg='Black')
    Label_Head.configure(font=('Arial', 15), foreground='Turquoise')
    Label_Head.grid(row=0, column=0)

    # Frames
    Frame_Mid = Frame(mainWindow, bg='Black', borderwidth=2)
    Frame_Mid.place(relx=0.008, rely=0.1)
    Frame_Mid_Correct = Frame(mainWindow)
    Frame_Mid_Correct.place(relx=0.5015, rely=0.103)
    Frame_btn_Restart = Frame(mainWindow, bg='Gray', borderwidth=1)
    Frame_btn_Restart.place(relx=0.13, rely=0.835)
    Frame_btn_Deactivate = Frame(mainWindow, bg='Gray', borderwidth=1)
    Frame_btn_Deactivate.place(relx=0.435, rely=0.835)
    Frame_btn_Activate = Frame(mainWindow, bg='Gray', borderwidth=1)
    Frame_btn_Activate.place(relx=0.77, rely=0.835)

    # Listboxes
    lb_Head_Adapter = Listbox(Frame_Mid, bg='Black', fg='Turquoise', width=43, height=1, selectbackground='Black', selectforeground='Turquoise', activestyle='none')
    lb_Head_Adapter.configure(justify='center', font=('Arial', 13))
    lb_Head_Adapter.grid(row=0, column=0, ipadx=1)
    lb_Head_Status = Listbox(Frame_Mid_Correct, bg='Black', fg='Turquoise', width=43, height=1, selectbackground='Black', selectforeground='Turquoise', activestyle='none')
    lb_Head_Status.configure(justify='center', font=('Arial', 13))
    lb_Head_Status.grid(row=0, column=0, ipadx=1)
    lb_NICS = Listbox(Frame_Mid, bg='Black', fg='Purple', width=64, selectbackground='Black', selectforeground='Yellow', activestyle='none')
    lb_NICS.grid(row=1, column=0, ipady=115, ipadx=3)
    lb_Status = Listbox(Frame_Mid, bg='Black', fg='Purple', width=64, selectbackground='Black', selectforeground='Purple', activestyle='none')
    lb_Status.grid(row=1, column=1, ipady=115, ipadx=2)

    # Listbox_Header
    lb_Head_Adapter.insert(0, "Uebersicht aller Netzwerkadapter")
    lb_Head_Status.insert(0, "Status")

    if (osname == 'nt'):
        Network_Overview = getoutput('netsh interface show interface')
        Search_Values = rsplit("Deaktiviert|Aktiviert|Verbunden|Dediziert|\n|Getrennt|Verw.|Status|Schnittstellenname|status|Typ|\n", Network_Overview)
    else: pass
        #Network_Overview = getoutput('ip address')
        #Search_Values = rsplit("Deaktiviert|Aktiviert|Verbunden|Dediziert|\n|Getrennt|Verw.|Status|Schnittstellenname|status|Typ|\n", Network_Overview)

    Name = ""
    for i in Search_Values:
        Filter_Search = findall("[a-z A-Z 0-9 -]", str(i))
        for k in Filter_Search:
            Name += k

        if (Name != ""):
            for l in Name:
                if (l.isupper() or l.islower()):
                    if (Name[8:] not in Array_NICS):
                        Array_NICS.append(Name[8:])
        Name = ""

    for i in Array_NICS:
        lb_NICS.insert(len(Array_NICS), i)

    # Functions
    def Search(State):
        global Array_Status
    
        if (osname == 'nt'):
            Status_Overview = getoutput('netsh interface show interface')
            Status_NICS = findall('Verbunden|Getrennt', Status_Overview)
            Status_NICS_Two = findall('Aktiviert|Deaktiviert', Status_Overview)
        else: pass
            #Status_Overview = getoutput('netsh interface show interface')
            #Status_NICS = findall('Verbunden|Getrennt', Status_Overview)
            #Status_NICS_Two = findall('Aktiviert|Deaktiviert', Status_Overview)
    
        if (State != False):
            while True:
                n = 0
                if (osname == 'nt'): 
                    Test = str(run(['ping', '-n', '3', '8.8.8.8'], stdout=PIPE).stdout).splitlines()
                else: pass
                for i in Test:
                    for j in i.split(' '):
                        if ('TTL' in j): n += 1
                if (n == 3): break
                else: sleep(0.25)

        n = 0
        for i in Status_NICS:
            if (i == 'Verbunden'): Array_Status.append(f'{i}                                                                                        {Status_NICS_Two[n]}')
            else: Array_Status.append(f'{i}                                                                                            {Status_NICS_Two[n]}')
            n += 1

    def Network_Status(State, seconds):
        Array_Status.clear()
        sleep(seconds)
        lb_Status.delete(0, tkEND)
        Search(State)

        for i in Array_Status:
            lb_Status.insert(len(Array_Status), f'  {i}')

    def Operation(Adapter, Status, seconds):
        try:
            if (Status == False):
                if (osname == 'nt'): run(['netsh', 'interface', 'set', 'interface', lb_NICS.get(lb_NICS.curselection()), 'disable'], stderr=PIPE)
                else: run(['ifdown', lb_NICS.get(lb_NICS.curselection())], stderr=PIPE)
            else:
                if (osname == 'nt'): run(['netsh', 'interface', 'set', 'interface', lb_NICS.get(lb_NICS.curselection()), 'enable'], stderr=PIPE)
                else: run(['ifup', lb_NICS.get(lb_NICS.curselection())], stderr=PIPE)
        except: messagebox.showerror("Fehler", "Es wurde kein Netzwerkadapter ausgewaehlt!")
        Network_Status(Status, seconds), mainWindow.update()

    def Restart_click():
        Operation(lb_NICS.get(lb_NICS.curselection()),False,0), Operation(lb_NICS.get(lb_NICS.curselection()),True,3)

    def Deactivate_click():
        Operation(lb_NICS.get(lb_NICS.curselection()),False,0)

    def Activate_click():
        Operation(lb_NICS.get(lb_NICS.curselection()),True,0.25)

    # Aufruf_Bereich
    Network_Status(False, 0)

    # Wichtige_Steuerelemente
    btn_Restart = Button(Frame_btn_Restart, text='  Neustart  ', style='btn.TButton', command=Restart_click).grid(row=0, column=0)
    btn_Deactivate = Button(Frame_btn_Deactivate, text='  Deaktivieren  ', style='btn.TButton', command=Deactivate_click).grid(row=0, column=0)
    btn_Activate = Button(Frame_btn_Activate, text='  Aktivieren  ', style='btn.TButton', command=Activate_click).grid(row=0, column=0)

    # Entwickler_Bereich
    Label_Programmer = Label(Frame_Bottom, text="Bjoern Herold", bg='Black')
    Label_Programmer.configure(font=('Arial', 15), foreground='Turquoise')
    Label_Programmer.grid(row=0, column=1)
    Label_Version = Label(Frame_Bottom, text="Version 1.2", bg='Black')
    Label_Version.configure(font=('Arial', 15), foreground='Turquoise')
    Label_Version.grid(row=0, column=7)

    mainWindow.protocol("WM_DELETE_WINDOW", Program_Destroy)
    mainWindow.mainloop()
