num = int(input("กรอกระยะทาง")) 

if num < 5 : 
    print ("ไม่ส่ง")
elif num <= 50 :
    print ("10 bath")
elif num <= 100 :
    print ("15 bath")
elif num <= 300 :   
    print ("25 bath")
elif num <= 500 :
    print ("35 bath") 
else :
    print ("45 bath") 