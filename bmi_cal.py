from decimal import Decimal
class bmi:
    def __init__(self,namel,weight,height):
        self.namel = namel
        self.weight = float(weight)
        self.height = float(height)
       
    def nameout(a):
        return a.namel

    def bmi_calc(b):
        height1 = b.height
        weight1 = b.weight
        heightn = height1/100
        bmitotal = weight1/(heightn**2)
        return bmitotal

    def bmi_process(self,bmit):
        if(bmit<0):
           text = "404 error"
        elif(bmit>=30):
            text = "โรคอ้วนอันตราย"
        elif(bmit>=25):
            text = "โรคอ้วน"
        elif(bmit>=23):
            text = "น้ำหนักเกิน"
        elif(bmit>=18.5):
            text = "สมส่วน"
        else:
            text = "น้ำหนักต่ำกว่าเกณฑ์"
        return text

name = input("Enter name and lastname => ")
weight = input("Enter weight(Kg) => ")
height = input("Enter height(cm) => ")
aa = bmi(name,weight,height)
name1 = aa.nameout()
bmitotal = aa.bmi_calc()
bmi2 = Decimal("%.2f" % bmitotal)
text = aa.bmi_process(bmitotal)
print("คุณ " + name1)
print("ค่า BMI ของคุณ : " , bmi2)
print("ภาวะ : " + text)