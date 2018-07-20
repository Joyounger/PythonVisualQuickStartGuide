
```python
class Person:
    """Class to repersent a person
    """
    def __init__(self):
        self.name = ''
        self.age = 0

p = Person()
```
上述代码定义了一个名为Person的类.它定义了Person对象包含的数据和函数.Person类很简单,它包含数据name和age.当前唯一一个函数是__init__,这是用于初始化对象值的标准函数
创建Person对象时,Python将自动调用__init__.
类中定义的函数被称为方法.与__init__一样,方法的第一个参数必须是self
要创建Person对象,只需调用Person().这导致Python运行Person类的函数__init__,并返回一个新的Person对象.

Python自动给每个对象添加特殊变量self,self指向对象本身
所有类都应该有方法__init__(self),这个方法的职责是初始化对象,仅在对象被创建时调用一次.
特殊方法__str__返回对象的字符串表示.__repr__返回对象的官方表示大多数类中,__repr__和__str__相同.
创建自己的类和对象时,编写函数__str__和__repr__总是值得的.它们对于显示对象的内容很有帮助,而显示对象的内容有助于调试程序.
如果定义了__repr__,但没有定义__str__,则对象调用str时,将执行__repr__.
python官方文档建议将对象的字符串表示设置为创建对象所需的代码.

###### 特性装饰器
装饰器是python中的一种通用结构,用于系统地修改既有函数.装饰器通常放在函数开头,并以@字符打头.
特性装饰器集变量的简洁与函数的灵活于一身.装饰器指出函数或方法有点特殊.
获取函数返回变量的值,我们将使用@property装饰器指出这一点:
```python
def age(self):
    """ return this person's age
    """
    return self._age
```
修改后的person类为:
```python
class Person:
    def __init__(self, name = '', age = 0):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age
    
    def set_age(self, age):
        if 0 < age <= 150:
            self._age = age

    def display(self):
        print(self)

    def __str__(self):
        return "Person('%s', %s)" % 
             (self._name, self._age)

    def __repr__(self):
        return str(self)

    @age.setter
    def age(self, age):
        if 0 < age <= 150:
            self._age = age
```
为降低变量self._age被直接修改的可能性,一种方式是将其重命名为self.__age,即在变量名开头包含两个下划线.两个下划线表明age是私有变量,不应在Person类外直接访问它.
要直接访问self.__age,需要在前面加上_Person:
p._Person__age = -44
这样虽然不能禁止直接修改内部变量,但将无意间这样做的可能性几乎降低到了0.
不以下划线打头的变量是公有变量,任何代码都可访问它们.

编写大型程序时,一条使用经验是先将所有变量对象都设置为私有的,再在有充分理由的情况下将其改为公有的.这可避免无意间修改对象内部变量导致的错误.

###### 继承
```python
class Player:
    def __init__(self, name):
        self._name = name
        self._score = 0
    def reset_score(self):
        self._score = 0
    def incr_score(self):
        self._score = self._score + 1
    def get_name(self):
        return self._name
    def __str__(self):
        return "name = '%s', score = %s"
          % (self._name, self._score)
    def __repr__(self):
        return 'Player(%s)' % str(self)

class Huamn(Player): #让human类继承player类的所有变量和方法
    pass

class Huamn(Player): # 重写方法
    def __repr__(self):
        return 'Human(%s)' % str(self)
class Computer(Player): # 重写方法
    def __repr__(self):
        return 'Computer(%s)' % str(self)
```
python中pass表示什么都不做.


######　多态
```python
def play_undercut(p1, p2):
    p1.reset_score()
    p2.reset_score()
    m1 = p1.get_mov()
    m2 = p2.get_mov()
    print('%s move: %s' %  (p1/get_name(), m1))
```
