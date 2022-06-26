def min(numbers):
    result = numbers[0]
    for num in numbers:
        if result > num:
            result = num
    return result
min_number = min("123456789")
print("Min number: ", min_number)
