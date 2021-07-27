class comission:
    def __init__(self):
        self.namelast = input("Enter name and lastname => ")
        self.jobp = int(input("Job Position List\n 1 - Head of Department \n 2 - Deputy Head of Department \n 3 - Sales Person \nEnter Number your Job Position => "))
        self.circ = float(input("Enter your circulation per month => "))
    def nameout(self):
        return self.namelast
    def setsalarytotal(self):
        if self.jobp == 1 :
            sjob = 50000
            sposition = 10000
            stotal = sjob + sposition
            jobptext = "Head of Department"
        elif self.jobp == 2 :
            sjob = 30000
            sposition = 5000
            stotal = sjob + sposition
            jobptext = "Deputy Head of Department"
        elif self.jobp == 3 :
            sjob = 15000
            sposition = 3000
            stotal = sjob + sposition
            jobptext = "Sales Person"
        else :
            sjob = 0
            sposition = 0
            stotal = sjob + sposition
            jobptext = "Error job Position | Please Try again!"
        return sjob,sposition,stotal,jobptext
    def circulationtotal(self,salarytotal):
        if self.circ <= 2999999 :
            ctotal = self.circ * 0.02
            sctotal = ctotal + salarytotal
        elif self.circ <= 3999999 :
            ctotal = self.circ * 0.03
            sctotal = ctotal + salarytotal
        elif self.circ <= 4999999 :
            ctotal = self.circ * 0.04
            sctotal = ctotal + salarytotal
        else :
            ctotal = self.circ * 0.05
            sctotal = ctotal + salarytotal
        return ctotal,sctotal
process = comission()
name = process.nameout()
salaryjob , salaryposition , salarytotal , jobptext = process.setsalarytotal()
ctotal , sctotal = process.circulationtotal(salarytotal)
print("------------------------------")
print("Salary Report \nName : ", name,"\nJob Position : ",jobptext, "\nSalary : ","%.2f" %salaryjob," Baht", "\nSaraly Positon : ","%.2f" %salaryposition," Baht", "\nTotal Saraly : ","%.2f" %salarytotal, "\nTotal Commission : ","%.2f" %ctotal," Baht", "\nAmount Salary : ","%.2f" %sctotal," Baht")


    