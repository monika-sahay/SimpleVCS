import unittest
import os
import shutil
import tempfile
from simplevcs.simple_vcs import SimpleVCS


class TestSimpleVCSInitialization(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for the tests
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.test_dir)

    def test_repository_initialization(self):
        # Initialize the SimpleVCS with the test directory
        vcs = SimpleVCS(self.test_dir)
        vcs.init()

        # Check if the main repository directory exists
        self.assertTrue(os.path.isdir(self.test_dir))

        # Check if the objects directory exists within the repository
        objects_path = os.path.join(self.test_dir, 'objects')
        self.assertTrue(os.path.isdir(objects_path))


if __name__ == '__main__':
    unittest.main()
