from tkinter import *

s = "Result:\nLoop1: "
for i in (1, 2, 3, 4):
    s = s + str(i) + " "

s += "\nLoop2: "
for i in (1, '2', 3.09, True, None):
    s = s + str(i) + " "

s += "\nLoop3: "
x = (1, 2, 3, 4)
for i in x:
    s = s + str(i) + " "

s += "\nLoop4: "
x = "Python"
for i in x :
    s = s + str(i) * 2 + " "

s += "\nLoop5: "
x = "Python"
j = 1
for i in x:
    s = s + str(i * j) + "\n"
    j = j + 1

s += "\nLoop6: "
for i in ['P', 'y', 't', 'h', 'o', 'n'] :
    s = s + str(ord(i)) + " "
s += "\nLoop7: "

x = ['Apple', 15, True, 3.15]
for i in x:
    s = s + str(i) + " "

s += "\nLoop8: "
x = []
for i in (4, 5, 6, 7):
    x.append(i)
s += str(x)

s += "\nLoop9: "
for i in (66, 67, 68, 69, 70, 71):
    s = s + chr(i)

# Message Box Code#######

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()