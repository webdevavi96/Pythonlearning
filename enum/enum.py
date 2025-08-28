list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_list = []

for index, item in enumerate(list):
    if index == 2 or index == 4 or index == 6 or index == 8:
        odd_list += [item]
        
print(f"The odd list is: {odd_list}")