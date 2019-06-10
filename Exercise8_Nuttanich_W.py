username = input("Username :")
password = input("Password :")
if username == "nuttanich" and password == "wangsotorn" :
    print(">>>>>> Welcome to stationery store <<<<<<")
    print("1.Pencil 15 Baht\n2.Pen 20 Baht\n3.Eraser 5 Baht")
    x = input("what do you want ? :")
    a = 0
    while (x != "no" ) :
        if x == "pencil" :
           b = int(input("How mach do you want ? :"))
           c = (15*b)
           a += c
           x = input("what do you want ? :")
        elif x=="pen" :
            k = int(input("How mach do you want ? :"))
            f = 20*k
            a += f
            x = input("what do you want ? :")
        elif x=="eraser" :
            d = int(input("How mach do you want ? :"))
            r = 5*d
            a += r
            x = input("what do you want ? :")
    print(">>>>>> Bill <<<<<<")
    print("TOTAL :",int(a))
    print(">>>>>> THANK YOU <<<<<<")
else:
    print("ERROR")






