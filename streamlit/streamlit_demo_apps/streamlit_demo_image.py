import streamlit as st
from PIL import Image
import os
import uuid
import base64

def save_file(uploaded_file):
    file_extension = os.path.splitext(uploaded_file.name)[-1].lower()
    unique_filename = str(uuid.uuid4()) + file_extension
    uploaded_image = Image.open(uploaded_file)
    uploaded_image.save(unique_filename)
    return unique_filename

def set_bg_hack(main_bg):
    file_extension = os.path.splitext(main_bg)[-1].lower().replace(".", "")
    with open(main_bg, "rb") as f:
        image_data = f.read()
    base64_image = base64.b64encode(image_data).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{file_extension};base64,{base64_image});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    st.set_page_config(page_title="Ex-stream-ly Cool App", 
                   page_icon="🧊", 
                   layout="wide", 
                   initial_sidebar_state="auto", 
                   menu_items=None)
    set_bg_hack("sample.jpeg")
    st.header('Image Upload and Save App', divider='rainbow')
    st.divider()
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if 'save_img' not in st.session_state:
        st.session_state.save_img = False
        
    if (st.button("Save Image") or (st.session_state.save_img)):
        st.session_state.save_img = True
        if uploaded_file is not None:
            local_filename = save_file(uploaded_file)
            st.success(f"Image saved locally as {local_filename}",icon="✅")
            if st.button('View Image'):
                st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        else:
            st.error('Image missing error',icon="🚨")
            st.warning('Image missing warning', icon="⚠️")
            
if __name__ == "__main__":
    main()
