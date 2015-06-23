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
            print("linea1")
            print("linea2")
            value = out.getvalue()

        self.assertEqual("linea1\nlinea2\n", value)

        redirected_file = os.path.join(tempfile.gettempdir(), "redirected_file.txt")
        correct_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "static", "output_redirection_test", "correct_file_redirection.txt")
        with FileOutputRedirector(redirected_file) as out:
            print("linea3")
            print("linea4")
            print("linea5")

        self.assertTrue(filecmp.cmp(redirected_file, correct_file, True))
        os.remove(redirected_file)


if __name__ == "__main__":
    unittest.main(verbosity = 2)
