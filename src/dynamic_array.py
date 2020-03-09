class DynamicArray:
    # we need an initial size, which we'll call capacity. We're emulating building an array by initializing an array with empty data, and not using built-in python methods.
    def __init__(self, capacity): 
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity

    def insert(self, index, value):
        #we need to check that we have room for our new data
        if self.count >= self.capacity:
            self.double_size()
        #make sure index is in range
        if index > self.count:
            print("Error: Index out of range")
            return
        #start with the last one, shift everything right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i -1]

        #insert our value
        self.storage[index] = value
        self.count +=1

    def append(self, value):
        self.insert(self.count, value)

    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage


        
my_array = DynamicArray(4)
my_array.insert(0, 1)
my_array.insert(0, 2)
my_array.insert(1, 3)
my_array.insert(3, 4)
my_array.insert(0, 5)
my_array.append(20)

print(my_array.storage)



