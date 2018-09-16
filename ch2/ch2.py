

# 所有适用于整数的算术运算都可用于浮点数,包括%和//(整除)
5.6 // 2
8.8 ** -5.4



# 溢出错误OverflowError 意味着计算结果太大或太小.python无法将其表示为浮点数



# python中用1j表示-1的平方根



# 使用导入方式from math import *时.如果函数与math模块中的某个函数同名,将被math模块中的某个同名函数覆盖
# 因此使用import math通常更安全,因为它不会覆盖任何既有函数.
# 还可以导入模块的特定函数,eg 只导入sqrt和tan
# from math import sqrt, tan



# 字符串
# 单引号和双引号的一个主要用途是,能够在字符串中包含字符"和'
"It's great"
'she said  "Yes!"'

# 如果在字符串中包含错误类型的引用,将导致错误.
# len(s)返回字符串长度

# 将同一个字符串拼接很多次
'hee' * 3 # 'heeheehee'


# 导入模块后,可以使用dir(模块名)列出模块的所有函数
# help(函数名)然看每个函数帮助文档

print(math.tanh.__doc__) # 打印math.tanh函数帮助文档

dir(__builtins__) # 查看完整的python内置函数清单
dir('') # 查看内置的字符串函数

# python3将小数部分为.5的数字圆整到最接近的偶数


# python区分大小写



