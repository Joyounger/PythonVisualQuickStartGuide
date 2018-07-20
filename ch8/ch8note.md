
###### 设置字符串格式
字符串插入是一种设置字符串格式的简单方法,是Python从C语言借鉴而来:
x = 1 / 81
print('value: %.2f' % x)

格式字符串:Python中另一种创建美观字符串的方式是结合使用格式字符串和字符串函数format(value, format_spec).例如:
'My {pet} has {prob}'.format(pet = 'dog', prob='fleas')
在格式字符串中,用大括号括起的内容都将被替换,称为named replacement.named replacement的可读性好.
也可以按照位置替换值:
'My {0} has {1}'.format('dog', 'fleas')
还可以像字符串那样插入那样使用转换说明符:
'1/81 = {x}'.format(x/81)
可以使用大括号指定格式设置参数
'num = {x:.{d}f}'.format(x=1/81, d=3)
使用常规的字符串插入无法做到这一点.如果要在格式字符串中表示字符{或}可使用{{和}}
相比字符串插入,格式字符串更灵活,更强大,但也更复杂.如果只想创建一些格式简单的字符串,字符串插入可能是最佳的选择.而格式字符串更适合庞大而复杂的设置任务.

要在Python中包含\字符,必须使用\, 为避免使用两个反斜杠,可使用原始字符串:
r'C:\home\python'

###### 检查文件和文件夹

```python
def list_cwd():
    return os.listdir(os.getcwd())
def files_cwd():
    return [p for p in list_cwd()
            if os.path.isfile(p)]
def folders_cwd():
    return [p for p in list_cwd()
            if os.path.isdir(p)]
def list_py(path = None): #获取当前目录中的py文件
    if path == None:
        path = os.getcwd()
        return [fname for fname in os.listdir(path)
          if os.path.isfile(fname)
          if fnmae.endswith('.py')]

def size_in_bytes(fname):
    return os.stat(fname).st_size
def cwd_size_in_bytes():
    total = 0
    for name in files_cwd():
        total = total + size_in_bytes(name)
    return total
def cwd_size_in_bytes2(): # 用到了生成器表达式
    return sum(size_in_bytes(f)
               for f in files_cwd())
```

###### 处理文本文件
1 逐行读取文本文件
```python
def print_file1(fname):
    f = open(fname, 'r')
    for line in f:
        print(line, end = '') # 如果改为print(line),显示的文件内容中就会包含额外的空行.
    f.close()  # 这行代码是可选的
```
open不会将文件读取到内存.未指定模式时,open默认以只读方式打开文本文件.

2 将整个文本文件作为一个大型字符串读取
```python
def print_file2(fname):
    f = open(fname, 'r')
    print(f.read())
    f.close()
```
如果要读取的文件很大,这种方法会占用大量内存

3 将字符串插入到文件开头
```python
def insert_title(title, fname = 'story.txt'):
    f = open(fname, 'r+') #打开文件的模式为r+,意味着可读取和写入文件
    temp = f.read()
    temp = title + '\n\n' + temp
    f.seek(0)  # 让文件指针指向文件开头
    f.write(temp)
```

###### 处理二进制文件
```python
def is_gif(fname):
    f = open(fname, 'br') #二进制读取模式
    first4 = tuple(f.read(4)) # 调用f.read(n)来读取接下来的n个字节
    return first4 == (0x47, 0x49, 0x46, 0x38)
```
与文本文件一样,二进制文件对象也使用文件指针来记录接下来应该读取文件的哪个字节

**pickle**
pytho模块pickle执行的操作通常被称为对象串行化(简称串行化).基本思想是将复杂的数据结构转换为字节流,即创建数据结构的串行化表示.
在处理二进制方面,pickle通常方便的多,能轻松读写任何数据结构:
```python
import pickle
def make_pickled_file():
    grades = {'alan' : [4, 8, 10, 10],
              'tom' : [7, 7, 7, 8],
              'dan' : [5, None, 7, 7],
              'may' : [10, 8, 10, 10]}
    outfile = open('grades.dat', 'wb')
    pickle.dump(grades, outfile)

def get_pickled_data():
    infile = open('grades.dat', 'rb')
    grades = pickle.load(infile)
    return grades
```
基本上,可以使用pickle.dump将数据结构存储到磁盘,以后再使用pickle.load从磁盘获得数据结构.因此每当需要存储二进制数据时,都应考虑使用这种功能.
还可使用pickle存储函数
pickle不能用于读写特殊格式的二进制文件如gif,对于这样的文件必须逐字节处理.
python包含一个名为shelve的模块,该模块提供了存储和检索数据的高级方式.

###### 读取网页
用模块urllib可读取网页:
```python
import urlib.request
page = urlib.request.urlopen('http://www.python.org')
html = page.read()
```





