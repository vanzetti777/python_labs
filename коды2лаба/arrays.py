# test1=[3,-1,5,5,0]
# test2=[42]
# test3=[-5, -2, -9]
# test4=[]
# test5=[1.5, 2, 2.0, -3.1]
# def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
#     if len(nums)==0:
#         print('ValueError')
#     else:
#         list2=(min(nums),max(nums))
#         print(list2)

# print(min_max(test1))
# print(min_max(test2))
# print(min_max(test3))
# print(min_max(test4))
# print(min_max(test5))



test1=[3, 1, 2, 1, 3] 
test2=[]
test3=[-1, -1, 0, 2, 2]
test4=[1.0, 1, 2.5, 2.5, 0]
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    list_int=[]
    list_float=[]
    for i in nums:
        if type(i)==int:
            list_int.append(i)
        else:
            list_float.append(i)
    res1=[x for x in list_float if int(x) in list_int]
    res2=[x for x in list_int if float(x) not in list_float]
    print(sorted(set(res1+res2+list_float)))
    print(res1)
    print(res2)
    print(list_float)
print(unique_sorted(test1))
print(unique_sorted(test2))
print(unique_sorted(test3))
print(unique_sorted(test4))



# test1=[[1, 2], [3, 4]]
# test2=([1, 2], (3, 4, 5))
# test3=[[1], [], [2, 3]]
# test4=[[1, 2], "ab"]

# def flatten(mat: list[list | tuple]) -> list:
#     list1=[]
#     list2=[]
#     count=0
#     for enum1 in mat:
#         for enum2 in enum1:
#             list1.append(enum2)
#             if type(enum2)==int:
#                 count+=1
#             if count==len(list1):
#                 list2.append(enum2)
#             else:
#                 print('TypeError')
#     if count==len(list1):
#         print(list2)

# print(flatten(test1))
# print(flatten(test2))
# print(flatten(test3))
# print(flatten(test4))




