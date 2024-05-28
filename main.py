# print('Hello World')

# # ini comment

# """Ini
# comment multi line"""

# a = 7
# b = 'a'



# print(a*b)

# print("hasil dari a dikali b adalah", a*b)

# testing = [1,3,4,5,6,7]
# boolean = False

# print("tipe data", boolean ,"adalah", type(boolean))

# data_complex = complex(5,6)

# print("tipe data", data_complex ,"adalah", type(data_complex))

# #cara menjadikan file python agar di compile
# #ketik python -m py_compile [Nama file]
# #cd __pycache__
# #run program yang ada di folder pycache ketik manual
# #cd .. untuk kembali ke folder sebelumnya


# #memanggil type variable C

# from ctypes import c_char

# testingData = c_char('s')
# print(testingData, "bertipe data", type(testingData))



# #Casting variabel

# dataInt = 19
# print(dataInt, "bertipe data", type(dataInt))

# dataFloat = float(dataInt)
# print(dataFloat, "bertipe data", type(dataFloat))

# data_input = input("Masukkan Password : ")
# print("Password anda : ", data_input)

# data_inputFloat = float(input("Masukkan nilai anda : "))
# print("Nilai anda : ", data_inputFloat, "tipe data nilai anda", type(data_inputFloat))

# biner = bool(int(input("Masukkan biner : ")))
# print("Nilai anda : ", biner, "tipe data nilai anda", type(biner))

# a = 7
# b = 3

# print(a % b)

# fahrenheit = float(input("Masukkan suhu fahrenheit : "))
# print("Suhu fahrenheit : ", fahrenheit)

# celcius = 5/9*(fahrenheit-32)
# print("Suhu celcius : ", celcius)


# kelvin = celcius + 273
# print("Suhu kelvin : ", kelvin)

# reamur = 4/9*(fahrenheit - 32)
# print("Suhu reamur : ", reamur) 

# kelvinInput = float(input("Masukkan suhu kelvin : "))
# print("Suhu kelvin : ", kelvinInput)

# celciusConvert = kelvinInput - 273
# fahrenheitConvert = 9/5*celciusConvert + 32

# print("Suhu kelvin ke fahrenheit sebesar : ", fahrenheitConvert)

# a = 5
# b =15

# print(a is b)

# print("Id penyimpanan variabel a adalah : ", hex(id(a)))

#Operasi Not, or, and, xor

# a = True
# b = not a

# print("Data b adalah = ", b)

# c = True
# d = False

# print(c, "OR", d, "OR", a, " = ",c and d and a)

# print(d, "OR", d, " = ",d or d)

# a = 9
# b = 3

# c = a|b
# d = a&b

# #bitwise OR

# print(a, "hasil biner : ", format(a, '08b'))
# print(b, "hasil biner : ", format(b, '08b'))
# print(c, "hasil biner : ", format(c, '08b'))

# #bitwise AND

# print(d, "hasil biner : ", format(d, '08b'))

# #bitwise NOT

# e = ~a

# print(a, "hasil biner : ", format(a, '08b'))
# print(e, "hasil biner : ", format(e, '08b'))

# #shifting right and left

# f = a >> 1
# g = a << 2

# print(f, "hasil biner : ", format(f, '08b'))
# print(g, "hasil biner : ", format(g, '08b'))

#Operator assignment

a = 7

a += 1

print(a)

a %= 3

print(a)

b = 7//3 #pembulatan

print(b)

x = 0b0010

print(x, " dengan format : ", format(x, '08b'))

x <<= 2 # atau bisa dituliskan x = x << 2
print(x, " dengan format : ", format(x, '08b'))






