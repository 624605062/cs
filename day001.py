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

