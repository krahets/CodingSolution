class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.dic = {}
    

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)
        self.dic[number] = len(self.nums) - 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in range(len(self.nums)):
            tar = value - self.nums[i]
            if tar in self.dic and self.dic[tar] != i: return True
        return False