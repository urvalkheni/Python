name = "Urval,Kheni"
print(len(name))
print(name[0:5]) # including 0 but not 5
print(name[2:5]) # including 2 but not 5
print(name[:5]) # including 0 but not 5
print(name[0:-6]) # negative slicing
print(name[0:len(name)-6]) # it will automatically use lenn if negative slicing

# Quick Quiz :
nm = "Urval"
print(nm[-4:-2]) # print(nm[1:3]) output rv