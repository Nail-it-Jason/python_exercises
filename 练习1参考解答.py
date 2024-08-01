# 把下列10个人的成绩排序，并输出前三名和后三名，以及所有人的平均分
score_list = [90, 65, 82, 40, 99, 76, 55, 59, 100, 36]
score_list.sort(reverse=True) # 这里通过设置reverse=True可以使得排序从大到小
print(f"前三名: {score_list[0]}, {score_list[1]}, {score_list[2]}")
print(f"后三名: {score_list[-1]}, {score_list[-2]}, {score_list[-3]}")
print(f"平均分: {sum(score_list)/len(score_list)}")


# 现在知道上面十个人各自的姓名
# 排序后手动删除A开头名字的人(只有1人)，并输出新的名单，不改变原名单的其他人的先后顺序，不能直接通过观察删除。
name_list = ["Tom", "Jerry", "Jason", "Mary", "Fiona", "Teresa", "Alex", "John", "Ed", "Bright"]
name_list.remove(sorted(name_list)[0])
# 11行代码 从里向外看，首先sorted返回临时的排好序的副本但并不改变name_list本身，
# 下标0取出副本的第一个元素，也就是Alex，然后对原来的表remove掉这个关键词
print(name_list)


# 使用一个print语句打印下列图案（提示，使用\n和空格，不使用\t）
print("   *   \n  ***  \n ***** \n*******\n ***** \n  *** \n   *   ")


# 使用for循环的range形式，计算以下数值（提示: 定义一个变量用于在循环的每一次去累加或累乘）
sum = 0
for i in range(1, 101):
    sum = sum + i
print("1 + 2 +...+ 100 =", sum)

sum = 0
for i in range(1, 101):
    sum = sum + i * i
print("1 + 4 +...+ 10000 =", sum)

product = 1
for i in range(1, 11):
    product = product * i
print("1 * 2 *...* 10 =", product)

sum = 0
for i in range(1, 101): # 1到200的奇数有100个，偶数也有100个
    sum = sum + (2 * i - 1)
print("1 + 3 +...+ 197 + 199 =", sum)

sum = 0
for i in range(1, 101):
    sum = sum + (2 * i)
print("2 + 4 +...+ 198 + 200 =", sum)

# 交换a和b的值
a = 369
b = 176
temp = a
a = b
b = temp
print(f"a = {a}, b = {b}")
# 第二种交换a和b的值的方法
a = 369
b = 176
a = a ^ b
b = a ^ b
a = a ^ b
print(f"a = {a}, b = {b}")
# 利用异或的4个性质
# a ^ a = 0
# a ^ (b ^ c) = (a ^ b) ^ c
# a ^ 0 = a
# a ^ b = b ^ a
# 58行 a = 369 ^ 176
# 59行 b = a ^ b = (369 ^ 176) ^ 176 = 369 ^ (176 ^ 176) = 369 ^ 0 = 369
# 60行 a = a ^ b = b ^ a = 369 ^ (369 ^ 176) = (369 ^ 369) ^ 176 = 0 ^ 176 = 176


