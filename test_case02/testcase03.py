# -*-coding:utf-8-*-
import unittest
class Test03(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_003(self):
        a = 1+2
        print("用例003")
        '''如果a=3那么通过'''
        self.assertEqual(a,2)

if __name__ == '__main__':
    '''创建组件--可理解为一个容器'''
    suite = unittest.TestSuite()
    '''加载组件--可理解为把用例放到容器里'''
    list1=[Test01("test_003"),Test01("test_001")]
    suite.addTests(list1)
    '''创建一个驱动器--可理解为安装上发动机'''
    runner = unittest.TextTestRunner()
    '''运行发动机'''
    runner.run(suite)

