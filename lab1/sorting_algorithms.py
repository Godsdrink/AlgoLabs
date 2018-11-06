from Lviv.ua.iot.lab1.squeezer import Squeezer


class Sorting_algorithms:
    sort_list = []

    def insert_sort(list):
        for index in range(1, len(list)):
            current_var = list[index]  # значення буде завжди правіше і ми будемо зрівнювати з лівим
            i = index - 1
            while i >= 0:
                if current_var.max_juice_level > list[i].max_juice_level:
                    list[i + 1] = list[i]  # переносим і вправо на місце числа з яким порівнюєм
                    Squeezer.changes()
                    list[i] = current_var  # перенести число вліво на і

                i = i - 1  # тепер 2 позиції вліво і зрівнюємо з тим що на 1 вправо...

                Squeezer.compare()

        return list

    def __init__(self, list):
        self.sort_list = list

    # main func of sort
    def quick_sort(self, low, hi): #high index and low index
        if low < hi: #less than 1 item in a list to be sorted
            p = self.partition(low, hi)
            self.quick_sort(low, p - 1) #all items right ot pivot
            self.quick_sort(p + 1, hi) #all items left to pivot
            pass

    # func to find pivot
    def get_pivot(self, low, hi):
        mid = int((hi + low) / 2)
        pivot = hi
        Squeezer.compare()
        if self.sort_list[low].power_consumption < self.sort_list[mid].power_consumption:
            if self.sort_list[mid].power_consumption < self.sort_list[hi].power_consumption:
                pivot = mid
            Squeezer.changes()
        elif self.sort_list[low].power_consumption < self.sort_list[hi].power_consumption:
            pivot = low
        Squeezer.compare()
        return pivot

    # func to make a swap
    def partition(self, low, hi):
        pivot_index = self.get_pivot(low, hi)
        pivot_value = self.sort_list[pivot_index]
        self.sort_list[pivot_index], self.sort_list[low] = self.sort_list[low], self.sort_list[pivot_index]
        Squeezer.changes()
        border = low

        for i in range(low, hi + 1):
            if self.sort_list[i].power_consumption < pivot_value.power_consumption:
                border += 1
                self.sort_list[i], self.sort_list[border] = self.sort_list[border], self.sort_list[i]
                Squeezer.changes()
            Squeezer.compare()

        if self.sort_list[low].power_consumption > self.sort_list[border].power_consumption:
          self.sort_list[low], self.sort_list[border] = self.sort_list[border], self.sort_list[low]
        Squeezer.changes()

        return border
