import unittest
from pit import Pit

class PitTestCase(unittest.TestCase):
    def test_set_get(self):
        Pit.set("test", {'data':{'username':'foo','password':'bar'}})
        self.assertEqual("foo", Pit.get("test")["username"] )
        self.assertEqual("bar", Pit.get("test")["password"] )

        Pit.set("test2", {'data' : {"username":"foo2","password":"bar2"}})
        self.assertEqual( "foo2", Pit.get("test2")["username"])
        self.assertEqual( "bar2", Pit.get("test2")["password"])
        
        Pit.set("test", {'data' : {"username":"foo","password":"bar"}})
        self.assertEqual( "foo", Pit.get("test")["username"])
        self.assertEqual( "bar", Pit.get("test")["password"])

        self.assertEqual( "foo", Pit.set("test",{'data':{"username":"foo","password":"bar"}})["username"])

    def test_with_mock_editor(self):
        import os
        ORIGINAL_EDITOR = os.environ.get('EDITOR')
        os.environ["EDITOR"] = "./mock_editor.py"
        conf = Pit.get('test', 
                       {'require': 
                        {'login': 'your ID', 
                         'passwd': 'GoMa'}})
        os.environ["EDITOR"] = ORIGINAL_EDITOR


if __name__ == "__main__":
        unittest.main()
