# coding: utf-8

import unittest
import test_column

suite = unittest.TestLoader().discover('.')
unittest.TextTestRunner(verbosity=2).run(suite)
