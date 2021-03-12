import pytest
@pytest.fixture(scope='module',autouse=True)
def start(request):
    print('\n----开始执行module--------')
    print('module   :%s' % request.module.__name__)
    print('---启动浏览器--')
    yield
    print('-----结束测试----')
@pytest.fixture(scope='function',autouse=True)
def open_home(request):
    print('function:%s\n------回到首页----'% request.function.__name__)
def test_01(self)
    print('---用例01----')
def test_02(self)
    print('---用例02---')
if __name__ == '__main__':
    pytest.main(['-s','test_03.py'])



'''def open():
    print('打开浏览器，并且打开百度')
    yield
    print('执行teardown')
    print('最后关闭浏览器')
def test_s1(open):
    raise NameError
def test_s2(open):#不传login
    print('用例2，不需要登录操作222')
def test_s3(open):
    print('用例3，登录之后其他动作333')
if __name__ == '__main__':
    pytest.main(['-s','test_03.py'])'''
