#Вывод данных студента
name,surname,year= input("Введите имя: "), input("Введите фамилию: "), (input ("Введите год рождения: "))
student= name + "_" + surname + "_" + year #первый вывод
print(student)
name,surname=surname,name
year=int(year)
year+=60
year=str(year)
studentchanged= name + "_" + surname + "_" + year #второй вывод после смены местами имени и фамилии, изменении года
print(studentchanged)