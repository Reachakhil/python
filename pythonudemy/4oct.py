#
# lower = 3
# upper = 99
#
# print("Prime numbers between",lower,"and",upper,"are:")
#
# for num in range(lower,upper + 1):
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
#
# def prompt():
#     print("Please enter an integer value: ", end="")
# # Start of program
# print("This program adds together two integers.")
# prompt()
# # Call the function
# value1 = int(input())
# prompt()
# # Call the function again
# value2 = int(input())
# sum = value1 + value2;
# print(value1, "+", value2, "=", sum)

#-----------------------------
def count_to_10():
    for i in range(1, 11):
       print(i)
print("Going to count to ten . . .")
count_to_10()
print("Going to count to ten again. . .")
count_to_10()
