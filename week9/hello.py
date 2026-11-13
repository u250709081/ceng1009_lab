# def is_odd(n):
#     return n % 2 == 1
# print(is_odd(4))
# print(is_odd(5))
from operator import truediv
from os import MFD_ALLOW_SEALING
from unittest import result


#
# def is_leapyear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
# print(is_leapyear(2026))

# def print_triangle_numbers(n):
#     total = 0
#     for i in range(1,n+1):
#         total = total + i
#         print(i, total)
# print_triangle_numbers(3)
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#           return False
#     return True
# print(is_prime(5))
# def reverse(s):
#     result = ""
#     for ch in s:
#         result = ch +result
#     return result
# # print(reverse("bismillahirrahmanirrahim"))
# def reverse_slice(s):
#     return s[::-1]
# print(reverse_slice("rahmanverahimolanallahinadiyla"))
# def remove_all(sub,s):
#     return s.replace(sub,"")
# print(remove_all("rahman","bismillahirrahmannirrahim"))
# def substitute(message,key):
#     alphabet="abcçdefgğhıijklmnoöprsştuüvyz"
#     result=""
#     for ch in message:
#         index=alphabet.find(ch.lower())
#         if index==-1:
#             result=result+ch
#         elif ch.isupper():
#             result=result+key[index].upper()
#         else:
#             result=result+key[index].lower()
#     return result
# key="qtgweryuıopğüasdfhjklşizxcvbn"
# print(substitute("nasilsin insallah",key))
# def remove_dups(s):
#     result=""
#     for ch in s:
#         if ch not in result:
#             result += ch
#     return result
# print(remove_dups("hande şeker"))