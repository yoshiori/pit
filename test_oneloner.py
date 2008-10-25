import unittest, pit_oneliner

class PitTestCase(unittest.TestCase):
    def test_set_get(self):
        pit_oneliner.set("test", {'data':{'username':'foo','password':'bar'}})
        self.assertEqual("foo", pit_oneliner.get("test")["username"] )
        self.assertEqual("bar", pit_oneliner.get("test")["password"] )

        pit_oneliner.set("test2", {'data' : {"username":"foo2","password":"bar2"}})
        self.assertEqual( "foo2", pit_oneliner.get("test2")["username"])
        self.assertEqual( "bar2", pit_oneliner.get("test2")["password"])
        
        pit_oneliner.set("test", {'data' : {"username":"foo","password":"bar"}})
        self.assertEqual( "foo", pit_oneliner.get("test")["username"])
        self.assertEqual( "bar", pit_oneliner.get("test")["password"])

        self.assertEqual( "foo", pit_oneliner.set("test",{'data':{"username":"foo","password":"bar"}})["username"])
if __name__ == "__main__":
        unittest.main()
