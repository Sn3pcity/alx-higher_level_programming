0x05. Python - Exceptions

Python

 By: Guillaume

 Weight: 1

 Project will start Jan 23, 2023 6:00 AM, must end by Jan 24, 2023 6:00 AM

 Checker was released at Jan 23, 2023 12:00 PM

 An auto review will be launched at the deadline

Resources

Read or watch:



Errors and Exceptions

Learn to Program 11 Static & Exception Handling (starting at minute 7)

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:



General

Why Python programming is awesome

What’s the difference between errors and exceptions

What are exceptions and how to use them

When do we need to use exceptions

How to correctly handle an exception

What’s the purpose of catching exceptions

How to raise a builtin exception

When do we need to implement a clean-up action after an exception

Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.

You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.

You are not allowed to publish any content of this project.

Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements

General

Allowed editors: vi, vim, emacs

All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

All your files should end with a new line

The first line of all your files should be exactly #!/usr/bin/python3

A README.md file, at the root of the folder of the project, is mandatory

Your code should use the pycodestyle (version 2.8.*)

All your files must be executable

The length of your files will be tested using wc
Write a function that prints x elements of a list.



Prototype: def safe_print_list(my_list=[], x=0):

my_list can contain any type (integer, string, etc.)

All elements must be printed on the same line followed by a new line.

x represents the number of elements to print

x can be bigger than the length of my_list

Returns the real number of elements printed

You have to use try: / except:

You are not allowed to import any module

You are not allowed to use len()

guillaume@ubuntu:~/0x05$ cat 0-main.py

#!/usr/bin/python3

safe_print_list = __import__(0-safe_print_list).safe_print_list



my_list = [1, 2, 3, 4, 5]



nb_print = safe_print_list(my_list, 2)

print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list))

print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list) + 2)

print("nb_print: {:d}".format(nb_print))



guillaume@ubuntu:~/0x05$ ./0-main.py

12

nb_print: 2

12345

nb_print: 5

12345

nb_print: 5

guillaume@ubuntu:~/0x05$ 
Write a function that divides 2 integers and prints the result.



Prototype: def safe_print_division(a, b):

You can assume that a and b are integers

The result of the division should print on the finally: section preceded by Inside result:

Returns the value of the division, otherwise: None

You have to use try: / except: / finally:

You have to use "{}".format() to print the result

You are not allowed to import any module

guillaume@ubuntu:~/0x05$ cat 3-main.py

#!/usr/bin/python3

safe_print_division = __import__(3-safe_print_division).safe_print_division



a = 12

b = 2

result = safe_print_division(a, b)

print("{:d} / {:d} = {}".format(a, b, result))



a = 12

b = 0

result = safe_print_division(a, b)

print("{:d} / {:d} = {}".format(a, b, result))



guillaume@ubuntu:~/0x05$ ./3-main.py

Inside result: 6.0

12 / 2 = 6.0

Inside result: None

12 / 0 = None

guillaume@ubuntu:~/0x05$
Write a function that divides element by element 2 lists.



Prototype: def list_division(my_list_1, my_list_2, list_length):

my_list_1 and my_list_2 can contain any type (integer, string, etc.)

list_length can be bigger than the length of both lists

Returns a new list (length = list_length) with all divisions

If 2 elements can’t be divided, the division result should be equal to 0

If an element is not an integer or float:

print: wrong type

If the division can’t be done (/0):

print: division by 0

If my_list_1 or my_list_2 is too short

print: out of range

You have to use try: / except: / finally:

You are not allowed to import any module

guillaume@ubuntu:~/0x05$ cat 4-main.py

#!/usr/bin/python3

list_division = __import__(4-list_division).list_division



my_l_1 = [10, 8, 4]

my_l_2 = [2, 4, 4]

result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))

print(result)



print("--")



my_l_1 = [10, 8, 4, 4]

my_l_2 = [2, 0, "H", 2, 7]

result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))

print(result)



guillaume@ubuntu:~/0x05$ ./4-main.py

[5.0, 2.0, 1.0]

--

division by 0

wrong type

out of range

[5.0, 0, 0, 2.0, 0]

guillaume@ubuntu:~/0x05$
Write a function that raises a type exception.



Prototype: def raise_exception():

You are not allowed to import any module

guillaume@ubuntu:~/0x05$ cat 5-main.py

#!/usr/bin/python3

raise_exception = __import__(5-raise_exception).raise_exception



try:

    raise_exception()

except TypeError as te:

    print("Exception raised")



guillaume@ubuntu:~/0x05$ ./5-main.py

Exception raised

guillaume@ubuntu:~/0x05$
