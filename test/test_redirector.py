# -*- coding: utf-8 -*-
from __future__ import print_function

import unittest

import filecmp
import os
import tempfile

from redirector import VariableOutputRedirector
from redirector import FileOutputRedirector


class OutputRedirectionTest(unittest.TestCase):
    def testVariableOutputRedirection(self):
        with VariableOutputRedirector() as out:
            print('line1')
            print('line2')
            value = out.getvalue()

        self.assertEqual('line1\nline2\n', value)

    def testFileOutputRedirection(self):
        redirected_file = tempfile.NamedTemporaryFile().name
        correct_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    'static', 'output_redirection_test',
                                    'correct_file_redirection.txt')
        with FileOutputRedirector(redirected_file):
            print('line3')
            print('line4')
            print('line5')

        print(redirected_file)
        print(correct_file)
        self.assertTrue(filecmp.cmp(redirected_file, correct_file, True))


if __name__ == '__main__':
    unittest.main()
