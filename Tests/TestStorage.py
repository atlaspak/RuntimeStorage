import unittest
from Storage import Storage

class TestStorage(unittest.TestCase):
    def test_init_dict(self):
        storage = Storage()
        self.assertIsNotNone(storage.dict)
    
    def test_init_cnt(self):
        storage = Storage()
        self.assertIsNotNone(storage.ctr)
    
    def test_add_data(self):
        storage = Storage()
        test_key = 1
        test_val = 2
        storage.add(test_key,test_val)
        self.assertEqual(storage.get(test_key), test_val)

    def test_check_val_count(self):
        storage = Storage()
        test_key_1 = 1
        test_key_2 = 2
        test_val = 2
        storage.add(test_key_1,test_val)
        storage.add(test_key_2,test_val)
        self.assertEqual(storage.get_count(2), 2)

    def test_check_delete(self):
        storage = Storage()
        test_key = 1
        test_val = 2
        storage.add(test_key,test_val)
        storage.delete(test_key)
        self.assertEqual(storage.get_count(2), 0)
    
    def test_check_data_cleared(self):        
        storage = Storage()
        test_key = 1
        test_val = 2
        storage.add(test_key,test_val)
        storage.add(test_val,test_key)
        storage.clear()
        self.assertEqual(storage.get_count(2), 0)
    