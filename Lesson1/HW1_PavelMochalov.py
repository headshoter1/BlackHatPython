a = input("please input name of file with extention: ")
b = input("please input new extention: ")
c = a.split(".")
d = "".join(c)

print(d)
print(".".join(c[0:len(c)-1]) + "_" + str(len(d)) + "." + b)