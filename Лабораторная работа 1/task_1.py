numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
s=len(numbers) #Определение количества элементов в списке

s_1 = numbers.index(None) #Поиск индекса пропущенного элемента

r=sum(numbers[0:s_1])+sum(numbers[s_1+1:])  #Определение суммы элементов в списке

sr = r/s #Определение среднего арифметического элементов в списке

numbers[4]=sr #Замена значения в списке

print("Измененный список:", numbers)

