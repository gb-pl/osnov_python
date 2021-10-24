
1.)

name = input("Как тебя зовут?")
age = input("Сколько тебе лет?")
print("привет", (name),"! как тебе живется в твои", (age), "?")


time_sec = int(input("Введите время в секундах"))
sec = (time_sec % 60)
mins_o = (time_sec // 60)
mins = (mins_o % 60)
hour = (mins_o // 60)
print("%d:%02d:%02d" % (hour, mins, sec))

##3
ni = input("Введите число N:")
ns =(str(ni))
n = int(ni)
nn = int(ns + ns)
nnn = int(ns + ns + ns)
print(n + nn + nnn)

##4
count = int(input("Введите целое число:"))
result = count % 10
while count >= 1:
    count = count // 10
    if count % 10 > result:
        result = count % 10
    if count > 9:
        continue
    else:
        print("Наибольшая цифра в числе -", result)
        break

##5

revenue = int(input("Ведите значение выручки: "))
costs = int(input("Ведите значение издержек: "))
profit = revenue - costs
rent = profit / revenue

if profit < costs:
    print("Фирма работает в убыток")
if profit > costs:
    print("Фирама работает с прибылью, рентабельность -", rent)
    staff = int(input("Введите число сотрудников: "))
    staffrent = profit / staff
    print("Прибыль на сотрудника составила:", staffrent)



