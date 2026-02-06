import pathlib
import re


def test_trend_schema_exists_in_spec():
    """Failing test: ensure a trend schema is defined in specs/technical.md.

    The technical spec MUST define a trend-related schema (e.g., TrendResult).
    If the schema is missing, this test fails to indicate the specification gap.
    """
    spec_path = pathlib.Path("specs/technical.md")
    assert spec_path.exists(), "specs/technical.md is missing"
    content = spec_path.read_text(encoding="utf-8")

    # Look for explicit Trend schema or trend-related field names
    has_trend_schema = bool(re.search(r"\bTrend\b|TrendResult|trend result", content, re.IGNORECASE))
    assert has_trend_schema, (
        "Specification ambiguity: no 'Trend' schema found in specs/technical.md. "
        "Test expects a trend-related schema (topic/source/timestamp)."
    )


def test_trend_schema_contains_expected_fields():
    """Failing test: assert trend schema includes required fields.

    The expected fields (topic, source, timestamp) are derived from the API contract
    expectations. If the spec does not list these fields, this test fails.
    """
    spec_path = pathlib.Path("specs/technical.md")
    content = spec_path.read_text(encoding="utf-8")

    # Search for the required field names anywhere in the spec as a proxy for schema
    required_fields = ["topic", "source", "timestamp"]
    missing = [f for f in required_fields if f not in content]
    assert not missing, (
        f"Specification missing expected trend field(s): {missing}. "
        "The technical spec must define these fields for the trend data contract."
    )
