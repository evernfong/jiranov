import unittest
import pathlib

class TestRepositoryState(unittest.TestCase):
    def test_no_source_files_present_or_generate(self):
        """
        Placeholder to keep a minimal test suite in repositories without source files.
        If source files are added later, run: python3 tools/generate_tests.py
        This will create per-function skipped test stubs under tests/.
        """
        code_exts = {'.py', '.js', '.ts', '.java', '.go', '.rb', '.php', '.rs', '.kt', '.c', '.cpp', '.cs'}
        has_code = False
        for p in pathlib.Path('.').rglob('*'):
            if p.is_file() and p.suffix in code_exts and 'tests' not in p.parts and '.git' not in p.parts:
                has_code = True
                break
        if has_code:
            self.skipTest('Source files detected; run tools/generate_tests.py to scaffold tests for functions.')
        else:
            self.assertTrue(True)
