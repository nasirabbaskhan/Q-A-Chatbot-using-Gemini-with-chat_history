import streamlit as st
import google.generativeai as genai # type: ignore

from dotenv import load_dotenv
import os
load_dotenv()

# configure GOOGLE_API_KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_response_gemini(question):
    response = chat.send_message(question)
    return response
    
# initilizing our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")


# initilize session state for chat history if it does not exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] =[]
    
user_input = st.text_input("input", key="input")
submit = st.button("Ask the question")
        
        
if submit and user_input:
    response = get_response_gemini(user_input)
    # add user query and response to the sesson chat history 
    st.session_state['chat_history'].append(("You", user_input))
    st.subheader("The Response is:")
    # print stream respons
    
    st.write(response.text)
    st.session_state['chat_history'].append(("Bot", response.text))
        

st.header("The Chat history is:")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")