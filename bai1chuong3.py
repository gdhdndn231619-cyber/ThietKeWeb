def somax(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print("Giá trị lớn nhất là: ",somax(4,5,6))