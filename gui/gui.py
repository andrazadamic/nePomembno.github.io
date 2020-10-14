from tkinter import *
from tkinter import ttk

dataList = [(1,'Raj','Mumbai',19),
        (2,'Aaryan','Pune',18),
        (3,'Vaishnavi','Mumbai',20),
        (4,'Rachna','Mumbai',21),
        (5,'Shubham','Delhi',21),
        (1, 'Raj', 'Mumbai', 19),
        (2, 'Aaryan', 'Pune', 18),
        (3, 'Vaishnavi', 'Mumbai', 20),
        (4, 'Rachna', 'Mumbai', 21),
        (5, 'Shubham', 'Delhi', 21),
        (1, 'Raj', 'Mumbai', 19),
        (2, 'Aaryan', 'Pune', 18),
        (3, 'Vaishnavi', 'Mumbai', 20),
        (4, 'Rachna', 'Mumbai', 21),
        (5, 'Shubham', 'Delhi', 21)]
total_rows = len(dataList)
total_columns = len(dataList[0])
class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.line = Entry(tableFrame, width=10, fg='#0C0C0C', font=('Roboto',12))
                self.line.grid(row=i, column=j)
                self.line.insert(END, dataList[i][j])

root = Tk()
#root.geometry("600x400")

root.title("Neco's Password Manager")

#definiran osnovni okvir
mainFrame = ttk.Frame(root, padding="10 10 10 10")
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#okvir tabele in tabela
tableFrame = ttk.Frame(mainFrame, padding="5 5 5 5")
tableFrame.grid(column=1, row=1, sticky=(N, E), rowspan=10)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainTable = Table(tableFrame)

#okvir nastavitveBrowserja
browserFrame = ttk.Frame(mainFrame, padding="5 5 5 5")
browserFrame.grid(column=2, row=1, rowspan=2, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#okvir passwordGenerator
passwordFrame = ttk.Frame(mainFrame, padding="5 5 5 5")
passwordFrame.grid(column=2, row=3, rowspan=2, sticky=(N, W, E, S))

#okvir miscSettings
miscFrame = ttk.Frame(mainFrame, padding="5 5 5 5")
miscFrame.grid(column=2, row=5, rowspan=6, sticky=(S, E))

browserLabel = ttk.Label(browserFrame, text="Selected browser: ").grid(column=1, row=1, sticky=N)
browserEntry = ttk.Entry(browserFrame, width=5, font=('Roboto', 12)).grid(column=2, row=1, sticky=(W, E))
browserButton = ttk.Button(browserFrame, text="Change browser").grid(column=2, row=2, sticky=S)

passwordLabel = ttk.Label(passwordFrame, text="Password Generator").grid(column=1, row=1)
passwordButtonGenerate = ttk.Button(passwordFrame, text="Generate password").grid(column=1, row=3, sticky=W)
passwordButtonPreferences = ttk.Button(passwordFrame, text="Preferences").grid(column=2, row=3, sticky=E)

mainAdd = ttk.Button(mainFrame, text="Add...").grid(column=1, row=11, sticky=W)
mainRemove = ttk.Button(mainFrame, text="Remove").grid(column=1, row=11, sticky=E)

miscWebsite = ttk.Button(miscFrame, text="Visit our website").grid(column=1, row=2, sticky=(W, E))
miscUpdate = ttk.Button(miscFrame, text="Check for updates").grid(column=1, row=3, sticky=(W, E))
miscBug = ttk.Button(miscFrame, text="Report a bug").grid(column=1, row=4, sticky=(W, E))
miscTheme = ttk.Button(miscFrame, text="Switch the theme").grid(column=1, row=5, sticky=(W, E))

authorLabel= ttk.Label(mainFrame, text="Created by Nemanja Raduljica").grid(column=2, row=13, sticky=E)
root.mainloop()