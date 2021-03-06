#!/usr/bin/python

import unittest
import subprocess

class ClusterTest(unittest.TestCase):

    def testSanityCheck(self):
        self.assertTrue(True)

    def test_create_model(self):
        # Define command and arguments
        command = 'Rscript'
        path2script = '../../../PeakSegDisk-master/R/PeakSegFPOP_dir.R'

        # the function we want to run has 2 arguments
        # a path to the coverage data we are observing
        # and a penalty > 0
        args = ['../PeakLearner-1.1/jbrowse/tests/data/all_labels.bigBed', '1']

        # Build subprocess command
        cmd = [command, path2script] + args

        # check_output will run the command and store to result
        newModel = subprocess.check_output(cmd, universal_newlines=True)

        self.assertIsNotNone(newModel)


if __name__ == "__main__":
    unittest.main()
