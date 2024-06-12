import socket
from tkinter import *
from  threading import Thread
import random
from PIL import ImageTk, Image
import platform

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None
playerName = None

canvas1 = None

nameEntry = None
nameWindow = None

def createTicket():
    global gameWindow
    global ticketGrid

    mainLable = Label(gameWindow,width=85,height=16,borderwidth=5,bg='white')
    mainLable.place(95,110)

    xpos= 105
    ypos= 130
    for row in range(0,3):
        rowlist = []
        for col in range(0,9):
            if(platform.system() == "Darwin"):
                boxButton = Button(gameWindow,
                borderwidth=3,
                pady=23,
                padx=-23,
                bg="yellow",
                highlightbackground="yellow",
                activebackground="green"
                )

                boxButton.place(x=xpos,y=ypos)
            else:
                boxButton = Button(gameWindow,font=("Chalkboard SE",30),width=3,height=2,borderwidth=5,bg='yellow')
                boxButton.place(x=xpos,y=ypos)
            rowlist.append(boxButton)
            xpos += 64
        ticketGrid.append(rowlist)
        xpos = 105
        ypos +=82

def placeNumbers():
    global ticketGrid
    global currentNumberList

    for row in range(0,3):
        randomColList = []
        counter = 0
        while counter<= 4:
            randomCol = random.randint(0,8)
            if(randomCol not in randomColList):
                randomColList.append(randomCol)
                counter +=1

def gameWindow():
    global gameWindow
    global canvas2
    global screen_width
    global screen_height
    global dice
    global winingMessage
    global resetButton
    global flashNumberLabel


    gameWindow = Tk()
    gameWindow.title("Tambola Family Fun")
    gameWindow.geometry('800x600')

    screen_width = gameWindow.winfo_screenwidth()
    screen_height = gameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "C:/Users/iliea/OneDrive/Desktop/Code/Python/Hw/hw205/assets/background.png")

    canvas2 = Canvas( gameWindow, width = 500,height = 500)
    canvas2.pack(fill = "both", expand = True)

    # Display image
    canvas2.create_image( 0, 0, image = bg, anchor = "nw")

    # Add Text
    canvas2.create_text( screen_width/4.5,50, text = "Tambola Family Fun", font=("Chalkboard SE",50), fill="#3e2723")

    createTicket()
    placeNumbers()


    # Flash Number Label
    flashNumberLabel = canvas2.create_text(400,screen_height/2.3, text = "Waiting for other players to join...", font=("Chalkboard SE",30), fill="#3e2723")

    gameWindow.resizable(True, True)
    gameWindow.mainloop()

def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())

    



def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1

    nameWindow  = Tk()
    nameWindow.title("Tambola Family Fun")
    nameWindow.geometry('800x600')


    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/4.5,screen_height/8, text = "Enter Name", font=("Chalkboard SE",60), fill="black")

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 30), bd=5, bg='white')
    nameEntry.place(x = screen_width/7, y=screen_height/5.5 )


    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=11, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/6, y=screen_height/4)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()





def recivedMsg():
    pass


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 6000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    thread = Thread(target=recivedMsg)
    thread.start()

    askPlayerName()


setup()
