from tkinter import *

s = "Result:\nLoop1: "
for i in range(1, 10):
    if i == 6:
        break
    else:
        s = s + str(i) + " "

s += "\nLoop2: "
i = 0
while i <= 9:
    if i == 7:
        break
    s = s + str(i) + " "
    i += 1

s += "\nLoop3:\n"
for n in range(2, 11):
    for x in range(2, n):
        if n % x == 0:
            s += str(n) + ' equals ' + str(x) + '*' + str(n/x) + "\n"
            break
    else:  # loop fell through without finding a factor
        s += str(n) + ' is a prime number\n'

s += "\nLoop4: "
i = -1
while i <= 20:
    i = i + 1
    if i % 2 != 0:
        continue
    s = s + str(i) + " "

s += "\nLoop5: "
m = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
     "Dec")
for i in m:
    if i == "May":
        pass
    else:
        s = s + str(i) + " "

# Message Box Code#######

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
