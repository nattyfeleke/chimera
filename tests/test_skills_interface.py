import pathlib
import re


def test_skill_readmes_and_impl_presence():
    """Failing test: assert each skill has README and an implementation entrypoint.

    Tests the repository for skill directories and fails if an implementation
    callable (python module with a run/execute function) is not present. This
    enforces the contract that skill interfaces be declared before implementation.
    """
    skills_dir = pathlib.Path("skills")
    assert skills_dir.exists() and skills_dir.is_dir(), "skills/ directory is missing"

    skill_dirs = [p for p in skills_dir.iterdir() if p.is_dir()]
    assert skill_dirs, "No skill directories found under skills/"

    for sd in skill_dirs:
        readme = sd / "README.md"
        assert readme.exists(), f"Missing README.md for skill: {sd.name}"

        content = readme.read_text(encoding="utf-8")
        # Assert README documents Input Contract and Output Contract headings
        assert re.search(r"Input Contract", content, re.IGNORECASE), (
            f"README.md for skill '{sd.name}' missing 'Input Contract' section"
        )
        assert re.search(r"Output Contract", content, re.IGNORECASE), (
            f"README.md for skill '{sd.name}' missing 'Output Contract' section"
        )

        # Implementation presence check: look for any .py file that could expose an entrypoint
        py_files = list(sd.glob("*.py"))
        # Enforce failure because implementations are not expected yet
        assert py_files, (
            f"No implementation Python module found for skill '{sd.name}'. "
            "Expected at least one .py file exposing a callable entrypoint (run/execute)."
        )


def test_skill_entrypoint_signature_declared_in_readme():
    """Failing test: assert README declares expected input parameter names.

    This test examines the README 'Input Contract' section for a brief JSON-like
    schema and fails if the section is missing or ambiguous.
    """
    skills_dir = pathlib.Path("skills")
    skill_dirs = [p for p in skills_dir.iterdir() if p.is_dir()]

    for sd in skill_dirs:
        readme = sd / "README.md"
        content = readme.read_text(encoding="utf-8")

        # Try to extract a JSON-style block under 'Input Contract'
        m = re.search(r"Input Contract\s*(\{[\s\S]*?\})", content, re.IGNORECASE)
        assert m, (
            f"Ambiguous Input Contract in README for '{sd.name}': expected JSON-like block."
        )

        # Do not parse the JSON; instead assert presence of at least one key token
        block = m.group(1)
        assert re.search(r"\"type\"|\"properties\"|\"required\"", block), (
            f"Input Contract for '{sd.name}' appears incomplete or not schema-like."
        )
