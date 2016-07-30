from tkinter import *

s = "Result:\nLoop1: "
for i in range(10):
    s = s + str(i) + " "

s += "\nLoop2: "
x = []
for i in range(0, 10):
    x.append(i/10)
s += str(x)

s += "\nLoop3: "
for i in range(10, 51, 5):
    s = s + str(i) + " "

s += "\nLoop4: "
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
         "Nov", "Dec"]
for m in range(len(month)) :
    s += str(m) + " is the index of " + month[m] + "\n"

s += "\nLoop5: "
for i in range(5, 0, -1):
    s = s + str(i) + " "

s += "\nLoop6: "
for i in range(15, -1, -3):
    s = s + str(i) + " "

s += "\nLoop7: "
x = "Python Programming"
result = ""
for i in range(len(x)-1, -1, -1):
    result = result + x[i]
s += result + "\n"

s += "\nLoop8: "
total = 0
for i in range(10, 0, -1):
    total = total + i
s += str(total) + "\n"

s += "\nLoop9: "
for i in range(0, 11):
    if i % 2 == 0:
        s += str(i) + " is an even number!\n"
    else:
        s += str(i) + " is an odd number!\n"

# Message Box Code#######

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
