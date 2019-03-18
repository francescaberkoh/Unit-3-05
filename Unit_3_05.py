'''
Created on Mar 17, 2019
Created for: ICS3U
@author: Francesca Berkoh
This program displays the factorial of a number
'''
#open window
from tkinter import *

root = Tk()


#Create widgets
Label1 = Label(root, text="Enter an integer higher than 0:")
Label1.pack()

TextBox = Entry(root)
TextBox.pack()


#Create a function that when called calculates the factorial
def calculate():
    userinput = TextBox.get()
    user_num = int(userinput)
    count = 1
    value = 1
    while count <= user_num:
        value = count * value
        count = count + 1
    result = Label(text = "Factorial:" + " "+ str(value))
    result.pack()

#This button will kickloff the command
ClickMe = Button(root, text="ClickMe", command=calculate)

ClickMe.pack()        

#Kickoff the code
root.mainloop()