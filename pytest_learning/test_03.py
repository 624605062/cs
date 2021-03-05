import pytest
@pytest.fixture(scope='module')
def open():
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
    pytest.main(['-s','test_03.py'])
