#hasRice = True
#hasspoon = False 

#if hasRice :
#    print("มีข้าว")
#     if hasspoon :
#         print("มีช้อน")
#         print("กินข้าวได้")
#    else:
#        print("กินข้าวไม่ได้ เพราะไม่่มีช้อน")
#else:
#    print("กินข้าวไม่ได้เพราะไม่มีข้าว")


vera = int(input("กี่รอบ"))
box = 0

for i in range (1,vera+1): 
    box += i
    print("วนรอบที่ ", i,"ผลรวมคือ",box)
    


    
