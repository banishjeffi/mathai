import streamlit as st
from PIL import Image
import os

import google.generativeai as genai

genai.configure(api_key = "AIzaSyC6zEe1IMBGSvq5QfOrci-1KLO2Ztkc1Bk")

def load_model():
    model = genai.GenerativeModel('gemini-pro')
    return model

def ocr(image):
    gemini_pro_vision_model = genai.GenerativeModel('gemini-pro-vision')
    prompt = "Extract the questions from the image, this image might contain mathematical symbols so convert it to searchable text if it is not related to maths please say that sorry i cant process this image please provide me a math related images"
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result

working_directory = os.path.dirname(os.path.abspath(__file__))

print(working_directory)

# setting up the page configuration
st.set_page_config(
    page_title = "Math Ai",
    page_icon = "🤖",
    layout = "centered"
)
    
st.header("🤖 Math AI", divider='rainbow')

tab1, tab2 = st.tabs(["📇 Scan Q/A", "🖺 Type Q/A"])
    
    
def translate_role_for_streamlit(user_role):
    
    if user_role == 'model':
        return 'assistant'
    
    else:
        return user_role
    

with tab1:
    
    st.subheader("📇 Scan Q/A")
    
    uploaded_image = st.file_uploader(" Upload an Image................", type = ["jpg","png","jpeg"])
    
    if st.button("Scan and Extract Image"):
        image = Image.open(uploaded_image)
        
        model = load_model()
        chat = model.start_chat(history = [])
        chat.send_message("Your name is Math AI, you are a part of Eduport developed by Banish Jeffi. You can solve math-related problems. - Handling Math Inquiries: - If the customer's query is math-related, provide a clear and concise answer to their questions. - If the inquiry is complex, break down the steps in a logical manner to aid understanding. - Include relevant formulas or explanations to support the solution. - Non-Math Requests: - If the customer's request is not related to math, respond with a friendly message: 'Sorry, as I am a mathematical branch of Eduport, I can only provide mathematical solutions. - Handling Inappropriate or Offensive Content: - If the customer provides inappropriate or offensive content, respond with a neutral message: 'I'm here to help you with math questions. If you have any math-related inquiries, feel free to ask! - Language and Tone: - Use language that is easy to understand, especially when explaining complex mathematical concepts.")
        
        
        st.image(image)
        
        question = ocr(image)
        st.info(question)

        if question in "sorry":
            st.danger(question)
        elif question in "image":
            st.danger("Sorrry I couldn't able to process image please try another image")
        else:
            st.text("Question")
            st.info(question)  
            ans = chat.send_message(question)
            st.text('Solution:')
            st.markdown(ans.text)
            
with tab2:
    
    st.subheader('🖺 Type Q/A')
    
    model = load_model()

    context = "Your name is Math AI, you are a part of Eduport developed by Banish Jeffi. You can solve math-related problems. - Handling Math Inquiries: - If the customer's query is math-related, provide a clear and concise answer to their questions. - If the inquiry is complex, break down the steps in a logical manner to aid understanding. - Include relevant formulas or explanations to support the solution. - Non-Math Requests: - If the customer's request is not related to math, respond with a friendly message: 'Sorry, as I am a mathematical branch of Eduport, I can only provide mathematical solutions. - Handling Inappropriate or Offensive Content: - If the customer provides inappropriate or offensive content, respond with a neutral message: 'I'm here to help you with math questions. If you have any math-related inquiries, feel free to ask! - Language and Tone: - Use language that is easy to understand, especially when explaining complex mathematical concepts."

    if "Chat_session" not in st.session_state:
        st.session_state.Chat_session = model.start_chat(history=[])
        st.session_state.Chat_session.send_message(context)
    
    for message in st.session_state.Chat_session.history:
        if message.parts[0].text != context:
            with st.chat_message(translate_role_for_streamlit(message.role)):   
                st.markdown(message.parts[0].text)
                
                
    user_prompt = st.chat_input("Ask Gemini Pro...................")
        
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        gemini_response = st.session_state.Chat_session.send_message(user_prompt)
            
        with st.chat_message('assistant'):
            st.markdown(gemini_response.text)
