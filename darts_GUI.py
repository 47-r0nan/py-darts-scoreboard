from tkinter import *
from tkinter import messagebox
from player import Player

window = Tk()
window.geometry("270x315")
window.title("Darts")
border_color = Frame(window, background="black")


# Methods

def display(index):
    global current
    global player
    player = teamlist[index]
    current = index
    nameentry.delete(0, END)
    nameentry.insert(END, player.getName())
    scoreentry.delete(0, END)
    scoreentry.insert(END, player.getScore())
    turnentry.delete(0, END)
    turnentry.insert(END, player.getTurn())
    dartentry1.delete(0, END)
    dartentry1.insert(END, player.getDart1())
    dartentry2.delete(0, END)
    dartentry2.insert(END, player.getDart2())
    dartentry3.delete(0, END)
    dartentry3.insert(END, player.getDart3())


def recordThrows():
    dart1 = int(dartentry1.get())
    dart2 = int(dartentry2.get())
    dart3 = int(dartentry3.get())
    score = int(scoreentry.get())
    if dartLimit(dart1, dart2, dart3):
        changeScore(dart1, dart2, dart3, score)
    else:
        messagebox.showerror("Warning", "You have entered an invalid dart score.")


def dartLimit(dart1, dart2, dart3):
    if dart1 < 0 or dart2 < 0 or dart3 < 0:
        return False
    elif dart1 > 60 or dart2 > 60 or dart3 > 60:
        return False
    else:
        return True


def writeScore(score):
    player.recordDarts(score)
    if player.getScore() == 0:
        answer = messagebox.askyesno("Results", player.getName() + " wins!!\nWould you like to play again?")
        if answer:
            reset()
        else:
            escape()
    display(current)


def changeScore(dart1, dart2, dart3, score):
    throws = [dart1, dart2, dart3]
    for x in throws:
        if x <= score:
            score -= x
        else:
            break
    player.updateName(nameentry.get())
    writeScore(score)
    nextPlayer()


def nextPlayer():
    global current
    player.updateName(nameentry.get())
    if current < 1:
        current += 1
    else:
        current -= 1
    display(current)


def reset():
    player.resetAll()
    clearData()
    display(0)


def clearData():
    nameentry.delete(0, END)
    scoreentry.delete(0, END)
    turnentry.delete(0, END)
    dartentry1.delete(0, END)
    dartentry2.delete(0, END)
    dartentry3.delete(0, END)


def showInfo():
    messagebox.showinfo("Info", "Use this scoreboard app to keep track of your darts scores.\n\n"
                                "Just enter each dart scores and watch your score deplete.\n\n"
                                "Get your starting score from 501 down to 0.\n\n"
                                "Press the \"Change Player\" button to check the other player\'s score.\n\n"
                                "Press the \"Record Throws\" button to record all your dart scores.\n\n"
                                "60 is the max you can get with each dart.\n\n"
                                "You need to score down to exactly 0 to win.\n\n"
                                "Have fun!!")


def escape():
    answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if answer:
        window.destroy()


# Player choice
team1 = Player("Player1")
team2 = Player("Player2")

teamlist = [team1, team2]
global current  # current player
global player
player = teamlist[0]  # initialize to first player

# Menu
menu1 = Menu(window)  # MenuBar
window.config(menu=menu1)
subm1 = Menu(menu1)  # Menu
menu1.add_cascade(label="Help", menu=subm1)
subm1.add_command(label="Restart Game", command=reset)
subm1.add_command(label="Info", command=showInfo)
subm1.add_command(label="Exit", command=escape)


# GUI

frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)

title = Label(window, text="Darts ScoreBoard", fg="red", bg="green", font=("arial", 16, "bold"))
title.place(x=45, y=30)

namelabel = Label(frame, text="Player Name", fg="white", bg="black", width=15, font=("arial", 10, "bold"))  #
namelabel.grid(row=0, column=0, sticky=W + E)

nameentry = Entry(frame)
nameentry.insert(END, '0')
nameentry.grid(row=0, column=1, sticky=W + E)

scorelabel = Label(frame, text="Player Score", fg="black", bg="white", width=15, font=("arial", 10, "bold"))  #
scorelabel.grid(row=1, column=0, sticky=W + E)

scoreentry = Entry(frame)
scoreentry.insert(END, '501')
scoreentry.grid(row=1, column=1, sticky=W + E)

turnlabel = Label(frame, text="Turn", fg="white", bg="black", width=15, font=("arial", 10, "bold"))  #
turnlabel.grid(row=2, column=0, sticky=W + E)

turnentry = Entry(frame)
turnentry.insert(END, '0')
turnentry.grid(row=2, column=1, sticky=W + E)

playerbutton = Button(frame, text="Change Player", fg="black", font=("arial", 10, "bold"), command=nextPlayer)
playerbutton.grid(row=3, column=0, columnspan=2, sticky=W + E)

breakLine = Label(frame, text="", width=15)
breakLine.grid(row=4, column=0, columnspan=2)

dartlabel1 = Label(frame, text="Dart 1", fg="black", bg="white", width=15, font=("arial", 10, "bold"))  #
dartlabel1.grid(row=5, column=0, sticky=W + E)

dartentry1 = Entry(frame)
dartentry1.insert(END, '0')
dartentry1.grid(row=5, column=1, sticky=W + E)

dartlabel2 = Label(frame, text="Dart 2", fg="white", bg="black", width=15, font=("arial", 10, "bold"))  #
dartlabel2.grid(row=6, column=0, sticky=W + E)

dartentry2 = Entry(frame)
dartentry2.insert(END, '0')
dartentry2.grid(row=6, column=1, sticky=W + E)

dartlabel3 = Label(frame, text="Dart 3", fg="black", bg="white", width=15, font=("arial", 10, "bold"))  #
dartlabel3.grid(row=7, column=0, sticky=W + E)

dartentry3 = Entry(frame)
dartentry3.insert(END, '0')
dartentry3.grid(row=7, column=1, sticky=W + E)

throwsbutton = Button(frame, text="Record Throws", fg="black", font=("arial", 10, "bold"), command=recordThrows)
throwsbutton.grid(row=8, column=0, columnspan=2, sticky=W + E)

display(0)

mainloop()
