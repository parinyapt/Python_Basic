def timeinp(timein):
    timeinhr,timeinmin = int(timein[0:2]),int(timein[3:5])
    timeintotal = (timeinhr * 60)+timeinmin
    return(timeintotal)

def timeoutp(timeout):
    timeouthr,timeoutmin = int(timeout[0:2]),int(timeout[3:5])
    timeouttotal = (timeouthr * 60)+timeoutmin
    return(timeouttotal)

def processp(tin,tout):
    ttotal = tout - tin
    if (ttotal) % 60 == 0:
        hrtotal = ttotal // 60
    else:
        hrtotal = ttotal // 60 + 1

    if ttotal < 0:
        price = 404404
    elif ttotal <15:
        hrtotal = 0
        price = 0
    elif ttotal >=15 and ttotal <240:
        price = hrtotal *10
    elif ttotal >=240 and ttotal <360:
        hrtotal = hrtotal - 3
        price = (hrtotal *20)+30
    else:
        price = 200
    return price,hrtotal,ttotal

timein = input("Enter Time in with this format(HH:MM) : ")
timeout = input("Enter Time out with this format(HH:MM) : ")
print("----------------------------------")
tin = timeinp(timein)
tout = timeoutp(timeout)
price,hrtotal,ttotal = processp(tin,tout)
usehr = ttotal // 60
usemin = ttotal - (usehr * 60)
if price == 404404:
    print("error process | please try again")
else:
    print("Total Using Hour : " , usehr , "Hour " , usemin , "Minute")
    print("Total Hour : " , hrtotal , "Hour")
    print("Total Price : " , price , "Baht")
