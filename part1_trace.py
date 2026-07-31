numbers = [8, 3, 15, 6, 2]

maximum = numbers[0]
comparisons = 0

for i in range(1, len(numbers)):
    comparisons += 1
    if numbers[i] > maximum:
        maximum = numbers[i]

print("Input:", numbers)
print("Largest number:", maximum)
print("Comparisons made:", comparisons)

sorted_numbers = sorted(numbers)
print("Sorted List:", sorted_numbers)