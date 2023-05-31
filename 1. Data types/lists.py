prizes = [5, 10, 20, 30]

dbl_prizes = []

for prize in prizes:
    dbl_prizes.append(prize * 2)
print(dbl_prizes)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_nums_even = []

for num in nums:
    if (num**2) % 2 == 0:
        squared_nums_even.append(num**2)
print(squared_nums_even)


# comprehension method

print("Comprehension method")
dbl_prizes = [prize * 2 for prize in prizes]
print(dbl_prizes)


squared_nums_even = [num**2 for num in nums if (num**2) % 2 == 0]
print(squared_nums_even)
