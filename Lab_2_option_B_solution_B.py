#***********************************************************************************************
#Edgar Escobedo
#80502432
#Lab 2 option B, Solution B
#***********************************************************************************************
#Regular node class and constructor which stores the next and counter


#This lab is solution B, in which we will first use the passwords list in a dictionary, which will give use the amount of times that it
#appears, when we are done, we will use that information to introduce it to the linked list, and then sort the linked list with
#our bubble sort and merge sort

class Node(object):
    password = ""
    count = -1
    next = None

    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next


#Method to get the size of the node by traversing it
def get_length(self):
    curr = self
    counter = 0
    while curr != None:
        counter +=1
        curr = curr.next
    return counter


#Linked list, when is first created it has size 0, here we have the get length method
#The most important part is my add_to_list method which will first create the node with the information that it's given, if the list
#is empty it will insert the node as head. If is is not empty it will traverse the whole list to check if that password "node" is already
#in it, if it is it will only update the counter, if it is not, it will add to the end of the list
class Linked_List:
    def __init__(self):
        self.size = 0
        self.head = None

    def length(self):
        return self.size

    def add_to_list(self, password):
        added_node = Node(password, 1, None)
        if self.head == None:
            self.head = added_node
            self.size = self.size + 1
        else:
            curr = self.head
            while (curr != None):
                if str(added_node.password) == str(curr.password):
                    curr.count += 1
                    return
                elif curr.next == None:
                    curr.next = added_node
                    self.size = self.size + 1
                    return
                curr = curr.next

    def list_read(self):
        if (self.head == None):
            return
        curr = self.head
        while curr != None:
            print("Password: "+curr.password + ", Count: "+str(curr.count))
            curr = curr.next


    def list_20_top(self):
        if self.head == None:
            return
        curr = self.head
        counter = 0
        while curr != None:
            if counter == 20:
                return
            else:
                print("Password: " + curr.password + ", Count: " + str(curr.count))
                curr = curr.next
                counter +=1


#READING FILE
my_file = open("10-million-combos.txt", "r")
passwords_list = my_file.readlines()

#Separating passwords
#Separating passwords
#In this method we will use the previously created list with usernames and passwords to store it in the linked list, we will do so,
#by iterating each "line" in our list with usernames and passwords, we will separate them by means of the split method, check if
#the length is greater than 1 (because in some cases we have a null password), if it is, we will add it to our list which will later
#be used inside the dictionary
counter = 0
list_passwords_dict = []
while (counter != len(passwords_list)):
    list_x = passwords_list[counter]
    wrds = list_x.split()
    if len(wrds) > 1:
        list_passwords_dict.append(wrds[1])
    counter = counter + 1

#Creation of dictionary, if it sees a now password it will add it to the dictionary, if it is repeated, it will increase by 1 its item value
dict = {}
for item in list_passwords_dict:
    if item in dict:
        dict[item] = dict[item] + 1
    else:
        dict[item] = 1


#Using the information of the dictionary, we will use its key, as the password, and the value inside of it to know how many times it must be
#entered into the list
linked_list_dict = Linked_List()
for item, value in dict.items():
    for i in range (dict[item]):
        linked_list_dict.add_to_list(item)


#My bubble sort method has 4 cases, which are the simple cases, checks if the list is empty or if it's length 1, just returning the list
#If the length is 2, it will swap the nodes if needed. If the list if any longer it will enter my list method, which will check if any swaps
#were as the base cases, if no swaps were made it means that is sorted and it will end, if not it will go throught the length of
#the list and swap the information inside of the nodes if the curr (node one step ahead) is greater than previous.
def bubble_sort(ls):
    if ls.size == 0:
        return None
    if ls.size == 1:
        return ls
    if ls.size == 2:
        if ls.head.count < ls.head.next.count:
            tmp = ls.head
            ls.head = ls.head.next
            ls.head.next = tmp
            return ls
    previous = ls.head
    swapped = True
    while swapped:
        swapped = False
        previous = ls.head
        curr = ls.head.next
        while curr != None:
            if previous.count < curr.count:
                tmp_count = previous.count
                tmp_password = previous.password
                previous.count = curr.count
                previous.password = curr.password
                curr.count = tmp_count
                curr.password = tmp_password
                swapped = True
            curr = curr.next
            previous = previous.next


#The merge sort method works by recursively "cutting" the linked list by half, we will do so by means of traversing through
#our list to find the right place to partition it. Once the list is divided into lists of one value or node, we will use
#the second part which is the merge_lists, which will check the value inside the node and compare it against each other, to place
#the biggest values in the right position and in this way sort it.
def merge_sort(list):
    tmp = list
    if list is None or list.next is None:
        return list
    length = get_length(list)
    for i in range(int(length / 2) - 1):
        tmp = tmp.next
    lefty = tmp.next
    tmp.next = None
    righty = list
    left = merge_sort(lefty)
    right = merge_sort(righty)
    return merge_lists(left, right)


def merge_lists(lefty, righty):

    if lefty == None:
        return righty
    if righty == None:
        return lefty
    if lefty.count > righty.count:
        final_list = lefty
        final_list.next = merge_lists(lefty.next, righty)
    else:
        final_list = righty
        final_list.next = merge_lists(lefty, righty.next)
    return final_list


second_list = Linked_List()
second_list = linked_list_dict
print("====================================== UNSORTED LINKED LIST ==========================================")
#Sorting the linked list
Linked_List.list_read(linked_list_dict)
bubble_sort(linked_list_dict)
print("=================== SORTED TOP 20 PASSWORDS IN LINKED LIST USING BUBBLE SORT =========================")
Linked_List.list_20_top(linked_list_dict)
merge_sort(second_list.head)
print("")
print("===================== SORTED TOP 20 PASSWORDS IN LINKED LIST USING MERGE SORT =========================")
Linked_List.list_20_top(second_list)
