from tkinter import*

def check_major():
    #print("Name = ",name.get())
    #print("Average = ",average.get())
    #print("Sex = ",gender.get())
    #print("Computer IT = %d,\nComputer MT = %d,\nMath = %d,\nScience = %d" %(it.get(),mt.get(),math.get(),sci.get()))
    name_s.set(name.get())
    average_s.set(average.get())
    sex_s.set(gender.get())
    m = []
    if it.get() == 1:
        m.append("Computer_IT")
    if mt.get() == 1:
        m.append("Computer_MT")
    if math.get() == 1:
        m.append("Math")
    if sci.get() == 1:
        m.append("Science")
    major_s.set(m)

root = Tk()
root.option_add("*Font","cloud 15")
root.geometry("600x550")
root.title("Test System")
name_s = StringVar()
average_s = IntVar()
sex_s = StringVar()
major_s = StringVar()
Label(root, text = "Student name = ").grid(row = 0,column = 0,stick = "sw")
Label(root, text = "Average = ").grid(row = 1,column = 0,stick = "sw")
name = Entry(root)
average = Entry(root)
name.grid(row = 0,column = 1)
average.grid(row = 1,column = 1)

gender = StringVar()
Label(root, text = "Sex : ").grid(row = 2,column = 0,stick = "sw")
Radiobutton(root,text = "Male",value = "Male",variable = gender).grid(row = 2,column = 1,stick = "w")
Radiobutton(root,text = "Female",value = "Female",variable = gender).grid(row = 2,column = 1,stick = "s")

Label(root, text = "Major : ").grid(row = 3,column = 0,stick = "sw")
it = IntVar()
mt = IntVar()
math = IntVar()
sci = IntVar()
Checkbutton(root,text = "Computer IT",variable = it).grid(row = 3,column = 1,stick = "w")
Checkbutton(root,text = "Computer MT",variable = mt).grid(row = 4,column = 1,stick = "w")
Checkbutton(root,text = "Math",variable = math).grid(row = 5,column = 1,stick = "w")
Checkbutton(root,text = "Science",variable = sci).grid(row = 6,column = 1,stick = "w")

Button(root,text = "OK",width = 6,command = check_major).grid(row = 7,column = 1,stick = "w")
Button(root,text = "Quit",width = 6,command = quit).grid(row = 7,column = 1,stick = "s")

Label(root, text = "Answer Confirm : ").grid(row = 8,column = 0,stick = "sw")
Label(root, text = "Name : ").grid(row = 9, column = 0,stick = "w")
Label(root, textvariable = name_s).grid(row = 9, column = 1,stick = "w")
Label(root, text = "Average : ").grid(row = 10, column = 0,stick = "w")
Label(root, textvariable = average_s).grid(row = 10, column = 1,stick = "w")
Label(root, text = "Sex : ").grid(row = 11, column = 0,stick = "w")
Label(root, textvariable = sex_s).grid(row = 11, column = 1,stick = "w")
Label(root, text = "Major Select : ").grid(row = 12, column = 0,stick = "w")
Label(root, textvariable = major_s).grid(row = 12, column = 1,stick = "w")
Button(root,text = "Confirm",width = 10,command = exit).grid(row = 13,column = 1,stick = "w")

root.mainloop(0)
