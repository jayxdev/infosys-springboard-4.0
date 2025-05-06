import pytest
from unittest.mock import patch, MagicMock
from backend.services.nlp import categorize_request

@pytest.fixture
def mock_text_analytics_client():
    with patch('backend.services.nlp.TextAnalyticsClient') as MockTextAnalyticsClient:
        yield MockTextAnalyticsClient

def test_categorize_request_emergency(mock_text_analytics_client):
    mock_client = mock_text_analytics_client.return_value
    mock_client.analyze_sentiment.return_value = [
        MagicMock(sentiment="negative")
    ]
    result = categorize_request("This is a terrible situation.")
    assert result == "Emergency"

def test_categorize_request_routine(mock_text_analytics_client):
    mock_client = mock_text_analytics_client.return_value
    mock_client.analyze_sentiment.return_value = [
        MagicMock(sentiment="neutral")
    ]
    result = categorize_request("This is a regular check-up.")
    assert result == "Routine"

def test_categorize_request_urgent(mock_text_analytics_client):
    mock_client = mock_text_analytics_client.return_value
    mock_client.analyze_sentiment.return_value = [
        MagicMock(sentiment="positive")
    ]
    result = categorize_request("I am feeling much better now.")
    assert result == "Urgent"

def test_categorize_request_empty_text():
    result = categorize_request("")
    assert result == "Uncategorized"

def test_categorize_request_unexpected_response(mock_text_analytics_client):
    mock_client = mock_text_analytics_client.return_value
    mock_client.analyze_sentiment.return_value = [
        MagicMock(sentiment=None)
    ]
    result = categorize_request(None)
    assert result == "UncategorizedUnexpectedResponse"

def test_categorize_request_exception(mock_text_analytics_client):
    mock_client = mock_text_analytics_client.return_value
    mock_client.analyze_sentiment.side_effect = Exception("Test exception")
    result = categorize_request("This will cause an exception.")
    assert result == "Error"
