#Bai21
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def getArea(self):
        area = round(self.width * self.height)
        return area
    
    def getPerimeter(self):
        perimeter = round((self.width + self.height)*2, 1)
        return perimeter
    
#Bai36
r1 = Rectangle(7,3)
r2 = Rectangle(5,4)

# Get the width and height attributes of the rec1 object
x = r1.width
y = r1.height
print('----Attributes----')
print('1. Width:', x)
print('2. Height:', y)

# Call the getArea and getPerimeter methods of the rec1 object
area = r1.getArea()
perimeter = r1.getPerimeter()
print('---------Methods----------')
print('1. Area:', area)
print('2. Perimeter:', perimeter) 

#Bai37
f = open('testFile.txt')

st = f.read()

print('Content:')
print(st)

#Bai38
f = open('testFile.txt')
print(f.readline())
print(f.readline())

f.close()

f = open('testFile.txt')
for x in f:
    print(x)

f.close()

#Bai39
f1 = open('testFile.txt', 'w')
st = 'Welcome to Python for Analysis'
f1.write(st)
f1.close()

#Bai40
f1 = open('testFile.txt', 'a+')
st = 'This is new line........'
f1.write('st')
f1.close()
f = open("testFile.txt", "r")
print(f.read())

#bai41
f2 = open('testFile.txt')
print('1.Tên file: ',f2.name)
print('2. Chế độ mở: ',f2.mode)
print('3. Trạng thái đóng mở file: ',f2.closed)

#Bai42
fo = open('testFIle.txt', 'w')
fo.write("Tobe or not tobe. \n Nghi lon de thanh cong! \n")
fo.close()
print('Ghi file thanh cong!')
obj = open("test.txt", "w")
obj.write("Chao mung cac ban den voi khoa CNTT")
obj.close()

obj1 = open("test.txt", "r")
s = obj1.read()
print(s)
obj1.close()

obj2 = open("test.txt", "r")
s1 = obj2.read(20)
print(s1)
obj2.close()