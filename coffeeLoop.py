count,countd = 1,1
user = 10
c = 0
name = []
discount = []
while count <= user:
    name.append(input("Input your name : "))
    if count<=3:
        discount.append("50")
    elif count<=6:
        discount.append("30")
    elif count<=10:
        discount.append("15")
    count = count + 1
else :
    print("FULL")

print("***********Output************")

while countd <= user:
    print(c ,name[c] ,"| Discount " ,discount[c],"%")
    countd = countd + 1
    c = c + 1
