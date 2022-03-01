from tkinter import *


def input1(event):
    text = event.widget.cget("text")
    # print(text)

    if text == "=":
        try:
            result = eval(str(value.get()))
            value.set(result)
        except Exception as e:
            value.set("Error")
            print("error", e)
           
    elif text == "DEL":
        try:
            fullstring = value.get()
            newstring = fullstring.replace(fullstring[-1], "")
            value.set(newstring)

            # print(newstring)
            entry1.update()
        except Exception as e:
            print(e)

    elif text == "C":
        value.set("")
        entry1.update()
    else:
        value.set(value.get() + text)
        entry1.update()
        # print(value.get())

bgcolor = "#79C9D4" 

root = Tk()
root.geometry("430x400")
root.title("Simple Calculator")
root.configure(bg=bgcolor)
root.iconbitmap("icon\calc.ico")
root.resizable(False, False)


value = StringVar()
entryframe = Frame(root, borderwidth=3, relief=SUNKEN)
entry1 = Entry(entryframe, font="Calculator 30 bold", textvariable=value, bg="#170D0D", fg="#16C12D")
entry1.pack()
entryframe.pack(pady=20, padx=5)

buttonframe = Frame(root, )

list1 = ["9", "8", "7", "C", "6", "5", "4", "/", "3", "2", "1", "*", "00", "0", ".", "-", "%", "DEL", "=", "+"]
i = 0
for n in list1:
    if n == "1" or n == "2" or n == "3" or n == "4" or n == "5" or n == "6" or n == "7" or n == "8" or n == "9": 
        button1 = Button(buttonframe, text=n, font="lucida 20 ", padx=35, width=1, bg="#DAF7A6" )
        button1.grid(row=int(i / 4), column=i % 4)
        i = i + 1
        button1.bind("<Button-1>", input1)
    elif n == "00" or n == "0" or n == ".":
        button1 = Button(buttonframe, text=n, font="lucida 20 ", padx=35, width=1, bg="#FFC300" )
        button1.grid(row=int(i / 4), column=i % 4)
        i = i + 1
        button1.bind("<Button-1>", input1)
    elif n == "+" or n == "-" or n == "*" or n == "/" or n == "%" or n == "=":
        button1 = Button(buttonframe, text=n, font="lucida 20 ", padx=35, width=1, bg="#FF5733" )
        button1.grid(row=int(i / 4), column=i % 4)
        i = i + 1
        button1.bind("<Button-1>", input1)
    else:
        button1 = Button(buttonframe, text=n, font="lucida 20 ", padx=35, width=1, bg="#900C3F" )
        button1.grid(row=int(i / 4), column=i % 4)
        i = i + 1
        button1.bind("<Button-1>", input1)


buttonframe.pack()

text = Label(root, text= "        by Soumyajit Banik", bg=bgcolor) ##758D8C
text.pack(side=LEFT)


root.mainloop()