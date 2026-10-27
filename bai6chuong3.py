def sohoanhao(n):
    tong=0
    for i in range(1, n):
        if n%i==0:
            tong=tong+i
    if tong==n:
        return True
    return False

def sichinhphuong(n):
    if int(n**0.5)**2==n:
        return True
    return False

n=int(input("Nhập n: "))
if sohoanhao(n)==True:
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải số hoàn hảo")

if sichinhphuong(n) == True:
    print(n, "là số chính phương")
else:
    print(n, "không phải số chính phương")