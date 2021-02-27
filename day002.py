#########################类
'''class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+'is now sitting')
    def roll_over(self):
        print(self.name.title()+'rolled over!')'''
'''def city_s(city,country,population=''):
    if population:
        return city+','+country+'- population'+str(population)
    else:
        return city+','+country'''

'''class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    def __init__(self,question):
        self.question=question
        self.responses=[]
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    def store_responses(self):
        """存储单份调查问卷"""
        self.responses.append(new_responses)
    def show_results(self):
        """显示所有问卷"""
        print("所有问卷为：")
        for response in self.responses:
            print("-"+response)'''
'''class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
    def show_question(self):
        """显示调查问卷"""
        print(question)
    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)
    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
    for response in self.responses:
        print('- ' + response)'''

'''class Employee():
    def __init__(self,firstname,lastname,job=0):
        self.firstname=firstname
        self.lastname=lastname
        self.job=job
    def give_raise(self,salary=5000):
        self.job+=salary
        return salary
import unittest
class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.longwj=Employee('long','wj',5000)
    def test_give_default_raise(self):
        names=self.longwj.give_raise()
        self.assertEqual(names,5000)
    def test_give_custom_raise(self):
        ournames=self.longwj.give_raise(6000)
        self.assertEqual(ournames,16000)
unittest.main()'''
