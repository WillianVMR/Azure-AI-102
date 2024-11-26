from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config
import streamlit as st

def analyze_credit_card(card_image_url):
    credential = AzureKeyCredential(Config.KEY)
    document_client = DocumentIntelligenceClient(
        endpoint=Config.ENDPOINT_URL, credential=credential
    )
    card_analysis = document_client.begin_analyze_document_from_url(
            model_id="prebuilt-document", document_url=card_image_url
    )
    result = card_analysis.result()

    for document in result.documents:
        fields = document.get('fields', {})
        return {
            "card_name": fields.get('CardName', {}).get('valueString'),
            "bank": fields.get('Bank', {}).get('valueString'),
            "card_number": fields.get('CardNumber', {}).get('valueString'),
            "expiration_date": fields.get('ExpirationDate', {}).get('valueString')
        }

    
    