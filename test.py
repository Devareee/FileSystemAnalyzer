import os
import unittest
import platform
import file_system_analyzer as fsa


def test_fsa():
    # get the current path
    current_path = os.getcwd()
    test_dir = 'test'
    new_path = os.path.join(current_path, test_dir)
    # create test directory in current directory
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    # create text file
    with open(os.path.join(new_path, 'text.txt'), 'wb') as f:
        num_chars = 1024 * 1024  # 1 MB
        f.write(b'0' * num_chars)
    # create executable file
    with open(os.path.join(new_path, 'executable.py'), 'wb') as f:
        num_chars = 1024 * 1024 * 2  # 2 MB
        f.write(b'0' * num_chars)
    # create image file
    with open(os.path.join(new_path, 'image.jpg'), 'wb') as f:
        num_chars = 1024 * 512  # 0.5 MB
        f.write(b'0' * num_chars)
    # create sound file
    with open(os.path.join(new_path, 'sound.wav'), 'wb') as f:
        num_chars = 1024 * 1024 * 10  # 10 MB
        f.write(b'0' * num_chars)


class MyTestCase(unittest.TestCase):

    test_fsa()

    # test file type categorization
    def test_ftc(self):
        new_path = os.path.join(os.getcwd(), 'test')
        files = [1, 1, 1, 0, 1, 0, 0]
        result = fsa.file_type_categorization(new_path)
        self.assertEqual(result, files)

    # test size analysis
    def test_sa(self):
        new_path = os.path.join(os.getcwd(), 'test')
        files = [2.0, 0.5, 1.0, 0.0, 10.0, 0.0, 0.0]
        result = fsa.file_type_categorization(new_path, calculate_size=True)
        self.assertEqual(result, files)

    # test large files identification
    def test_lfi(self):
        new_path = os.path.join(os.getcwd(), 'test')
        size = 1
        large = {os.path.join(new_path, 'executable.py'): 2.0,
                 os.path.join(new_path, 'sound.wav'): 10.0}
        result = fsa.large_files_identification(new_path, size)
        self.assertEqual(result, large)

    # test file permissions report
    def test_fpr(self):
        new_path = os.path.join(os.getcwd(), 'test')
        # a crutch for Windows :)
        if platform.system() == 'Windows':
            unusual = {os.path.join(new_path, 'text.txt'): '666',
                       os.path.join(new_path, 'executable.py'): '666',
                       os.path.join(new_path, 'image.jpg'): '666',
                       os.path.join(new_path, 'sound.wav'): '666'}
        else:
            unusual = {}
        result = fsa.file_permissions_report(new_path)
        self.assertEqual(result, unusual)


if __name__ == '__main__':
    unittest.main()
