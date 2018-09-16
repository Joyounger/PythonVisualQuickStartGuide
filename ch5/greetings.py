

# 带默认值的参数不能位于没有默认值的参数前面

# 如果只在第一次调用函数时给默认参数赋值, 在复杂的程序中,这可能称为微妙的bug根源

def greet(name, greeting = 'Hello'):
	print(greeting, name + '!')

greet('Bob')
greet('Bob', 'Good morning')