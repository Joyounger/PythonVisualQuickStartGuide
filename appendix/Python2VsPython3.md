

Python3发布于2008年底,是一次重大的升级,有些改进不与Python2兼容.
1 python2中print是个语言结构,类似if,for等.
2 python3中整数除法的结果完全服务预期,python2中执行整数除法时将删除小数部分.
3 python2有两种类,老式类和新式类.Python3完全抛弃了老式类
4 python3重命名了两个重要的函数:函数input和range在Python2中分别名为raw_input和xrange
5 Python2不支持格式字符串,只支持使用运算符%的字符串插入.
全面了解Python2和Python3之前的差异
http://docs.python.org/3/whatsnew/3.0.html

将python2程序转为python3通常不难,有个工具叫2to3(http://docs.python.org/3/library/1to3/html),几乎能将任何python2程序自动转换为python3.

