
numbers=[int(x) for x in input("input list of numbers:").split()]
count_odd=0
count_even=0
for x in numbers:
    if x%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("No. of even numbers:",count_even)
print("No. of odd numbers:",count_odd)

