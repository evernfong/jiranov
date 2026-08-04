#!/usr/bin/env python3
"""
Auto-generate unit test stubs for each discovered Python function.
- Scans all .py files outside typical exclude dirs
- Creates/updates tests under tests/ with unittest-based, skipped stubs

Usage:
  python3 tools/generate_tests.py
"""
import ast
import pathlib
from typing import Iterable, List, Set

EXCLUDE_DIRS: Set[str] = {"tests", ".venv", "venv", "env", "__pycache__", "node_modules", ".git"}


def iter_py_files(root: str = ".") -> Iterable[pathlib.Path]:
    root_path = pathlib.Path(root)
    for p in root_path.rglob("*.py"):
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        yield p


def extract_functions(py_path: pathlib.Path) -> List[str]:
    try:
        src = py_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return []
    try:
        tree = ast.parse(src, filename=str(py_path))
    except SyntaxError:
        return []

    funcs: List[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            funcs.append(node.name)
    return funcs


def ensure_test_file(module_path: pathlib.Path, functions: List[str]) -> None:
    tests_dir = pathlib.Path("tests")
    tests_dir.mkdir(exist_ok=True)

    mod_name = module_path.stem
    test_file = tests_dir / f"test_{mod_name}.py"

    existing: Set[str] = set()
    content = ""
    if test_file.exists():
        content = test_file.read_text(encoding="utf-8", errors="ignore")
        try:
            ttree = ast.parse(content, filename=str(test_file))
            for tnode in ast.walk(ttree):
                if isinstance(tnode, ast.FunctionDef) and tnode.name.startswith("test_"):
                    existing.add(tnode.name)
        except SyntaxError:
            # If the existing test file is malformed, ignore and regenerate stubs
            pass

    lines: List[str] = []
    if not content:
        lines.append("import unittest")
        lines.append("import importlib.util, pathlib")
        lines.append(f"spec = importlib.util.spec_from_file_location('{mod_name}', pathlib.Path(r'{module_path}'))")
        lines.append("mod = importlib.util.module_from_spec(spec)")
        lines.append("assert spec and spec.loader is not None")
        lines.append("spec.loader.exec_module(mod)")
        lines.append("")

    for func in functions:
        tname = f"test_{func}_auto"
        if tname in existing:
            continue
        lines.append("")
        lines.append(f"class Test_{mod_name}_{func}(unittest.TestCase):")
        lines.append(f"    def {tname}(self):")
        lines.append(f"        # TODO: implement unit test for {mod_name}.{func}")
        lines.append(f"        self.skipTest('Auto-generated stub for {mod_name}.{func}')")

    if lines:
        with open(test_file, "a" if content else "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")


def main() -> None:
    any_sources = False
    generated = 0
    for p in iter_py_files("."):
        any_sources = True
        funcs = extract_functions(p)
        if funcs:
            ensure_test_file(p, funcs)
            generated += len(funcs)
    if not any_sources:
        print("No Python source files found to generate tests.")
    else:
        print(f"Generated/updated test stubs for {generated} function(s). See tests/ directory.")


if __name__ == "__main__":
    main()
