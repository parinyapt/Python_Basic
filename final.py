from tkinter import*

def submit_regist():
    name_s.set(name.get())
    permonth = 250
    if monthly.get() == "1m":
        month = "1 Month"
        fullt = permonth*1
        if typee.get() == "std":
            typet = "Student"
            disc = 0
            total = permonth
        elif typee.get() == "o":
            typet = "Official"
            disc = 0
            total = permonth
        elif typee.get() == "gp":
            typet = "General Public"
            disc = 0
            total = permonth
    elif monthly.get() == "3m":
        month = "3 Month"
        fullt = permonth*3
        if typee.get() == "std":
            total = permonth*3-((permonth*3)*0.1)
            disc = 10
            typet = "Student"
        elif typee.get() == "o":
            total = permonth*3-((permonth*3)*0.05)
            disc = 5
            typet = "Official"
        elif typee.get() == "gp":
            total = permonth*3
            disc = 0
            typet = "General Public"
    elif monthly.get() == "6m":
        month = "6 Month"
        fullt = permonth*6
        if typee.get() == "std":
            total = permonth*6-((permonth*6)*0.15)
            disc = 15
            typet = "Student"
        elif typee.get() == "o":
            total = permonth*6-((permonth*6)*0.1)
            disc = 10
            typet = "Official"
        elif typee.get() == "gp":
            total = permonth*6-((permonth*6)*0.05)
            disc = 5
            typet = "General Public"
    elif monthly.get() == "12m":
        month = "12 Month"
        fullt = permonth*12
        if typee.get() == "std":
            total = permonth*12-((permonth*12)*0.20)
            disc = 20
            typet = "Student"
        elif typee.get() == "o":
           total = permonth*12-((permonth*12)*0.15)
           disc = 15
           typet = "Official"
        elif typee.get() == "gp":
           total = permonth*12-((permonth*12)*0.1)
           disc = 10
           typet = "General Public"
    total_s.set(total)
    disc_s.set(disc)
    month_s.set(month)
    type_s.set(typet)
    fullt_s.set(fullt)

root = Tk()
root.option_add("*Font","cloud 15")
root.geometry("425x700")
root.title("Register Cutomer")
name_s = StringVar()
total_s = IntVar()
disc_s = IntVar()
month_s = StringVar()
type_s = StringVar()
fullt_s = IntVar()
Label(root, text = "Customer Name ").grid(row = 0,column = 0,stick = "sw")
Label(root, text = "Email").grid(row = 1,column = 0,stick = "sw")
Label(root, text = "Address").grid(row = 2,column = 0,stick = "sw")
Label(root, text = "Mobile").grid(row = 3,column = 0,stick = "sw")
name = Entry(root)
email = Entry(root)
address = Entry(root)
mobile = Entry(root)
name.grid(row = 0,column = 1)
email.grid(row = 1,column = 1)
address.grid(row = 2,column = 1)
mobile.grid(row = 3,column = 1)

monthly = StringVar()
Label(root, text = "Monthly").grid(row = 5,column = 0,stick = "sw")
Radiobutton(root,text = "1 Month",value = "1m",variable = monthly).grid(row = 7,column = 0,stick = "sw")
Radiobutton(root,text = "3 Month",value = "3m",variable = monthly).grid(row = 8,column = 0,stick = "sw")
Radiobutton(root,text = "6 Month",value = "6m",variable = monthly).grid(row = 9,column = 0,stick = "sw")
Radiobutton(root,text = "12 Month",value = "12m",variable = monthly).grid(row = 10,column = 0,stick = "sw")
 
typee = StringVar()
Label(root, text = "Type").grid(row = 5,column = 1,stick = "sw")
Radiobutton(root,text = "Student",value = "std",variable = typee).grid(row = 7,column = 1,stick = "sw")
Radiobutton(root,text = "Official",value = "o",variable = typee).grid(row = 8,column = 1,stick = "sw")
Radiobutton(root,text = "General Public",value = "gp",variable = typee).grid(row = 9,column = 1,stick = "sw")

Button(root,text = "Register",width = 17,command = submit_regist).grid(row = 11,column = 1,stick = "sw")
Button(root,text = "Quit",width = 17,command = quit).grid(row = 12,column = 1,stick = "sw")

Label(root, text = "Register Confirm : ").grid(row = 14,column = 0,stick = "sw")
Label(root, text = "Customer Name : ").grid(row = 15, column = 0,stick = "w")
Label(root, textvariable = name_s).grid(row = 15, column = 1,stick = "w")
Label(root, text = "Monthly : ").grid(row = 16, column = 0,stick = "w")
Label(root, textvariable = month_s).grid(row = 16, column = 1,stick = "w")
Label(root, text = "Type : ").grid(row = 17, column = 0,stick = "w")
Label(root, textvariable = type_s).grid(row = 17, column = 1,stick = "w")
Label(root, text = "Total full price : ").grid(row = 18, column = 0,stick = "w")
Label(root, textvariable = fullt_s).grid(row = 18, column = 1,stick = "w")
Label(root, text = " Baht").grid(row = 18, column = 1,stick = "s")
Label(root, text = "Discount : ").grid(row = 19, column = 0,stick = "w")
Label(root, textvariable = disc_s).grid(row = 19, column = 1,stick = "w")
Label(root, text = " %").grid(row = 19, column = 1,stick = "s")
Label(root, text = "Total price : ").grid(row = 20, column = 0,stick = "w")
Label(root, textvariable = total_s).grid(row = 20, column = 1,stick = "w")
Label(root, text = " Baht").grid(row = 20, column = 1,stick = "s")

root.mainloop(0)
