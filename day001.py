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

'''sz=[value**2 for value in range(0,11,2)]
print(sz)'''
'''cslist=['a','b','c']
for cs in cslist[:2]:#遍历输出切片
    print(cs)
print(cslist[2:3])#切片输出
cs2list=cslist[:]#复制整个列表
cs2list.append('d')#复制的列表中添加元素
print(cs2list)'''

############################元组
'''dimensions = (200, 50)#定义元组
print("遍历元组:")
for dimension in dimensions:#元组的遍历
    print(dimension)
dimensions=(400,100)
print("\n修改元组变量")
for dimension in dimensions:
    print(dimension)'''

    ########################if语句

'''cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car=="bmw":#先检查当前的汽车名是否是'bmw'
        print(car.upper())
    else:
        print(car.title())'''

'''age=18
if age>=18:
    print("已成年")
else:
    print("未成年")
'''

'''cslist=['a','b','c']
if 'a' not in cslist:#判断在不在列表中
    print("存在")
else:
    print("不存在")'''

'''car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')'''
####练习
'''str1="bmw"
str2="Bmw"
if str1==str2:#检查两个字符串相等和不等
    print("一样")
else:
    print('不一样')'''

'''sz1=52
sz2=52
if sz1 and sz2 >=10:
    print('大于10')
else:
    print('小于10')'''
'''if sz2 or sz1 <=50:
    print('大于50')
else:
    print('小与50')'''

#if elif else 语句
'''age=19
if age<=18:
    print('少年')
elif age<=28:
    print('青年')
else:
    print('老年')'''
'''wxr='creen'
if wxr=='green':
    print('获得5分')
else:
    print('获得10分')'''
'''names=['a']
if names:
    for name in names:#遍历每一位成员
        print("存在个用户")
else:
    print("没有用户")'''
'''if name=='admin':#判断是不是管理员
        print(name+"你好管理员")
    else:
        print(name+'你好')
    if name1:
        print("没有用户")
    else:
        print("存在"+len(name1)+",个用户")'''

'''current_users=['a','b','c','d']
new_users=[1,2,3,4,'a','b']
for new_user in new_users:
    if new_user in current_users:
        print(new_user+'用户已存在')
    else:
        print("可以使用")'''

'''numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    int=number
    if number==1:
        print(str(number)+"st")#在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输出内容应为1st 、2nd 、3rd 、4th 、5th 、6th 、7th 、8th 和9th ，但每个序
数都独占一行。

    elif number==2:
        print(str(number)+'nd')
    elif number==3:
        print(str(number)+'rd')
    else:
        print(str(number)+'th')'''


#########################字典
'''zidian={}
zidian['a']=1
zidian['b']=2
zidian['a']=20
print(zidian)
del zidian['a']
print(zidian)'''
#遍历字典中的数据

'''user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key,value in user_0.items():#将遍历的它返回一个键—值对列表
    print("\nKey:"+key)
    print("Value:"+value)'''
'''favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
", I see your favorite language is " + favorite_languages[name].title() + "!")
'''
'''favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for language in set(favorite_languages.values()):#使用集合去重复保证值的独一无二
    print(language.title())

for name in sorted(favorite_languages.keys()):#顺序排序遍历字典中的键
    print(name)'''

##练习
'''heliu={'nile':'egypt',
        'dahe':'laile',
       'nih':'hhhj',
        }
for hl in heliu.values():
    print(hl)
#for hl in heliu.keys():
  #  print(str(hl)+'The Nileruns throughEgypt')'''
####嵌套
# 创建一个用于存储外星人的空列表
'''aliens = []
# 创建30个绿色的外星人
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#print(aliens[0:3])
for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='fast'
for alien in aliens[0:5]:
    print(alien)
print('....')'''

'''pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
for pizzas in pizza['toppings']:#遍历字典中的列表
    print(pizzas)'''
#元组中嵌套元组
'''users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username, user_info in users.items():#循环遍历键和值 存在在变量username, user_info中
    print("\nUsername: " + username)#输出键
    full_name = user_info['first'] + " " + user_info['last']#定义变量 full_name，其中包含user_info['first']user_info['last']的值
    location = user_info['location']#定义变量包含user_info['location']的值
print("\tFull name: " + full_name.title())
print("\tLocation: " + location.title())'''

####练习
#：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets 的列表中，再遍历该列表，并将宠物的所有信息都打印出来。
'''cat={"name":'james','leixi':'maomi'}
dog={"name":'ali','leixi':'go'}
monkey={"name":'mrst','leixi':'houzi'}
dongwus=[cat,dog,monkey]#将字典放在列表中
for dongwu in dongwus:
    for dwn,dwlx in dongwu.items():
        print(dwn+dwlx)'''
# ：创建一个名为favorite_places 的字典。在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个地方。为让这个练习更有趣些，可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。

'''favorite_places={'james':['beij','changsha','wuhan'],
                 'aili':['nanc','shanghai','chongq'],
                 }
for k,v in favorite_places.items():#遍历人名 和列表
    print(k)
    for i in v:#遍历列表
        print("\t%s" % i)'''

'''cities={'nanchang':{'renkou':'50万','chepai':'赣A'},
        'shanghai':{'人口':'100万','chepai':'沪A'},
        }
for k,v in cities.items():
    print(k)
    for key,values in v.items():
        print(key+':'+values)'''




#####用户输入和while 循环
'''username=input("请输入用户名；")
password=input("请输入密码：")
if username=='cs':
    password=='123'
    print('登录成功')
else:
    print('登录失败')'''

'''number=input("请输入数字：")
number=int(number)
if number %2==0:
    print('是偶数')
else:
    print('是奇数')'''
'''number=1
while number <=100:#循环到100次
    print(number)
    number +=1#每次循环都自增1  +1'''

'''prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)'''

######练习
'''pisa='请输入你想要的披萨材料：'

while pisa:
    pisas=input(pisa)
    if pisas=='quit':
        break
    else:
        print("我们会为你添加："+str(pisas)+'的')'''
'''pj=input("请输入你的年龄：")
pj=int(pj)
while pj:
    if pj <= 3:
        print('免费')
        break
    elif pj<=12:
        print('10元')
        break
    else:
        print('12元')
        break'''






