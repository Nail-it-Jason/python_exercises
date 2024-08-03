table = []
count = 0
while True:
    table += input()
    count += 1
    if count == 10:
        break
print(table)
#
# # 1
# list_0 = []
# for i in range(1, 11):
#     num = input()
#     num = int(num)
#     list_0.append(num)
# print(list_0)
#
#
# # 2
# list_temp = []
# list_a = [9, 80, 39, 48, 26, 2, 6, 77, 58, 25, 65]
# i = len(list_a) - 1
# while i >= 0:
#     list_temp.append(list_a[i])
#     i -= 1
# list_a = list_temp
# print(list_a)
#
# # 3
# list_b = [9, 80, 39, 48, 26, 2, 6, 77, 58, 25, 65]
#
# for i in range(1, len(list_b)):
#     key = list_b[i]
#     j = i - 1
#     while j >= 0 and list_b[j] > key:
#         list_b[j + 1] = list_b[j]
#         j = j - 1
#     list_b[j + 1] = key
#
# print(list_b)
#
#
# # 4
# num = input()
# num = int(num)
# i = 0
# ans = [1, 1]
# while i < num - 2:
#     ans.append(ans[i] + ans[i + 1])
#     i = i + 1
# print(ans)
#
#
# # 5
# a, b = 2813, 3589
# while(b != 0):
#     r = a % b
#     a = b
#     b = r
# print(a)
#
#
# # 6
# x = 1.0
# for i in range(1, 101):
#     x = x - (x ** 2 - 2) / (2 * x)
# print(x)
#
# x = 1.0
# for i in range(1, 101):
#     x = x - (x ** 2 - 3) / (2 * x)
# print(x)
#
# # 7
# x = input()
# x = int(x)
# i = 2
# if x == 2 or x == 3:
#     print("prime")
# while i ** 2 <= x:
#     if i ** 2 <= x and (i + 1) ** 2 > x and x % i != 0:
#         print("prime")
#     if x % i == 0:
#         print("no prime num")
#         break
#     else:
#         i += 1
#
#
# # 8
# for i in range(100, 1000):
#     a = i // 100
#     b = (i % 100) // 10
#     c = i % 10
#     if a ** 3 + b ** 3 + c ** 3 == i:
#         print(i)
