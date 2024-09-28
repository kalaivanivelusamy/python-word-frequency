import string
import pprint

def is_palindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1] #option 1
    # return s == ''.join(reversed(s)) #option 2

pprint.pprint(is_palindrome("A man, a plan, a canal: Panama"))  # True
pprint.pprint(is_palindrome("race a car"))                        # False
pprint.pprint(is_palindrome("No 'x' in Nixon"))                  # True