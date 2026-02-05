import pytest

# Test-first: this test references `src.trends.detector.detect_trends`
# which should be implemented by the feature work. The test is expected
# to fail until the implementation is provided.

from src.trends.detector import detect_trends


def test_detects_simple_hashtag_trend():
    posts = [
        {"id": "p1", "text": "We love #newtopic and it's growing", "timestamp": "2026-02-01T00:00:00Z"},
        {"id": "p2", "text": "#newtopic is everywhere today", "timestamp": "2026-02-02T00:00:00Z"},
        {"id": "p3", "text": "unrelated content", "timestamp": "2026-02-02T01:00:00Z"},
    ]

    trends = detect_trends(posts, window_days=7)

    assert isinstance(trends, list)
    # Expect at least one detected trend containing 'newtopic' or '#newtopic'
    assert any(("newtopic" in (t.get("term") or "").lower()) for t in trends)
