import pytest
def test_s1(login):
    print('用例1，登录之后其他动作111')
def test_s2():#不传login
    print('用例2，不需要登录操作222')
def test_s3(login):
    print('用例3，登录之后其他动作333')
if __name__ == '__main__':
    pytest.main(['-s','test_03.py'])
