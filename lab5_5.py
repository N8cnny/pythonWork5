import InputBox
from tkinter import *

s = "FOR LOOP\n"

InputBox.ShowDialog("Enter your first name: ")
s1 = InputBox.GetInput()

for i in range(len(s1)):
    s += str((i+1) * s1[i]) + "\n"
for i in range(len(s1)):
    s += str((len(s1) - i) * s1[i]) + "\n"
s += "\n\nWHILE LOOP\n"
number = ("Enter your last name: ")
s2 = InputBox.GetInput()

i = 0
while i < len(s2):
    s += str(s2[i] * (i+1)) + "\n"
    i = i + 1

i = 0
while i < len(s2):
    s += str(s2[i] * (len(s2) - i)) + "\n"
    i = i + 1

# Message Box Code#######

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
