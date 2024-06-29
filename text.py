import streamlit as st
from streamlit_option_menu import option_menu
from image import load_model
from image import load_model_1
import os
from PIL import Image
working_directory= os.path.dirname(os.path.abspath(__file__))
st.set_page_config(
    page_title= "Text Generation app",
    page_icon = ':moon:',
    layout = 'centered'
)
st.header("Neku Kavalasindhi Adagochu")
with st.sidebar:
    selected = option_menu(menu_title='Text Generation App',options=["Text to Text","Image to Text"])


def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return 'assistant'
    else:
        return 'model'
if selected == 'Text to Text':
    model = load_model()
    if 'chat_session' not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])
    st.title("Adigi Telusuko")
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)
    input_prompt = st.chat_input("Ask Quiery....")
    if input_prompt:
        st.chat_message('user').markdown(input_prompt)

        response= st.session_state.chat_session.send_message(input_prompt)
        with st.chat_message('assistant'):
            st.markdown(response.text)
if selected == 'Image to Text':
    st.title('Photo Nunchi adugu')
    upload_image = st.file_uploader(label = 'photo upload chey',type=['png','jpg','jpeg'])
    prompt = st.text_area(label='em kavalo adugu', height=30)
    if st.button('generate chey'):
        image = Image.open(upload_image)

        col1,col2 = st.columns(2)
        with col1:
            resized_image = image.resize({400,300})
            st.image(resized_image)
        with col2:
            caption = load_model_1(prompt,image)
            st.success(caption)









