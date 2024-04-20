import streamlit as st
import google.generativeai as genai


st.title("Conversational Ai Tutor")

f = open("keys\.gemini.txt")
API_KEY = f.read()
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                system_instruction='''you are a helping ai .
                                                what ever user enter the input you have politely answer and also
                                                provide some sorce which will help them''')

if "data" not in st.session_state:
    st.session_state['data'] = []

st.chat_message('AI').write("🙋‍♀️ Hii Folk 🙋‍♂️...Please Enter Your Query")

chat = model.start_chat(history=st.session_state['data'])

for mesg in chat.history:
    st.chat_message(mesg.role).write(mesg.parts[0].text)

user_input = st.chat_input()

if user_input:
    st.chat_message("user").write(user_input)
    response = chat.send_message(user_input)
    st.chat_message("AI").write(response.text)
    st.session_state['data'] = chat.history
