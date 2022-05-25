class MovingTotal:
    def __init__(self):
        self.store_numbers = []
        self.totals = []

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        if len(self.store_numbers) != 0:
            lenFlag = len(self.store_numbers)
            self.store_numbers.extend(numbers)
            for i in range(lenFlag-2, len(self.store_numbers)):
                    self.totals.append(sum(self.store_numbers[i:i+3])) 
        else:
            self.store_numbers.extend(numbers)
            for i in range(len(self.store_numbers)-2):
                    self.totals.append(sum(self.store_numbers[i:i+3])) 

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        return total in self.totals

if __name__ == "__main__":
    movingtotal = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    #print(movingtotal.contains(7))

    movingtotal.append([5])
    # print(movingtotal.contains(6))
    #print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    #print(movingtotal.contains(7))