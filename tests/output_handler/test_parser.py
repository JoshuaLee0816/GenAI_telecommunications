import pytest
from output_handler.parser import JSONOutputParser

@pytest.fixture
def parser():
    return JSONOutputParser()

def test_parse_valid_json(parser):
    raw_output = """
    {
        "category": "network_issue",
        "priority": "high",
        "recommended_action": "Restart the router"
    }
    """

    result = parser.parse(raw_output)

    assert isinstance(result, dict)
    assert result["category"] == "network_issue"
    assert result["priority"] == "high"
    assert result["recommended_action"] == "Restart the router"
    assert "error" not in result

def test_parse_invalid_json(parser):
    raw_output = """
    { category: network_issue, priority: high}
    """

    result = parser.parse(raw_output)

    assert result["category"] is None
    assert result["priority"] is None
    assert result["recommended_action"] is None
    assert "error" in result
    assert "Invalid JSON" in result["error"]

def test_parse_json_not_object(parser):
    raw_output = """
    [
        {"category": "network_issue"}
    ]
    """ #JSON is list not dict here

    result = parser.parse(raw_output)

    assert result["category"] is None
    assert result["priority"] is None
    assert result["recommended_action"] is None
    assert "error" in result
    assert "Output is not a JSON object" in result["error"] 