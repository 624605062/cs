#print("hellO,word!")#输出语句
'''x="a"
y="b"
# 换行输出
print(x)
print(y)
不换行输出
print (x,y)'''
'''a, b, c = 1, 2, "john"
print(a)
print(b)
print(c)
'''



'''var=1
var1=10
str="hello world"
print(str[0])# 输出字符串中的第一个字符
print(str[0:2])# 输出字符串中第一个至第三个之间的字符串'''
'''list=['hello',10,2.333]
tinylist=[123,'word']
print(list[0:2])
print(tinylist*2)# 输出列表两次
print(list+tinylist) # 打印组合的列表'''



'''tuple=('nh',10,20,'llll')
tinytuple=(10,'cccc')
list=['lll',456]
print (tuple)               # 输出完整元组
print (tuple[0])            # 输出元组的第一个元素
print (tuple[1:3])          # 输出第二个至第四个（不包含）的元素
print (tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print (tinytuple * 2 )      # 输出元组两次
print (tuple + tinytuple)   # 打印组合的元组
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用
print(list)'''



'''dict={}
dict['One']='this is One'
dict[2]='this is two'
tinydict={'name':'sss','ID':10,'Dept':20,}
print (dict['One'])          # 输出键为'one' 的值
print (dict[2])              # 输出键为 2 的值
print (tinydict)             # 输出完整的字典
print (tinydict.keys())      # 输出所有键
print (tinydict.values())    # 输出所有值'''



'''a=10
b=20
def sum(a,b):
    return a+b#符合要求

print(sum(10,20))'''

#input('\n\n按下 enter键后退出')
'''import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)'''

'''age=input('请输入你的年龄：')
age1=int(age)
print('我的年龄是：%d'%age1)#%r可以代表任意数据类型 %s 字符串 %d数字
'''
'''def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
print (list[1:3])       # 从第二个开始输出到第三个元素
# 获得结果 [786, 2.23]


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)'''

'''sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu',}

print(sites)   # 输出集合，重复的元素被自动去掉
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a 和 b 的差集

print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素'''
'''def test(*args):
    print(args)
    return args

print(type(test(1,2,3,4)))'''

'''def example(d):
    dict[d] = {1, 2}
    # d 是一个字典对象
    for c in d:
        print(c)
        #如果调用函数试试的话，会发现函数会将d的所有键打印出来;
        #也就是遍历的是d的键，而不是值.'''
'''a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b  # 12 = 0000 1100
print("1 - c 的值为：", c)'''
'''name='Long'
name1=name.title()
name2=name.upper()
name3=name.lower()
print(name1,name2,name3)

str="Longwj Say ,“Apersonwho never madea mistake never tried anything new.”"
print(str)
str1="\n longwj   "
print(str1)
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())'''

'''namelist=['as1','as2']
namelist.insert(3,'as5')#在列表中插入元素
print(namelist)
namelist.append('as3')#给列表增加元素
print(namelist)'''

'''namelist=['a1','a2','a3','a4']
namepop=namelist.pop()#默认弹出末尾的值 从列表删除后依然可以弹出使用
namepop2=namelist.pop(2)
print("很遗憾：",namepop,"我们无法邀请你来参加晚宴")
print("很遗憾：",namepop2,"我们无法邀请你来参加晚宴")
namelist2=namelist.remove('a1','a2')#删除列表中的元素
print(namelist2)'''

'''namelist=['c1','d2','b3','a4']
namelist.sort()#字母顺序进行排序
print(namelist)
namelist2=['c1','a2','b3','d4']
namelist2.sort(reverse=True)#反方向排序
print(namelist2)'''

'''cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))#临时将列表进行排序操作 此操作是临时的 
print("\nHere is the original list again:")
print(cars)'''

'''cars = ['bmw', 'audi', 'toyota', 'subaru']
len1=len(cars)# 确定列表的长度 使用函数len() 可快速获悉列表的长度
print(len1)
print(cars)
cars.reverse()#反向打印       reverse() 不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序：
print(cars)'''

'''wanttogo=["beijin","changsha","ai"]
print(wanttogo)
wanttogo1=sorted(wanttogo)
print(wanttogo1)
wanttogo2=wanttogo1
wanttogo2.reverse()
print(wanttogo2)
print(wanttogo)
wanttogo.sort()
print(wanttogo)'''


'''gsname=['hh','zj','xzq']
for gsnames in gsname:
    print(gsnames)'''

'''squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)'''
'''sz=[]
for value in range(1,100000):
    sz.append(value)
print(sz)
max1=max(sz)
print(max1)'''

'''numbers=list(range(3,30,3))
print(numbers)
for number in numbers:
    print(number)
'''
'''numbers=[number**3 for number in range(1,11)]
print(numbers)
szu=[]
numbers=list(range(1,11))
for number in numbers:
    sz=number**3
    szu.append(sz)
print(szu)'''