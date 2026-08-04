import unittest
import importlib.util, pathlib
spec = importlib.util.spec_from_file_location('generate_tests', pathlib.Path(r'tools/generate_tests.py'))
mod = importlib.util.module_from_spec(spec)
assert spec and spec.loader is not None
spec.loader.exec_module(mod)


class Test_generate_tests_iter_py_files(unittest.TestCase):
    def test_iter_py_files_auto(self):
        # TODO: implement unit test for generate_tests.iter_py_files
        self.skipTest('Auto-generated stub for generate_tests.iter_py_files')

class Test_generate_tests_extract_functions(unittest.TestCase):
    def test_extract_functions_auto(self):
        # TODO: implement unit test for generate_tests.extract_functions
        self.skipTest('Auto-generated stub for generate_tests.extract_functions')

class Test_generate_tests_ensure_test_file(unittest.TestCase):
    def test_ensure_test_file_auto(self):
        # TODO: implement unit test for generate_tests.ensure_test_file
        self.skipTest('Auto-generated stub for generate_tests.ensure_test_file')

class Test_generate_tests_main(unittest.TestCase):
    def test_main_auto(self):
        # TODO: implement unit test for generate_tests.main
        self.skipTest('Auto-generated stub for generate_tests.main')
