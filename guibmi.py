from tkinter import *
def cal_bmi():
    h = float(entHight.get())
    w = float(entWeight.get())
    m = h/100
    bmi = w/(m**2)
    bmi = float('%.2f'% bmi)
    b.set(bmi)
    if(bmi<0):
        text = "404 error"
    elif(bmi>=30):
        text = "โรคอ้วนอันตราย"
    elif(bmi>=25):
        text = "โรคอ้วน"
    elif(bmi>=23):
        text = "น้ำหนักเกิน"
    elif(bmi>=18.5):
        text = "สมส่วน"
    else:
        text = "น้ำหนักต่ำกว่าเกณฑ์"
    texts.set(text)
    
root = Tk() 
root.option_add("*Font","cloud 20")
root.title("BMI System")
b = IntVar()
texts = StringVar()
Label(root, text = "Hight = ").grid(row = 0, column = 0)
Label(root, text = "Weight = ").grid(row = 1, column = 0)
Label(root, textvariable = b).grid(row = 2, column = 0)
Label(root, textvariable = texts).grid(row = 3, column = 0)
entHight = Entry(root)
entWeight = Entry(root)
entHight.grid (row = 0, column = 1)
entWeight.grid (row = 1, column = 1)
Button(root, text = "Calculate", command = cal_bmi).grid( row = 4, column= 1 )
Button(root, text = "Exit", command = exit).grid( row = 5, column= 1 )
 
root.mainloop()
 

