
def list_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + list_sum(numbers[1:])

def count_char(string, char):
    if not string:
        return 0
    return (string[0] == char) + count_char(string[1:], char)

def fib(n):
    if n <=0:
        return 0
    elif n ==1:
        return 1
    return fib(n-1) + fib(n-2)


print(list_sum([1, 2, 3, 4, 5, 18,23, 3, 2, 1, 9319, 2]))
print(count_char("aaaaaa", "a"))
print(fib(6))
