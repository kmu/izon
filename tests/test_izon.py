import unittest
import os
from izon.izon import *


class TestIzon(unittest.TestCase):
    def setUp(self):
        for idx in range(5):
            with open("tmp_for_test_{}".format(idx), "w") as f:
                f.write("test")

    def tearDown(self):
        for idx in range(5):
            fname = "tmp_for_test_{}".format(idx)
            os.remove(fname)

    def test_old_new(self):
        assert should_run(
            should_old='tmp_for_test_2', 
            should_new='tmp_for_test_1')

        assert not should_run(
            should_old='tmp_for_test_1', 
            should_new='tmp_for_test_2')

    def test_olds_new(self):
        assert not should_run_olds_new(
            should_olds=['tmp_for_test_1', 'tmp_for_test_0'], 
            should_new='tmp_for_test_2')

        assert should_run_olds_new(
            should_olds=['tmp_for_test_1', 'tmp_for_test_3'], 
            should_new='tmp_for_test_2')

        assert should_run_olds_new(
            should_olds=['tmp_for_test_4', 'tmp_for_test_3'], 
            should_new='tmp_for_test_2')


    
    def test_old_news(self):
        assert should_run_old_news(
            should_news=['tmp_for_test_1', 'tmp_for_test_0'], 
            should_old='tmp_for_test_2')

        assert should_run_old_news(
            should_news=['tmp_for_test_1', 'tmp_for_test_3'], 
            should_old='tmp_for_test_2')

        assert not should_run_old_news(
            should_news=['tmp_for_test_4', 'tmp_for_test_3'], 
            should_old='tmp_for_test_2')


    
    def test_olds_news(self):
        assert should_run_olds_news(
            should_news=['tmp_for_test_1', 'tmp_for_test_0'], 
            should_olds=['tmp_for_test_2', 'tmp_for_test_4'])

        assert should_run_olds_news(
            should_news=['tmp_for_test_1', 'tmp_for_test_3'], 
            should_olds=['tmp_for_test_2'])

        assert not should_run_olds_news(
            should_news=['tmp_for_test_4', 'tmp_for_test_3'], 
            should_olds=['tmp_for_test_2'])