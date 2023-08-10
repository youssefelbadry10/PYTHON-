#1-Write a Python program to calculate the length of a string using 2 ways

name = "ahmed"
print(len(name))

count = 0
for index in name:
    count = count +1
    print(count)

#2-Write a Python program to get a string made of the first 2 and last 2 characters of a given
#string. If the string length is less than 2, return the empty string instead ("##Sample String :
#'w3resource' Expected Result : 'w3ce'

name = "yf"

count = 0
for x in name :
  count = count + 1

SampleSTR = name[0:2] + name[-2:]

print(SampleSTR)


#3-Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string
#is less than 3, leave it unchanged. (Sample String : 'abc' Expected Result : 'abcing')

name = input("enter the name : " )
if len(name) < 3 :
    print(name)
elif name [-3:] == "ing" :
    print(name + "ly")
else:
    print(name + "ing")

*#4-Write a Python function that takes a list of words and return the longest word and the
#length of the longest one (Longest word: Exercises Length of the longest word: 9)

def longestLength(numbers):
    max1 = len(a[0])
    temp = numbers[0]

    for i in a:
        if (len(i) > max1):
            max1 = len(i)
            temp = i

    print("The word with the longest length is:", temp,
          " and length is ", max1)

a = ["one", "two", "third", "four"]
longestLength(a)


#*5-Write a Python program to change a given string to a newly string where the first and last
#chars have been exchanged using 2 ways (Sample String:abca Expected Result:ebce)

thing = input("enter the thing : ")
start = thing[0]
end = thing [-1]

print(end+thing[1:-1]+start )

#*6-Write a Python program to remove characters that have odd index values in a given string
#(Sample String:abca Expected Result:ac)

f1 = input("Please Enter the thing : ")
f2 = ''
i = 0

while (i < len(f1)):
    if (i % 2 == 0):
        f2 = f2 + f1[i]
    i = i + 1
print("original name :  ", f1)
print("Final name :     ", f2)

#7-Write a Python program to count the occurrences of each word in a given sentence (Sample
#String:amr and ahmed are frindes but amr is the tallest Expected Result:2)

sentence = "I was very happy because, i was with my friend ali, ali is my old friend"
unique1 = sentence.split()
unique2 = set(sentence)
for word in sentence:
    print(word, sentence.count(word))

#8-Write a Python script that takes input from the user and displays that input back in upper
#and lower cases

name =input("please Enter the name : ")
word = name.swapcase()
print(word)

#9-Write a Python function to reverse a string if its length is a multiple of 4

def multipile (words):
    word = 4
    for i in words :
        if len(i) > word:
            print(i)
            print(len(i))
    return words
multipile(["youssef", "ali", "jo", "khaled"])

#10- Write a Python program to remove a newline in Python

my_name="youssef\n elbadry\n"
print(my_name)
print(my_name.replace("\n",""))

#11-Write a Python program to check whether a string starts with specified characters

names= ["youssef", "ali", "khaled", "sayed","Ahmed", "abdel rahman", "Abdallah"]
print(names.startswith("A"))

#12- Write a Python program to add prefix text to all of the lines in a string

words = [ "certainty", "expected", "certain ", "fair", "happy", "necessary"]
for i in words :
    print(input("Enter the true prefix: ")+i)


#13-Write a Python program to print the following numbers up to 2 decimal places

num = float(input("Enter the number : "))

print("Original number : ", float(num))
print("Formatted number : "+"{:.2f}".format(num))

#*14-Write a Python program to print the following numbers up to 2 decimal places with a sign

num = float(input("Enter the number : "))
i = 0
if num > i :
    print("Original number : " + "+", num)
    print("Formatted number : " + "+", "{:.2f}".format(num))
else:
    print("Original number : ", num)
    print("Formatted number : " + "{:.2f}".format(num))


#15-Write a Python program to display a number with a comma separator


num =int(input("Enter the number : "))
print("the number is : "+f"{num:,d}")

#16-Write a Python program to reverse a string


name = input("enter the name : ")
def reverse(name):
    if len(name) == 0:
        return name
    else:
        return reverse(name[1:]) + name[0]

print(reverse(name))


#17-Write a Python program to count repeated characters in a string
name = input("Enter your name : ")
unique1 = name.split()
unique2 = set(name)

for i in name :
    print(i, name.count(i))

#*18-Write a Python program to find the first non-repeating character in a given string

name = input("Enter your name : ")
unique1 = name.split()
unique2 = set(name)

for i in name :
    if name.count(i) == 1:
        print(i, name.count(i))
        break

    else:
        print("None")

#19-Write a Python program to remove spaces from a given string

name = input("Enter your name : ")

for i in name :
    if i == " ":
        print(name.replace(i,""))


#20-Write a Python program to count the number of non-empty substrings of a given string
def count_substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            count += 1
    return count

s = "hello"
print(count_substrings(s))

#21-write a Python program to swap first and last element of any list.

def swap(list1) :
    if len(list1) < 2 :
        return list1
    else:
        list1[0], list1[-1] = list1[-1], list1[0]
        return list1

list1 =[1, 2, 3, 4, 5]
print(swap(list1))

#22-Given a list in Python and provided the positions of the elements, write a program to swap
#the two elements in the list. (Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3 Output : [19, 65, 23,
#90])
def swap(lst):
    if len(lst) < 2 :
        return lst
    else:
        lst[0] , lst[2] = lst[2] , lst[0]
        return lst
lst = [1, 2, 3, 4, 5]
print(swap(lst))

#23- search for the all ways to know the length of the list
lst = [1, 2, 3, 4, 5]
print(len(lst))
count = 0
for i in lst:
    count += 1

print(count)

#24-write a Python code to find the Maximum number of list of
#numbers.

lst = [1, 2, 3, 4, 5]
print(max(lst))

#25-write a Python code to find the Minimum number of list of
#numbers.

lst = [1, 2, 3, 4, 5]
print(min(lst))

#*26-search for if an elem is existing in list

element = input("Enter the element : ")
def existing(lst) :
    for i in lst:
        if i == element:
            return True
        else:
            return False
lst = ["ahmed", "ibrahim","ali"]
print(existing(lst))

#27- clear python list using different ways

lst = [1, 2, 3, 4, 5]
lst1=[]
lst.clear()
print(lst)
lst = lst1
print(lst1)

#28-remove duplicated elements from a list

lst = [1, 1, 2, 3, 4, 4, 5]
removal = set(lst)

print(removal)

#29-write a python program to count unique values inside a list using different ways

lst =[1, 2, 3, 4, 5, 6, 1, 2, 4, 5]
unique2 = set(lst)
for i in lst:
    if lst.count(i) == 1 :
        print(i)
        continue

#30-Remove all the occurrences of an element from a list in Python (Input : 1 1 2 3 4 5 1 2 1
#**Output : 2 3 4 5 2)

lst = [1, 2, 3, 4, 5, 6, 1, 1, 1, 2, 3]
for i in lst :
    counter = int(lst.count(i))
    if counter == 1 :
        print(i)
        continue

#31- write a program to Sort Python Dictionaries by Key or Value

Exam_result={
    "ahmed": 15,
    "ali": 18,
    "sayed": 20,
    "youssef":10
}
sort_dict = sorted(Exam_result.items())
print("The Exam result is : ")
for key, value in sort_dict:
    print(key, value)

#32-write python program to Remove keys with Values Greater than K ( Including mixed
#values )

Exam_result={
    "ahmed": 15,
    "ali": 18,
    "sayed": 6,
    "youssef":4
}
sort_dict = sorted(Exam_result.items())
print("The Exam result is : ")
for key, value in sort_dict:
    if value >= 7 :
        continue
    else:
        print(key, value)

#33-Write a Python program to concatenate the following dictionaries to create a new one

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}
dic4 = {}

dic4.update(dict1)
dic4.update(dict2)
dic4.update(dict3)

print(dic4)


#34-Write a Python program to iterate over dictionaries using for loops

my_dict = {'a': 1, 'b': 2, 'c': 3}

print("keys : ")
for key in my_dict:
    print(key)

print("values : ")
for value in my_dict.values():
    print(value)

print("keys : values ")
for key,value in my_dict.items():
    print(key,value)

#35- Write a Python script to merge two Python dictionaries

dic1 = {"a":5, "b":8}
dic2 = {"c": 10, "g":99}
dic_merge = {}

dic_merge.update(dic1)
dic_merge.update(dic2)

print(dic_merge)

#36-Write a Python program to get the maximum and minimum values of a dictionary values

dict = {"a":10, "d":66, "o":20, "y":88, "s":22}

for value in dict.values():
    print(max(value))

#37-Write a Python program to create a tuple of numbers and print one item

tuple =(1, 2, 3, 4, 5)

print("the first item : ",tuple[0])

#38-Write a Python program to unpack a tuple into several variables

personal_tuple = ("Youssef", 19, "Egyptian")

name, age, nationality = personal_tuple

print("Name : ", name)
print("age : ", age)
print("Nationality : ", nationality)

#39-Write a Python program to add an item to a tuple

numbers = (1, 2, 3, 4, 5, 6, 7, 8)
extra_number = 9, 10

new_tuple= numbers + extra_number

print(new_tuple)

#40-Write a Python program to convert a tuple to a string

my_tuple = ("youssef", "ahmed", "ali", "tony")

for i in my_tuple:
    print(str(i))

#41-Write a Python program to convert a list to a tuple

list_of_numbers= [1, 2, 3, 4, 5, 6]

print("tuble_of_numbers : ", tuple(list_of_numbers))

#42-Write a Python program to reverse a tuple

tuple_of_numbers = (1, 2, 3, 5, 6, 7, 8, 9)

print(tuple_of_numbers[::-1])

#43-Write a Python program to replace the last value of tuples in a list.

list_of_tuples =  [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

new_value = 50

new_list_of_tuples = [tuple[:-1]+(new_value,) for tuple in list_of_tuples]

print(new_list_of_tuples)

#44-Write a Python program to calculate the average value of the numbers in a given tuple of
#tuples

numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in numbers_tuple:
    print(int((numbers_tuple[0]+numbers_tuple[-1])/2))

#45-Write a Python program to add member(s) to a set.

def add_members(set1):
    num = int(input("Enter the number of members : "))
    for i in range(num):
        member = input(f"Enter the member {i+1} : ")
        set1.add(member)

    return set1
my_set = set()
new_set = add_members(my_set)
print(new_set)

#46-Write a Python program to remove an item from a set if it is present in the set.

set1 = {1, 2, 3, 4, 5}
my_set = set(set1)
for i in my_set:
    member = int(input("Enter the member to remove : "))
    if i == member :
        remove = my_set.remove(member)
        print(remove)
    else:
        print(my_set)

#47-Write a Python program to find the maximum and minimum values in a set

set1 = {1, 2, 3, 4, 5}
my_set = set(set1)
print("the original set is : ", my_set)
print("the maximum number is : ", max(my_set))
print("the minimum number is : ", min(my_set))

#48- Write a Python program that finds all pairs of elements in a list whose sum is equal to a
#given value.

def find_result(lst, target_sum):
    pairs = []
    for i in range(len(lst)):
        for j in range( i + i , len(lst)):
            if lst[i] + lst[j] == target_sum:
                pairs.append((lst[i], lst[j]))

    return pairs
list = [1, 2, 3, 4, 5]
target = 6
result = find_result(list, target)
print("the target result : ", target)
print( "the numbers : ", result)

#49- Write a Python program that finds all pairs of elements in a list whose sub is equal to a
#given value.

def find_result(lst, target_sub):
    pairs = []
    for i in range(len(lst)):
        for j in range( i - i , len(lst)):
            if lst[i] - lst[j] == target_sub:
                pairs.append((lst[i], lst[j]))

    return pairs
list = [1, 2, 3, 4, 5]
target = 3
result = find_result(list, target)
print("the target result : ", target)
print( "the numbers : ", result)


#50- Write a Python program that finds all pairs of elements in a list whose times is equal to a
#given value.

def find_result(lst, target2):
    pairs = []
    for i in range(len(lst)):
        for j in range( i * i , len(lst)):
            if lst[i] * lst[j] == target2:
                pairs.append((lst[i], lst[j]))

    return pairs
list = [1, 2, 3, 4, 5]
target = 3
result = find_result(list, target)
print("the target result : ", target)
print( "the numbers : ", result)
