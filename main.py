import streamlit as st
import os
from utitlity import (load_model)

working_directory = os.path.dirname(os.path.abspath(__file__))

print(working_directory)

# setting up the page configuration
st.set_page_config(
    page_title = "Gemni Ai",
    page_icon = "🤖",
    layout = "centered"
)
    
    
def translate_role_for_streamlit(user_role):
    
    if user_role == 'model':
        return 'assistant'
    
    else:
        return user_role
    
model = load_model()
st.header('🤖 Chat Bot', divider='rainbow')

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