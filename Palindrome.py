

def is_palindrome(n: str) -> bool:
    return n == n[::-1]

def is_palindrome_recursive(n: str) -> bool:
    return len(n) <= 1 or (n[0] == n[-1] and is_palindrome_recursive(n[1:-1]))

print(is_palindrome_recursive("level")) #-> True
print(is_palindrome_recursive("tommy"))
print(is_palindrome_recursive("johnny"))
print(is_palindrome_recursive("anutforajaroftuna"))
print(is_palindrome_recursive("murderforajarofredrum"))
print(is_palindrome_recursive("electric"))