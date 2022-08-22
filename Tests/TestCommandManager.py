import unittest
from unittest.mock import Mock
from CommandManager import CommandManager
from Mocks.CommandLinerMock import MockCommandLiner

class TestCommandManager(unittest.TestCase):
    def test_init_db(self):
        commandManager = CommandManager()
        self.assertIsNotNone(commandManager.db)
    
    def test_init_transaction_db(self):
        commandManager = CommandManager()
        self.assertIsNotNone(commandManager.transaction_db)
    
    def test_init_transaction_default_transaction_state(self):
        commandManager = CommandManager()
        self.assertEqual(commandManager.in_transaction, False)

    def test_init_terminal(self):
        commandManager = CommandManager()
        self.assertIsNotNone(commandManager.terminal)
    
    def test_command_list(self):
        commandManager = CommandManager()
        self.assertEqual(len(commandManager.get_command_list()), 8)

    def test_set(self):
        commandManager = CommandManager()
        mock = Mock()
        commandManager.terminal = mock
        test_param = [
            "SET",
            1,
            2
        ]
        commandManager.set(test_param)
        mock.print.assert_called_once_with("Key Added")

    def test_set(self):
        commandManager = CommandManager()
        mock = Mock()
        commandManager.terminal = mock
        test_param = [
            "SET",
            1,
            2
        ]
        commandManager.set(test_param)
        commandManager.get(test_param)
        mock.print.assert_called_with(2)

    def test_unset(self):
        commandManager = CommandManager()
        mock = Mock()
        commandManager.terminal = mock
        test_param = [
            "SET",
            1,
            2
        ]
        commandManager.set(test_param)
        commandManager.unset(test_param)
        mock.print.assert_called_with("Key Deleted")

    def test_unset_nokey(self):
        commandManager = CommandManager()
        mock = Mock()
        commandManager.terminal = mock
        test_param = [
            "SET",
            1,
            2
        ]
        commandManager.unset(test_param)
        mock.print.assert_called_with("No key found")

    def test_unset_end(self):
        commandManager = CommandManager()
        mock = Mock()
        commandManager.terminal = mock
        commandManager.end()
        mock.print.assert_called_with("Bye")
    
    def test_unset_begin(self):
        commandManager = CommandManager()
        mock = Mock()
        commandManager.terminal = mock
        commandManager.begin()
        mock.print.assert_called_with("Transaction Started")

    def test_unset_commit(self):
        commandManager = CommandManager()
        mock = Mock()
        commandManager.terminal = mock
        commandManager.commit()
        mock.print.assert_called_with("Transaction Merged")
        
    def test_unset_rollback(self):
        commandManager = CommandManager()
        mock = Mock()
        commandManager.terminal = mock
        commandManager.rollback()
        mock.print.assert_called_with("Transaction Cleared")
    
    def test_check_transaction (self):
        commandManager = CommandManager()
        mock = Mock()
        commandManager.terminal = mock
        commandManager.begin()
        commandManager.set(["SET", 2,3])
        mock.print.assert_called_with("Transaction Key Added")

    def test_check_transaction_merged(self):        
        commandManager = CommandManager()
        mock = Mock()
        commandManager.terminal = mock
        commandManager.begin()
        commandManager.set(["SET", 2,3])
        commandManager.commit()
        commandManager.get(["GET", 2])
        mock.print.assert_called_with(3)
        