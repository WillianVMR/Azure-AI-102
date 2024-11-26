import streamlit as st
from services.blob_services import upload_file
from services.credit_card_service import analyze_credit_card
def configure_interface():
    st.set_page_config(page_title="Anti Fraud Document Analysis", page_icon=":guardsman:", layout="wide")
    st.title("Anti Fraud Document Analysis")
    upload_file = st.file_uploader("Upload a document", type=["png", "jpg", "jpeg"])
    
    if upload_file is not None:
        fileName = upload_file.name
        
        # Send file to Azure Storage
        blob_url = upload_file(upload_file, fileName)
        if blob_url:
            st.write(f"File uploaded successfully: {fileName}")
            st.success("File uploaded successfully")
            st.image(blob_url)
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_info(blob_url, credit_card_info)
        else:
            st.write(f"File not uploaded: {fileName}")
            st.error("Failed to upload file to Azure Storage")
    
    

def show_image_and_info(blob_url, credit_card_info):
    st.image(blob_url, caption="Image sent", use_column_width=True)
    st.write("Validation result:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color:green;'>Valid credit card</h1>", unsafe_allow_html=True)
        st.write(f"Owner: {credit_card_info['card_name']}")
        st.write(f"Bank: {credit_card_info['bank']}")
        st.write(f"Card number: {credit_card_info['card_number']}")
        st.write(f"Expiration date: {credit_card_info['expiration_date']}")
    else:
        st.markdown(f"<h1 style='color:red;'>Invalid credit card</h1>", unsafe_allow_html=True)

if __name__ == "__main__":
    configure_interface()