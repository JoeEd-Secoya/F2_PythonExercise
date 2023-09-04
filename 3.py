x = input("Please enter a number: ")
large = int(x[0])
small = int(x[0])
count = 0
for num in str(x):
    count+=1
    if(large<int(num)):
        large = int(num)
    if(small>int(num)):
        small = int(num)

print(f'Number of digits in the given number is: {count}\nSmallest number is: {small}\nHighest number is: {large}')
