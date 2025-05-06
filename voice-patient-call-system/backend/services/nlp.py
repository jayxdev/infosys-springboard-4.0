from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from backend.config import TEXT_ANALYTICS_KEY, TEXT_ANALYTICS_ENDPOINT

def categorize_request(text):
    """
    Categorizes a request based on sentiment analysis.
    
    Args:
        text (str): The input text to analyze.
    
    Returns:
        str: Categorization result - "Emergency", "Routine", or "Urgent".
    """
    try:
        # Initialize Azure Text Analytics Client
        client = TextAnalyticsClient(endpoint=TEXT_ANALYTICS_ENDPOINT, credential=AzureKeyCredential(TEXT_ANALYTICS_KEY))
        
        # Ensure text is not empty
        if not text or not text.strip():
            return "Uncategorized"  # Handle empty text input

        # Perform sentiment analysis (correct document structure)
        response = client.analyze_sentiment(documents=[{"id": "1", "text": text}])
        
        # Check if the response contains a valid result
        if response and response[0] and hasattr(response[0], "sentiment"):
            result = response[0]

            # Categorization based on sentiment
            if result.sentiment == "negative":
                return "Emergency"
            elif result.sentiment == "neutral":
                return "Routine"
            elif result.sentiment == "positive":
                return "Urgent"
            else:
                return "Uncategorized"  # Edge case fallback
        else:
            return "UncategorizedUnexpectedResponse"  # Handle unexpected response format

    except Exception as e:
        print(f"Error in categorize_request: {e}")
        return "Error"
