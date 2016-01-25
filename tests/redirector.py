# -*- coding: utf-8 -*-
import unittest

import filecmp
import os
import tempfile

from redirector import VariableOutputRedirector
from redirector import FileOutputRedirector


class OutputRedirectionTest(unittest.TestCase):
    def testOutputRedirection(self):
        with VariableOutputRedirector() as out:
            print("line1")
            print("line2")
            value = out.getvalue()

        self.assertEqual("line1\nline2\n", value)

        redirected_file = os.path.join(tempfile.gettempdir(),
                                       "redirected_file.txt")
        correct_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "static", "output_redirection_test",
                                    "correct_file_redirection.txt")
        with FileOutputRedirector(redirected_file) as out:
            print("line3")
            print("line4")
            print("line5")

        self.assertTrue(filecmp.cmp(redirected_file, correct_file, True))
        os.remove(redirected_file)


if __name__ == "__main__":
    unittest.main(verbosity=2)
