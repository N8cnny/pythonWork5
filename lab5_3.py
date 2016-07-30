import InputBox
from tkinter import *

s = "Result:\nLoop1: "
x = 1  # initial value
while x < 10:  # Boolean expression
    s = s + str(x) + " "
    x += 1  # increment

s += "\nLoop2: "
x = 9  # initial value
while x >= 1:  # Boolean expression
    s = s + str(x) + " "
    x -= 1  # increment

s += "\nLoop3: "
i = 10
f = 1
while i >= 1:
    f = f * i
    i -= 1
s += str(f) + "\n"

s += "\nLoop4: "
x = (23, 17, 22, 8, 10, 19, 5, 43, 28)
low = x[0]
i = 1  # initial value
while i < len(x):
    if x[i] < low:
        low = x[i]
    i += 1  # increment

s += "The smallest value is " + str(low) + "\n"

s += "\nLoop5: "
InputBox.ShowDialog("Are you nuts? [Yes/No]: ")
x = InputBox.GetInput()
while x.upper() != "YES":
    InputBox.ShowDialog("Again, are you nuts? ")
    x = InputBox.GetInput()
s += "Just kidding!! Thank you.\n"

s += "\nLoop6: "
s += " 1 2 3 4 5 6 7 8 9\n"
s += "--------------------\n"
for i in range(1, 10):
    rst = str(i) + "|"
    for j in range(1, 10):
        rst += " " + str(i*j)
    s += rst + "\n"

# Message Box Code#######

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
