large = 0
for x in range(1,4):
    y = int(input(f"Input {x} integer: "))
    if(y>large):
        large = y

print(f"Largest is : {large}")
