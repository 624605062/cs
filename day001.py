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

'''n=0
while n < 10:
    n+=1
    if n %2 == 0:
        continue#忽略对2取余=0的数 也就是忽略偶数
    print(n)'''


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
while pj:#循环用户输入
    if pj <= 3:#对用户输入进行判断
        print('免费')
        break
    elif pj<=12:
        print('10元')
        break
    else:
        print('12元')
        break'''
######## 使用while 循环来处理列表和字典
'''yz_users=['long','he','liu']#创建一个待验证的列表
yzcg_users=[]#创建一个存放验证过了的列表
while yz_users:#循环验证待验证列表
    yz_user=yz_users.pop()#每次循环验证 都弹出该用户
    print('验证的用户名为：'+yz_user)
    yzcg_users.append(yz_user)#验证后添加到空列表中
print("显示所有已验证的用户：")
for yzcg_user in yzcg_users:#遍历已经验证的用户
    print(yzcg_user.title())'''


###假设你有一个宠物列表，其中包含多个值为'cat' 的元素。要删除所有这些元素，可不断运行一个while 循环，直到列表中不再包含值'cat' ，如下所示：

'''dongwu=['cat','dog','mokeny','cat']
print(dongwu)
while 'cat' in dongwu:
    dongwu.remove('cat')
print(dongwu)'''
####使用用户输入来填充字典
##可使用while循环提示用户输入任意数量的信息。下面来创建一个调查程序，其中的循环每次执行
# 时都提示输入被调查者的名字和回答。我们将收集的数据存储在一个字典中，以便将回答同被调查者关联起来：
'''responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
# 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# 将答卷存储在字典中
    responses[name] =response
# 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")'''
#########练习
'''sandwich_orders=['pastrami','a1','a2','a3','pastrami']
finished_sandwiches=[]
while sandwich_orders:
    sandwich_order=sandwich_orders.pop()#循环弹出
    print('I made your tuna sandwich'+sandwich_order)
    finished_sandwiches.append(sandwich_order)#弹出的值添加到空列表
for cs in finished_sandwiches:
    print(cs)'''

'''sandwich_orders=['pastrami','a1','a2','a3','pastrami']
finishs=[]
biao=True
print('五香牛肉都卖完了')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    finishs.append(sandwich_orders)
for f in finishs:
    print(f)'''
###################函数的定义
'''def greet_user():######定义一个函数
    "你好吗"
    print('hello')
greet_user()'''


##################实参和形参
'''def user_cs(username):###username是形参
    print('hello')
user_cs('kall')#实参'''

###############练习
'''def make_shirt(cm,zy='I love Python'):
    print('\n你选择的尺码是：'+cm)
    print('\n你选择的字样是：'+zy)
make_shirt('L')
make_shirt(cm='xl')
make_shirt(cm='XXXL',zy='Fuck')'''

'''def describe_city(name,conture='China'):
    print(name+' is in the '+conture)
describe_city('changsha')
describe_city(name='nanchang')
describe_city(name='dongjin',conture='japen')'''


'''def get_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()
name=get_name('long','wenjie')
print(name)'''

'''def get_name(first_name, last_name, mid_name=''):
    if mid_name:#判断mid_name为ture也就是有数据
        full_name=first_name+' '+mid_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
     return full_name#将值返回导函数
name=get_name('long','wen','jie')
print(name)
names=get_name('long','wenjie')
print(names)'''

##################返回字典
'''def user_name(first,last,age=''):
    name={'firstname':first,'lastname':last}#定义函数值所在的字典
    if age:
        name['age']=age
    return name
names=user_name('long','wenjie',age=18)
print(names)'''

'''def get_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()
while True:
    print('\n请输入你的名字：')
    print('输入q退出')
    f_name=input('你的姓：')
    if f_name=='q':
        break
    l_name=input('你的名：')
    if l_name=='q':
        break
    name=get_name(f_name,l_name)
    print('\n你好！'+name)'''
##########练习
'''def city_country(city,gj):
    print(city+' '+gj)

city_country('changsha','zg')'''

'''def make_album(gs_name,zhuanji_name,gqs=''):
    full_name={'gs':gs_name,'zj':zhuanji_name}
    full_name['gqs']=gqs
    return full_name
while True:
    print('请输入你的数据：')
    print('按q退出')
    gss=input('\n请输入你喜欢的歌手名称： ')
    if gss=='q':
        break
    zjs=input('\n请输入他的专辑： ')
    if zjs=='q':
        break
    gq=input('\n请输入歌曲数： ')
    if gq=='q':
        break
    name=make_album(gss,zjs,gq)
    print(name)'''

########传递列表

'''def get_name(names):#定义一个函数包含形参
    for name in names:遍历参数 
        msg='hello,'+name.title()
        print(msg)
user_name=['long','wen','jie']#定义一个列表
get_name(user_name)#调用函数方法 循环遍历列表的值'''


'''def print_models(unprinted_designs,completed_models):
    """ 模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('打印的模型为：'+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print('\n打印好的模型为：')
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)#，如果不想清空未打印的设计列表 可以切片保存副本
print(unprinted_designs)
show_completed_models(completed_models)'''


#####练习

'''def show_magicians(names):
    for name in names:
        print(name)
def make_great(addnames,names):

    while addnames:
        add='尊敬的魔术师： '+' '+addnames.pop()
        names.append(add)
    return names
mss = ['long', 'wen', 'jie']
n=[]
make_great(mss[:],n)
show_magicians(n)
show_magicians(mss)'''
########################传递任意数量的实参

'''def make_pizza(*topps):#  *topps 表示让函数创建了一个元组 不管输入多少个值都将包含在中国元组中
    print('您选择的配料：')
    for topp in topps:
        print(topp)
make_pizza('火腿','芝士','蔬菜')'''

##########结合使用位置实参和任意数量实参

'''def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')'''


'''def build_profile(first,last,**user_info):#两个星号让Python创建一个名为user_info 的空字典，并将收到的所有名称—值对都封装到这个字典中。
    profile={}#我们创建了一个名为profile 的空字典，用于存储用户简介
    profile['first_name']=first#字典中的key 对应的vlue
    profile['last_name']=last
    for k,y in user_info.items():#遍历字典
        profile[k]=y#并将每个键—值对都加入到字典profile 中。
        return profile
user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)'''
###############练习
'''def make_pizzas(*fulls):
    print('添加的配料：')
    for full in fulls:
        print(full)
pizzs=make_pizzas('火腿肠','鸡蛋')'''

'''def cars_name(name,pinp,**full):
    car={}
    car['name']=name
    car['pinp']=pinp
    for k,y in full.items():
        car[k]=y
    return car
cars=cars_name('兰博基尼LP700','大牛',color='yellow',
               ccs='一百万')
print(cars)'''

'''import pizz
pizz.make_pizzas('火腿肠','鸡蛋')'''

'''from  pizz import cars_name 
user= cars_name('本田','跑车',color='blue',css=100)
print(user)'''

##################类 class
'''class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+'is now sitting')
    def roll_over(self):
        print(self.name.title()+'rolled over!')'''
'''class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):

        print(self.name.title() + " 是一只狗狗.")
    def roll_over(self):

        print(self.name.title() + " 给我坐下!")'''


'''class Dog():
    my_dog=Dog('willie', 6)
    print("My dog's name is " + my_dog.name.title() + ".")
    print("My dog is " + str(my_dog.age) + " years old.")'''
'''class Dog():
    my_dog=Dog('kall',20)
    my_dog.sit()
    my_dog.roll_over()'''
################练习
'''class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print('营业时间为：'+str(self.cuisine_type)+'点!')
    def open_restaurant(self):
        print('正在营业')
class Restaurant():
    my_restaurant=Restaurant('和平饭店','10:00-22:00')
    your_restaurant=Restaurant('寻味四级','11:00-23:00')
    our_restaurant=Restaurant('全聚德','10:00-22:00')
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
    your_restaurant.describe_restaurant()
    our_restaurant.describe_restaurant()'''

'''class User():
    def __init__(self,first_name,last_name,):
        self.first_name=first_name
        self.last_name=last_name
        self.full=full
    def describe_user(self):
        print('你好：'+self.first_name+self.last_name)
    def greet_user(self):
        print('尊敬的：'+self.first_name+'你好!')
user=User('long','wenjie')
user.describe_user()
user.greet_user()'''
#####使用类和实例
'''class Cars():
    def __init__(self,make,model,year):#定义了方法__init__()
        self.make=make
        self.model=model
        self.year=year
    def get_our_name(self):
        full_name=str(self.year)+' '+self.make+' '+self.model
        return  full_name
my_car=Cars('audi','R8','2020')
print(my_car.get_our_name())'''
###############练习

'''class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def get_number_served(self):
        print(str(self.number_served)+'人')
    def increment_number_served(self,rs):
        self.number_served +=rs
    def describe_restaurant(self):
        print(self.restaurant_name)
        print('营业时间为：'+str(self.cuisine_type)+'点!')
    def open_restaurant(self):
        print('正在营业')
my_restaurant=Restaurant('和平饭店','10:00-22:00')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served=20
my_restaurant.get_number_served()
my_restaurant.increment_number_served(20)
my_restaurant.get_number_served()'''


'''class User():
    def __init__(self,first_name,last_name,):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
    def describe_user(self):
        print('你好：'+self.first_name+self.last_name)
    def greet_user(self):
        print('尊敬的：'+self.first_name+'你好!')
user=User('Tony','Stark')
user.describe_user()
for n in range(5):
    user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)'''

'''class add_user():
    def __init__(self,user_name,user_password):
        self.user_name=user_name
        self.user_password=user_password

    def user_init(self):
        user_n=input('请输入账户：')
        user_p=input('请输入密码：')
        if self.user_name==user_n and self.user_password==user_p:
            print('登录成功')
        else:
            print('登录失败')

user=add_user('root','123')
user.user_init()'''

'''class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):###继承Car类的方法
    def __init__(self,make,model,year):#方法__init__() 接受创建Car 实例所需的信息
        super().__init__(make,model,year)#处的super() 是一个特殊函数，帮助Python将父类和子类关联起来。这行代码让Python调用ElectricCar 的父类的方法__init__() ，让ElectricCar 实例包含父类的所有属性。
        self.battery_size=100
    def describe_battery(self):#给子类定义一个新方法
        print('这个汽车的电池容量为：'+str(self.battery_size)+'千瓦')
my_car=ElectricCar('testla','model','2020')
print(my_car.get_descriptive_name())
my_car.describe_battery()'''
############练习
'''class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def get_number_served(self):
        print(str(self.number_served)+'人')
    def increment_number_served(self,rs):
        self.number_served +=rs
    def describe_restaurant(self):
        print(self.restaurant_name)
        print('营业时间为：'+str(self.cuisine_type)+'点!')
    def open_restaurant(self):
        print('正在营业')
class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine_type='ice_cream'):
        super().__init__(name,cuisine_type)
        self.flavors=[]
    def show_ice(self):
        for icer in self.flavors:
            print(icer)
IceCreamStands=IceCreamStand('s')
IceCreamStands.flavors=['a','b']
IceCreamStands.describe_restaurant()
IceCreamStands.show_ice()'''

'''class User():
    def __init__(self,first_name,last_name,):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
    def describe_user(self):
        print('你好：'+self.first_name+self.last_name)
    def greet_user(self):
        print('尊敬的：'+self.first_name+'你好!')
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        for qx in self.privileges:
            print('你的权限为: '+str(qx))
admin=Admin('long','wenjie')
admin.greet_user()
admin.show_privileges()'''

###########导入类
'''import Car
my_car=ElectricCar('testla','model','2020')
print(my_car.get_descriptive_name())
my_car.describe_battery()'''
'''from Car import ElectricCar
my_car=ElectricCar('testla','model','2020')
print(my_car.get_descriptive_name())
my_car.describe_battery()'''

'''from user import  User
from admin import Admin
name=Admin('long','wenjie')
name.show_privileges()'''
'''from collections import OrderedDict
favorite_languages=OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name,languages in favorite_languages.items():
    print(name.title()+'喜欢的语言是'+languages.title())'''

##########练习
'''from random import randint

class Die():
    def __init__(self,sides='6'):###初始化 筛子6个面
        self.sides=sides
    def roll_die(self):#定义一个方法
        for n in range(11):#循环10个数
            print(randint(1,eval(self.sides)),end=' ')
        print(' ')'''

################文件和异常
#关键字with 在不再需要访问文件后将其关闭。
'''with open('pi_digits') as  file_object:#打开文件  函数open()接受参数为打开文件的名称 as  file_object返回在我们所设置的变量中
    contents=file_object.read()#使用read()方法读取数据并存放在contents变量中
    print(contents.rstrip())#rstrip()方法删除末尾的空行'''
'''pi_string=''#定义一个空变量
for line in contents:#遍历整个文件的值
    pi_string+=line.rstrip()#将遍历的行数 赋值给pi_string
print(pi_string)
print(len(pi_string)'''
'''with open('txt_files/filename') as file_name:#使用绝对路径打开文件
    file_read=file_name.read()
    print(file_read.rstrip())'''
'''open_file='D:/aaaa/admin/cs.txt'##读取电脑中的文件
with open(open_file) as bugtxt:
    txtread=bugtxt.read()
    print(txtread)'''
'''file_read='txt_files/filename'
with open(file_read) as file_object:#打开文件
    lines=file_object.read()#读取文本
pi_string=''
for line in lines:#遍历数据
    pi_string+=line.strip()#清除空行后将数据存储在pi_string中
#print(pi_string[:52])#输出前52位
#print(len(pi_string))
birthday=input('请输入你的生日：')
if birthday in line:
    print("你的生日在此文件中")
else:
    print('你的生日不存在该文件中')'''

################练习
'''file_read='txt_files/filename'
with open(file_read) as file_object:
    lines=file_object.read()
pi_file=''
for line in lines:
    pi_file+=line.rstrip()
pi_file.replace('fly','down')
print(pi_file)'''
#文件写入
'''filename='pi_digits'
with open(filename,'w') as file_object:#第二个实参（'w' ）告诉Python，我们要以写入模式 打开这个文件。
    file_object.write("i love he\n")#使用写入方法write()
    file_object.write('i love creating new games\n')#要让每个字符串都单独占一行，需要在write() 语句中包含换行符：'''
#文件附加
'''filename='pi_digits'
with open(filename,'a') as file_object:#'a'为附加方法 不会清空文件
    file_object.write('I also love read books\n')
    file_object.write('I very like eat ice\n')'''

###############练习
'''filename='pi_digit'
adduser=1
while adduser:
    line=input("请输入你的用户名为你添加到文本：")
    print(line + '您好!')
    if line == '#':
        break
    with open(filename, 'a') as file_object:
        file_object.write(line + '\n')'''

'''filename='guest.txt'
adduser=1
while adduser:
    line=input('为何喜欢编程:')
    if line=='q':
        break
with open(filename,'a') as file_object:
    file_object.write(line+'\n')'''
###########异常
'''try:
    print(5/0)
except ZeroDivisionError:
    print('你不能除以0！')'''

'''print('请输入2个数字！')
print('输入q退出')
while True:
    first_number=input('请输入第一个数字：')
    if first_number=='q':
        break
    sencond_number=input('请输入第二个数字：')
    if sencond_number=='q':
        break
    try:
        anser=int(first_number)/int(sencond_number)
    except ZeroDivisionError:
        print('您不能除以0！')
    else:
        print(anser)'''
'''filename='aaa'
try:
    with open(filename) as file_l:
        aa=file_l.read()
except FileNotFoundError:
    msg='sorry,the file'+filename+'不存在'
    print(msg)'''




'''file_name='pi_digit'
try:
    with open(file_name,'rb') as file_book:#打开文件
        js=file_book.read()#读取文件
except FileNotFoundError:
    msg='sorry,the file'+file_name+'不存在'#错误提醒
else:
    words=js.split()#方法split() 以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
    new_words=len(words)#计算words的长度
    print('文本 '+file_name+'大概有 '+str(new_words)+'个字')'''

'''def count_book(filename):
    try:
        with open(filename,'rb') as file_name:
            contents=file_name.read()
    except FileNotFoundError:
        msg='sorry,the file'+filename+'不存在'#错误提醒
    else:
        words = contents.split()  # 方法split() 以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
        new_words = len(words)  # 计算words的长度
        print('文本 ' + filename + '大概有 ' + str(new_words) + '个字')

filename=['pi_digit','pi_digits']
for files in filename:#遍历列表的文件名称
    count_book(files)'''
'''def count_book(filename):
    try:
        with open(filename,'rb') as file_name:
            contents=file_name.read()
    except FileNotFoundError:
        pass#出现错误后之间跳过
    else:
        words = contents.split()  # 方法split() 以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
        new_words = len(words)  # 计算words的长度
        print('文本 ' + filename + '大概有 ' + str(new_words) + '个字')
filename=['ccc','bbb']
for filenames in filename:
    count_book(filenames)'''
#练习
'''print('请输入2个数字：')
addnumber=True
while addnumber:
    first_number=input('请输入第一个数字：')
    if first_number=='q':
        break
    last_number=input('请输入第二个数字：')
    if last_number=='q':
        break
    try:
        numbers = int(first_number) + int(last_number)
    except ValueError:
        msg='输入类型错误！'
        print(msg)
    else:
        print(numbers)'''

'''filename=['txt_files/dats','txt_files/dogs']
for files in filename:
    try:
        with open(files) as f_ojb:
            yd=f_ojb.read()
            print(yd)
    except FileNotFoundError:
        pass
        #msg='未找到 '+files+'的文件！'
       # print(msg)'''
'''filename='txt_files/cats'
with open(filename) as file_obj:
    js=file_obj.read()
    print(js)
    word=js.count('tom')
    print(word)'''

'''import json
number=[1,2,3,4]#创建一个列表
filename='number.json'#创建一个json文件
with open(filename,'w') as file_object:#打开该文件，进行写入
    json.dump(number,file_object)#json.dump()方法将数字列表存储到文件numbers.json中。'''


'''import json
filename='number.json'
with open(filename) as file_object:#打开number.json文件
    numbers=json.load(file_object)#json.load()方法读取文件内容
print(numbers)'''

'''import json
username=input('请输入你的用户名：')#让用户输入用户名
filename='number.json'#写入文件的名称
with open(filename,'w') as f_obj:#打开文件
    json.dump(username,f_obj)#进行文件的写入
    print(username+" 欢迎您回来！")'''
'''import json
filename='number.json'
with open(filename) as f_obj:
    username=json.load(f_obj)
    print('欢迎您！ '+username)'''