# TicTacToe for fun

# tkinter module is a standard python interface for Tk GUI Toolkit
from tkinter import *

# Used to display message boxes in our app/code
import tkinter.messagebox
tk = Tk()

#Main Title
tk.title("Tic Tac Toe")

#variable for mouse click
click = True

# function to check the buttons and their respective clicks of 'X' & 'O'
def checker(buttons):
    global click

    # This statement gives us an idea that X's turn is first
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
    # Turn of O is second after X
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True

    # loop of winning possibilities of X
    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
         button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
         button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
         button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
         button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
         button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
         button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
         button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        tkinter.messagebox.showinfo("And the winner is X", "You've just won a game!")

    # loop of winning possibilities of O
    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
         button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
         button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
         button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
         button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
         button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
         button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
         button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        tkinter.messagebox.showinfo("And the winner is O","You've just won a game!")

# Holds the string as a default value
buttons = StringVar()

# Placement of buttons in the GUI with respect to rows and columns as specified
# the lambda function can have any number of arguments but it can handle only a-
# single expression.
button1 = Button(tk,text=" ",font=('Helvetica 24 bold'),height=3,width=6,command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2 = Button(tk,text=" ",font=('Helvetica 24 bold'),height=3,width=6,command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3 = Button(tk,text=" ",font=('Helvetica 24 bold'),height=3,width=6,command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4 = Button(tk,text=" ",font=('Helvetica 24 bold'),height=3,width=6,command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5 = Button(tk,text=" ",font=('Helvetica 24 bold'),height=3,width=6,command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6 = Button(tk,text=" ",font=('Helvetica 24 bold'),height=3,width=6,command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7 = Button(tk,text=" ",font=('Helvetica 24 bold'),height=3,width=6,command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8 = Button(tk,text=" ",font=('Helvetica 24 bold'),height=3,width=6,command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9 = Button(tk,text=" ",font=('Helvetica 24 bold'),height=3,width=6,command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)

# At last call the main loop
tk.mainloop()