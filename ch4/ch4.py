
# 条件表达式
food = input("What's your favorite food?")
reply = 'yuck' if food == 'lamb' else 'yum'
# 等价于
food = input("What's your favorite food?")
if food == 'lamb':
  reply = 'yuck'
else:
  reply = 'yum'



# for循环通常比while循环更容易使用,也不那么容易出错.但没有while循环灵活

# for循环默认初始值为0.从0到n-1
# 与for循环自动初始化循环变量不同,由程序员负责给while循环使用的变量指定初始值

# while循环要灵活得多,在whil循环面前,可以使用任何代码完成必要的初始化.循环条件可以是任何布尔表达式,
# 递增语句可放在while循环体内的任何位置





