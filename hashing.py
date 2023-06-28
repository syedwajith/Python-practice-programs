class HashTable:
    def __init__(self):
        self.size = int(input("Enter Table size : "))
        self.table = [None] * self.size
    
    def insert(self, key, value):
        index = key
        self.table[index] = value

    def search(self, key):
        index = key
        if self.table[index] is not None:
            return self.table[index]
        else:
            return None
        
my_table = HashTable()

key_value = int(input("Enter key : "))
value = input("Enter the value : ")
my_table.insert(key_value, value)
add_value = input("Add another value means press 1 or press 0 : ")

while add_value != '0':
    key_value = int(input("Enter key : "))
    value = input("Enter the value : ")
    my_table.insert(key_value, value)
    add_value = input("Add another value means press 1 or press 0 : ")

search_key = int(input("Enter key to search : "))
result = my_table.search(search_key)
print(result)