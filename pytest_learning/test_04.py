import pytest
'''@pytest.mark.webtest
def test_send_http():
    pass
def test_something_quick():
    pass
class TestClass():
    def test_method(self):
        pass
if __name__ == "__main__":
    pytest.main(["-v", "test_04.py::TestClass::test_method"])
canshu=[{'user':'admin','psw':'123'}]
@pytest.fixture(scope='module')
def login(request):
    user=request.param['user']
    psw=request.param['psw']
    print('正在操作登录，账号：%s,密码：%s'%(user,psw))
    if psw:
        return True
    else:
        return False
@pytest.mark.parametrize('login',canshu,indirect=True)
class Test_xx():
    def test_001(self,login):
        result=login
        print('用例1：%s'%result)
        assert result==True

    def test_02(self, login):
        result = login
        print("用例 3,登录结果：%s" % result)
        if not result:
            pytest.xfail("登录不成功, 标记为 xfail")
        assert 1 == 1

    def test_03(self, login):
        result = login
        print("用例 3,登录结果：%s" % result)
        if not result:
            pytest.xfail("登录不成功, 标记为 xfail")

        assert 1 == 1
if __name__ == '__main__':
    pytest.main(['-s','test_04.py'])
#测试登录数据
test_login_data=[('admin','11111'),('admin','')]
def login(user,psw):
    print('登录账户：%s'%user)
    print('登录密码：%s'%psw)
    if psw:
        return True
    else:
        return False
@pytest.mark.parametrize('user,psw',test_login_data)
def test_login(user,psw):
    result=login(user,psw)
    assert result==True,'失败原因：密码为空'
if __name__ == '__main__':
    pytest.main(['-s','test_04.py'])'''
'''test_user_data=['admin1','admin2']
@pytest.fixture(scope='module')
def login(request):
    user=request.param
    print('登录账户：%s'%user)
    return user
@pytest.mark.parametrize('login',test_user_data,indirect=True)
def test_login(login):
#登录用例
    a=login
    print('测试用例中login的返回值：%s'%a)
    assert a!=''
if __name__ == '__main__':
    pytest.main(['-s','test_04.py'])'''
'''test_user_data = [{"user": "admin1", "psw": "111111"},
                  {"user": "admin1", "psw": ""}]
@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw = request.param["psw"]
    print("登录账户：%s" % user)
    print("登录密码：%s" % psw)
    if psw:
        return True
    else:
        return False
# indirect=True 声明 login 是个函数
@pytest.mark.parametrize("login", test_user_data,
indirect=True)
def test_login(login):
#登录用例
    a = login
    print("测试用例中 login 的返回值:%s" % a)
    assert a, "失败原因：密码为空"'''
'''test_user = ["admin1", "admin2"]
test_psw = ["11111", "22222"]
@pytest.fixture(scope="module")
def input_user(request):
    user = request.param
    print("登录账户：%s" % user)
    return user
@pytest.fixture(scope="module")
def input_psw(request):
    psw = request.param
    print("登录密码：%s" % psw)
    return psw
@pytest.mark.parametrize("input_user", test_user,indirect=True)
@pytest.mark.parametrize("input_psw", test_psw, indirect=True)
def test_login(input_user, input_psw):
#登录用例
    a = input_user
    b = input_psw
    print("测试数据 a-> %s， b-> %s" % (a, b))
    assert b
def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    assert 0 # to see what was printed
if __name__ == "__main__":
    pytest.main(["-s", "test_04.py"])'''


'''@pytest.mark.webtest
def test_send_http():
    print("mark web test")
def test_something_quick():
    pass
def test_another():
    pass
@pytest.mark.hello
class TestClass:
    def test_01(self):
        print("hello :")
    def test_02(self):
        print("hello world!")
if __name__ == "__main__":
    pytest.main(["-v", "test_04.py","-m=hello"])'''


'''def test_hello():
    print("hello world!")
    assert 1


@pytest.mark.xfail()
def test_yoyo1():
    a = "hello"
    b = "hello world"
    assert a == b


@pytest.mark.xfail()
def test_yoyo2():
    a = "hello"
    b = "hello world"
    assert a != b'''
'''>>> multiply(4, 3)
    12
>>> multiply('a', 3)
    'aaa'
def multiply(a,b):
    """
    fuction: 两个数相乘
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a*b
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)'''
'''for a in range(1,3):
    print(a)'''
'''@pytest.fixture()
def user():
    print('获取用户名')
    a='lwj'
    #b='123456'
    #assert a=='lwj11'#在fixture里断言失败就是error
    return a
@pytest.fixture()
def psw():
    print('获取密码')
    b='123456'
    return b
def test_01(user,psw):
    #传入多个fixtuer
    print('测试账户：%s,密码：%s' %(user,psw))
    assert user=='lwj'#如果断言失败就是failed'''
'''@pytest.fixture()
def first():#定义第一个fixture函数
    print('获取用户名')
    a='lwj'
    return a
@pytest.fixture()
def sencond(first):#定义第二个fixture调用第一个first方法
    a=first
    b='123546'
    return (a,b)
def test_01(sencond):#传入sencond函数 其中调用了first函数方法
    print('测试账户：%s,密码：%s' % (sencond[0], sencond[1]))
    assert sencond[0]=='lwj'''
'''@pytest.fixture()
def first():
    print("\n 获取用户名")
    a = "yoyo"
    return a
@pytest.fixture(scope="function")
def sencond():
    print("\n 获取密码")
    b = "123456"
    return b
class TestCase():
    def test_1(self, first):#用例传 fixture
        print("测试账号：%s" % first)
        assert first == "yoyo"
    def test_2(self, sencond):#用例传 fixture
        print("测试密码：%s" % sencond)
        assert sencond == "123456"'''
'''@pytest.fixture(scope='module')
def first():
    print("\n 获取用户名,scope 为 module 级别当前.py 模块只运行一次")
    a = "yoyo"
    return a
def test_1(first):#用例传 fixture
    print("测试账号：%s" % first)
    assert first == "yoyo"
#def test_2(first):#用例传 fixture
    #print("测试密码：%s" % first)
    #assert first == "yoyo"
class TestCase():
    def test_2(self, first):#用例传 fixture
        print("测试账号：%s" % first)
        assert first == "yoyo"'''
def test_1(first):#用例传 fixture
    print("测试账号：%s" % first)
    assert first == "yoyo"
if __name__ == '__main__':
    pytest.main(['-s','test_04.py'])
