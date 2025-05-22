for i in range(1,12):
    if(i==5):
        print("skip The Itration")
        continue
    if(i==7):
        print("breaking the loop")
        break
    print(i," x ",10," = ",10*i)
print("And Exit the loop")