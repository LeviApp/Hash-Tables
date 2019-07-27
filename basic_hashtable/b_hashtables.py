

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


user1 = Pair("App", "Levi")
user2 = Pair("Yi", "Anastasia")
user3 = Pair("Carson", "Jim")
user4 = Pair("Seke", "Hyde")
user5 = Pair("Thumb", "Tom")
user6 = Pair("Doff", "Valerie")
user7 = Pair("Hope", "Karla")
user8 = Pair("Brown", "Caleb")
user3_updated = Pair("Brown", "Kaleb")


def equal(a, b):
    if a.key == b.key:
        replace = input(f'Spot already filled, Do you want to replace {a.key}: {a.value} with {b.key}: {b.value}? y or n      ')

        if replace == 'y':
            a.value = b.value
            print(f'Updated dictionary with {a.key}: {a.value}')
            return a

        else:
            print(f'Dictionary entry {a.key}: {a.value} was kept')
            return a
# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.dict = [None]* capacity

bank = BasicHashTable(16)

# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):

    h = 5381

    for c in string:
        h = ((h << 5)+ h) + ord(c)

    print(h%max)
    return h % max

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, entry):
    
    index = hash(entry.key, hash_table.capacity)

    if hash_table.dict[index] == None:
        hash_table.dict[index] = entry
        print(f'Updated dictionary with {entry.key}: {entry.value}')
    
    else:
        item = hash_table.dict[index]

        equal(item,entry)

        while item.next != None:

            equal(item,entry)

            item = item.next
        
        equal(item,entry)

        item.next = entry
        print(f'Updated dictionary with {entry.key}: {entry.value}')


    
        
hash_table_insert(bank, user1)
hash_table_insert(bank, user2)
hash_table_insert(bank, user3)
hash_table_insert(bank, user4)
hash_table_insert(bank, user5)
hash_table_insert(bank, user6)
hash_table_insert(bank, user7)
hash_table_insert(bank, user8)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):

    index = hash(key, hash_table.capacity)

    deleted = key

    for entry in hash_table.dict:
        try:
            if entry.key == key:
                confirmation = input(f'Are you sure you want to delete value at {key}? y or n      ')
                if confirmation == 'y':
                    print(f'Entry {entry.key}: {entry.value} was deleted')
                    hash_table.dict[index] = None
                    return     
                else:
                    print(f'Entry {entry.key}: {entry.value} was kept')
                    return
        except:
            continue    
    print(f'Key "{key}" was not found')





# hash_table_remove(bank, 'Yi')

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    
    for item in hash_table.dict:
        try:
            if item.key == key:
                print(f'Entry was found -- {item.key}: {item.value}')
                return item.value
        except:
            continue
            
    print(f'Entry was not found, please try again.')
    return False


# v = input("What are you looking for?    ")

# while hash_table_retrieve(bank, v) == False:
#     v = input("What are you looking for?    ")





# def Testing():
#     ht = BasicHashTable(16)

#     hash_table_insert(ht, "line", "Here today...\n")

#     hash_table_remove(ht, "line")

#     if hash_table_retrieve(ht, "line") is None:
#         print("...gone tomorrow (success!)")
#     else:
#         print("ERROR:  STILL HERE")


# Testing()
