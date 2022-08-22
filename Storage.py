from collections import Counter

class Storage:
    def __init__(self):
        self.dict = {}
        self.ctr = Counter()
    
    def add(self, key, value):
        if(key in self.dict):
            self.ctr[self.dict[key]] -= 1
        self.dict[key] = value
        self.ctr[value] += 1
    
    def delete(self, key):
        if key not in self.dict:
            return False
        self.ctr[self.dict[key]] -= 1
        del self.dict[key]
        return True

    def get(self,key):
        if key in self.dict:
            return self.dict[key]

    def clear(self):        
        self.dict = {}
        self.ctr = Counter()
    
    def get_count(self, value):
        return self.ctr[value]

    def merge(self, new_db):
        if new_db.dict:
            for key, value in new_db.dict.items():
                self.add(key, value)
