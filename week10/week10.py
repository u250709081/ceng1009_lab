# mylist=[78,29,10,17,"hello"]
# print(mylist)
# mylist.append("apple")
# mylist.append("banana")
# myList.insert(3,cot)
# print(mylist)
# mylist.insert(0,99)
# print(mylist)
# print(mylist.index("hello"))
# mylist.remove("apple")
# print(mylist)
#
# def sumofsquares(num):
#     sum=0
#     for number in num:
#         sum+= number**2
#     return sum
# mylist=[3,4,5]
# print(sumofsquares(mylist))
#
#
# def sumevens(num):
#     sum=0
#     for number in num:
#         if num%2==0:
#             sum+=num
#         return sum
#     print(sumevens(mylist))
# def countfiveletter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#              counter += 1
#     return counter
# print(countfiveletter(["hello","world","world","world"]))
# def sumuntileven(numlist):
#     total = 0
#     for num in numlist:
#         if num%2==0:
#             break
#         total += num
#     return total
# print(sumuntileven([1,2,3,4,5,6]))
# def countuntilsam(words):
#     count = 0
#     for word in words:
#         count+=1
#         if word =='sam':
#             break
#         return count
# my_list=["ahmet","sam"]
# print(countuntilsam(my_list))
# def replace(s,old,new):
#     pieces=s.split(old)
#     print(pieces)
#     print(new.join(pieces))
#     return new.join(pieces)
# def test(actual,expected):
#     if actual==expected:
#         print("passed")
#     else:
#         print("failed")
# test(replace('missisipi','i',1),'missisipi')
# def findmaxvalueinlist(numlist):
#     max_value = numlist[0]
#     for num in numlist:
#         if num > max_value:
#             max_value = num
#         return max_value
# numlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(findmaxvalueinlist(numlist))