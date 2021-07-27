majorcount,majorprint = 1,1
majormax = 22
major = {}

while majorcount <= majormax:
    major[input("code : ")] = input("Major name : ")
    majorcount = majorcount + 1
else :
    print("FULL")

userselect = int(input("Select Menu 1 or 2\n1.Search major\n2.Report All Major\nMenu : "))
if userselect==1:
    print("***********Search major************")
    majorsearch = input("Major code for find major : ")
    print(major[majorsearch])
elif userselect==2:
    print("***********Report All Major************")
    print(major)
else:
    print("not correct")
    pass