import pytest
'''def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="myoption: type1 or type2"
    )
@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")'''
@pytest.fixture(scope="session")
def first():
    print("\n 获取用户名,scope 为 session 级别多个.py 模块只运行一次")
    a = "yoyo"
    return a
