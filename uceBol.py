print("""********************************
Üçe Bölünebilen Sayılar Programı     
********************************""")

list1 = list(range(1,101))

for i in list1:
    if (i % 3 == 0):
        print(i)
    else:
        continue