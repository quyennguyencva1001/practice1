
# def nguyen_to(x):
#     b=0
#     for i in range (2,x):
#         if x%i==0:
#             b=b+1
#             if b==1:
#                 break   
#     if b==0:
#         print(str(x)+ " " + "la so nguyen to")
#     else:
#         print(str(x)+ " " + "khong la so nguyen to")
# ket_qua= nguyen_to(15)
# print(ket_qua)
#return True false, tạo list đếm số nt trong list
def nguyen_to(x):
    b=0
    for i in range (2,x):
        if x%i==0:
            b=b+1
            if b==1:
                break   
    if b==0:
        return True
    else:
        return False
a=[2,3,4,5]
c=0
for j in a:
    if nguyen_to(j)==True:
        c=c+1
print("Co " + str(c)+" so nguyen to")