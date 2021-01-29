import pytest


def setup_module():
    print("setup_module")


def teardown_module():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def setup():
    print("setup")


def teardown():
    print("teardown")


def test_one():
    print("test_one")

#——————————————————————————————————————————————————————————
test_setup_and_teardowm.py
# setup_module
# setup_function
# setup
# test_one
# .teardown
# teardown_function
# teardown_module