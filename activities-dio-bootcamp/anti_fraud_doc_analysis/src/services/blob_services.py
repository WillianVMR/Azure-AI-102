import os
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient
import streamlit as st
from utils.Config import Config

def upload_file(file, fileName):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.AZURE_STORAGE_CONTAINER_NAME, blob=fileName)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as e:
        st.error(f"Error uploading file to Azure Storage: {e}")
        return None