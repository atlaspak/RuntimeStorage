from Storage import Storage
from CommandLiner import CommandLiner

class CommandManager:
    def __init__(self):
        self.db = Storage()
        self.transaction_db = Storage()
        self.in_transaction = False
        self.terminal = CommandLiner()
        self.command_list = {
            "GET": { "count": 2, "function": self.get},
            "SET": { "count": 3, "function": self.set},
            "UNSET": { "count": 2, "function": self.unset},
            "NUMEQUALTO": { "count": 2, "function": self.numequalto},
            "END": { "count": 1, "function": self.end},
            "BEGIN": { "count": 1, "function": self.begin},
            "COMMIT": { "count": 1, "function": self.commit},
            "ROLLBACK": { "count": 1, "function": self.rollback}
        }
        
    def get_command_list(self):
        return self.command_list

    def get(self, *args):
        if(self.in_transaction):
            print("In transaction")
            self.terminal.print(self.transaction_db.get(args[0][1]))
        else:
            self.terminal.print(self.db.get(args[0][1]))

    def set(self, *args):
        if(self.in_transaction):
            self.transaction_db.add(args[0][1], args[0][2])
            self.terminal.print("Transaction Key Added")
        else:
            self.db.add(args[0][1], args[0][2])
            self.terminal.print("Key Added")
    
    def unset(self, *args):
        if(self.in_transaction):
            if self.transaction_db.delete(args[0][1]):
                self.terminal.print("Transaction Key Deleted")
                return
        else:
            if self.db.delete(args[0][1]):
                self.terminal.print("Key Deleted")
                return
        self.terminal.print("No key found")
    
    def numequalto(self, *args):
        if(self.in_transaction):
            print("In transaction")
            self.terminal.print(self.transaction_db.get_count(args[0][1]))
        else:
            self.terminal.print(self.db.get_count(args[0][1]))
    
    def end(self, *args):
        self.terminal.print("Bye")
        self.terminal.exit()
    
    def begin(self, *args):
        self.in_transaction = True
        self.terminal.print("Transaction Started")
    
    def commit(self, *args):
        self.in_transaction = False
        self.db.merge(self.transaction_db)
        self.terminal.print("Transaction Merged")
    
    def rollback(self, *args):
        self.transaction_db.clear()
        self.terminal.print("Transaction Cleared")
