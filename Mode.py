def f_mode(num):
    mode = num[0]
    max_count = num.count(mode)

    for i in num:
        count = num.count(i)
        if count > max_count:
            max_count = count
            mode = i
    return mode


numbers = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in numbers.split()]

print("Mode:", f_mode(numbers))
