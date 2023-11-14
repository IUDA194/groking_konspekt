# Binary search
number_of_steps = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def binary_search(arr : list[int], item : int):
    low = 0 # Переменная которая хранит в себе начало диапазона чисел
    hight = len(arr) - 1 # Переменная которая хранит в себе конец диапазона чисел
    global number_of_steps
    while low < hight:
        number_of_steps += 1
        mid = (low + hight) // 2 # Получаем середину из возможных значений
        searhed = arr[mid]

        print("iter_number:", searhed, "middele_number:", mid, "lowwer_number:", low, "higher_number:", hight)

        if searhed == item: # Если серединаа == искомому возвращаем его
            return searhed
        elif searhed > item: # Если середина больше задаём верхнюю границу = середине
            hight = mid
        else: # Если меньше нижняя граница = середине + 1 ( + 1 для того что-бы если элемена не существуюет не отрабатывало условие low < hight в цикце и функция вохвращала None )
            low = mid + 1

    return None

print(binary_search(arr, int(input("Enter number: "))), " | number of steps: ", number_of_steps)