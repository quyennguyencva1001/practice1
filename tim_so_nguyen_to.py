
def nguyen_to(x):
    b=0
    for i in range (2,x):
        if x%i==0:
            b=b+1
            if b==1:
                break   
    if b==0:
        print(str(x)+ " " + "la so nguyen to")
    else:
        print(str(x)+ " " + "khong la so nguyen to")
ket_qua= nguyen_to(15)
print(ket_qua)
#return True false, tạo list đếm số nt trong list