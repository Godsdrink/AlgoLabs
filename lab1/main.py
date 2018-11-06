import csv
from datetime import datetime

from Lviv.ua.iot.lab1.sorting_algorithms import Sorting_algorithms
from Lviv.ua.iot.lab1.squeezer import Squeezer


def read_data_from_file():
    squeezer_list = []
    try:
        with open('data.csv') as csvin:
            reader = csv.reader(csvin)
            for row in reader:
                new_sqeezer = Squeezer(row[0], row[1], int(row[2]), int(row[3]), row[4])
                squeezer_list.append(new_sqeezer)
    except FileNotFoundError:
        print("File with data does not exist!")
    return squeezer_list


def time_of_work(start, finish):
    return finish - start


def print_all(algorithm_name, time_of_work, compare_count, change_count, sorted_list):
    print(str(algorithm_name) + "\n Work time is: " + str(time_of_work) + "\n Compare count is: " + str(
        compare_count) + "\n Change count is: " + str(change_count) + "\n Sorted list is: \n" + str(sorted_list))


if __name__ == '__main__':
    squeezer_list = read_data_from_file()
    start = datetime.now().microsecond
    needed_sorted_list = Sorting_algorithms.insert_sort(squeezer_list)
    finish = datetime.now().microsecond
    print_all("Selection sort", time_of_work(start, finish), Squeezer.compare(),
              Squeezer.changes(), needed_sorted_list)
    Squeezer.reset()

    quicksort = Sorting_algorithms(squeezer_list)
    start = datetime.now().microsecond
    quicksort.quick_sort(0, len(squeezer_list) - 1)
    finish = datetime.now().microsecond
    print_all("quick sort or Haora sort", time_of_work(start, finish),Squeezer.compare(),
              Squeezer.changes(), quicksort.sort_list)




    # China_squeezer = Squeezer("red", 3, 5, "China")
    # America_squeezer = Squeezer("blue", 4, 5, "America")
    # EU_squeezer = Squeezer("green", 2, 6, "Europe")
    # Indian_squeezer = Squeezer("green", 15, 1, "India")
    # Squeezer_of_my_brains = Squeezer("brown", 100, 10, "Production of my mind")
    # Squeezer_which_could_kill_us = Squeezer("suitable", 2000, 12, "Vietnam_production")
    #
    # my_list = [China_squeezer, America_squeezer, EU_squeezer, Indian_squeezer, Squeezer_of_my_brains,
    #            Squeezer_which_could_kill_us]
    #
    #     print("")
    # print("Bubble_sort result with max juice level ")
    # print("P.s. Descending order")
    # print("")

    # def bubble_sort(arr):
    #     while True:
    #         corrected = False
    #         for i in range(0, len(arr) - 1):
    #             if arr[i].max_juice_level < arr[i + 1].max_juice_level:
    #                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
    #                 corrected = True
    #         if not corrected:
    #             return arr
    #
    #
    # bubble_sort(my_list)
    # Squeezer.print_list(my_list)

    # print("")
    # print("Merge_sort result with power consumption")
    # print("P.s. BAD VARIANT")
    #

    # def mergeSort(arr):
    #     if len(arr) > 1:
    #         mid = len(arr) // 2
    #         lefthalf = arr[:mid]
    #         righthalf = arr[mid:]
    #
    #         mergeSort(lefthalf)
    #         mergeSort(righthalf)
    #
    #         i = 0
    #         j = 0
    #         k = 0
    #         while i < len(lefthalf) and j < len(righthalf):
    #             if lefthalf[i].power_consumption <= righthalf[j].power_consumption:
    #                 arr[k] = lefthalf[i]
    #                 i = i + 1
    #             else:
    #                 arr[k] = righthalf[j]
    #                 j = j + 1
    #             k = k + 1
    #
    #         while i < len(lefthalf):
    #             arr[k] = lefthalf[i]
    #             i = i + 1
    #             k = k + 1
    #
    #         while j < len(righthalf):
    #             arr[k] = righthalf[j]
    #             j = j + 1
    #             k = k + 1
    #
    #
    # mergeSort(my_list)
    # Squeezer.print_list(my_list)
    #
    # print("")
    # print("Merge_sort result with power consumption")
    # print("P.s. MY VARIANT")
    #
    # def my_merge_sort(arr):
    #     if len(arr) <= 1:
    #         return arr
    #
    #     mid = len(arr) // 2
    #     left_part = arr[:mid]
    #     right_part = arr[mid:]
    #
    #     my_merge_sort(left_part)
    #     my_merge_sort(right_part)
    #
    #     return merge(left_part, right_part)
    #
    #
    # # like in lection
    # def merge (left_part, right_part):
    #     resarr = []
    #     i = j = 0
    #     while len(left_part) > 0 and len(right_part) > 0:
    #         if left_part[i].power_consumption <= right_part[j].power_consumption:
    #             resarr.append(left_part[i])
    #             i += 1
    #         else:
    #             resarr.append(right_part)
    #             j += 1
    #     if len(left_part) > i:
    #       resarr.extend(left_part[i])
    #     if len(right_part) > j:
    #         resarr.extend(right_part[j])
    #     return resarr

    # my_merge_sort(my_list)
    # Squeezer.print_list(my_list)
