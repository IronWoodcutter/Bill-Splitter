# write your code here
import random
friends = {}
print('Enter the number of friends joining (including you):')
number_of_friends = int(input())
print()
if number_of_friends <= 0:

    print('No one is joining for the party')
    exit()
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for item in range(number_of_friends):
        friends[input()] = 0
print()
print('Enter the total bill value:')
total_bill = int(input())
print()
if total_bill % number_of_friends == 0:
    friend_bill = int(total_bill / number_of_friends)
else:
    friend_bill = round(total_bill / number_of_friends, 2)
for key in friends:
    friends[key] = friend_bill
#print(friends)
print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
lucky = input()
print()

if lucky == 'No':
    print('No one is going to be lucky')
    print()
    print(friends)
elif lucky == 'Yes':
    lucky_friend = random.choice(list(friends))
    if total_bill % number_of_friends == 0:
        friend_bill_new = int(total_bill / (number_of_friends - 1))
    else:
        friend_bill_new = round(total_bill / (number_of_friends - 1), 2)
    for key in friends:
        friends[key] = friend_bill_new
    friends[lucky_friend] = 0
    print(f'{lucky_friend} is the lucky one!')
    print()
    print(friends)





