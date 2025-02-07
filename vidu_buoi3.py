#4
def hello_MDC(str):
    #Hiển thị câu chào
    print('Hi ',str,', How are you?')
    print('Have a nice day!')

hello_MDC("Khuong")

#6, 7, 8
def giai_thua(n):
    tich = 1
    for i in range(1, n + 1):
        tich = tich * i
    return tich

n = int(input('Nhập vào một số nguyên n: '))
print(n,'! =', giai_thua(n))

print(12,'! = ',giai_thua(12))

#9
def all_ab(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div

a = 10
b = 6
tong, hieu, tich, thuong = all_ab(a, b)

print('Tổng: ',a,'+',b,' = ',tong)
print('Hiệu: ',a,'-',b,' = ',hieu)
print('Tích: ',a,'*',b,' = ',tich)
print('Thương: ',a,'/',b,' = ',thuong)

#10
def giai_thua(n):
    tich = 1
    for i in range(0,n+1):
        tich - tich*i
    return tich

print('12 !=', giai_thua)

#12
def sum_ab(a=5, b=7):
    total = a + b
    return total

print(sum_ab(8, 13))
print(sum_ab)

#13
def get_sum(*sum):
    tmp = 0
    for i in sum:
        tmp = tmp + i
    return tmp

result = get_sum(1,2,3,4,5)
print("Kết quả:", result)

#14
x = 300
y = 800
def myfunc():
    x = 200
    total = x + y
    print('(Local) x:', x)
    print('total: ', total)
myfunc()
print('-------------------------')
print('(global) x:', x)

def myfunc():
    global k
    k = 300
    print('Inside function: k = ',k)
myfunc()
print('Outside func: k =', k)

#15
x = lambda a : a + 10
print(x(5))
print(x(7))
x = lambda a, b : a*b
print(x(5,6))