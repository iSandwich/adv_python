import unittest
from unittest.mock import patch
import new_template
from pprint import pprint


class TestPack(unittest.TestCase):
    # def setUp(self):
    #     self.docs, self.dirs = new_template.program_start()
    #     with patch('new_template.program_start', return_value=(self.docs, self.dirs)):
    #         with patch('new_template.input', return_value='q'):
    #             catalog.interface()

    def setUp(self):
        self.docs, self.dirs = new_template.program_start()

    def test_delete_doc(self):
        before_len = len(self.docs)
        with patch('new_template.input', return_value='10006'):
            new_template.delete_doc()
        after_len = len(self.docs)
        self.assertLess(after_len, before_len)
