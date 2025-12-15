import streamlit as st
from groq import Groq

st.subheader("Chatbox")
client = Groq(api_key = "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")
if "history" not in st.session_state:
    st.session_state.history = []

text = st.text_input("Enter your message")
system_prompt =( "You can reply to the message that is given by the user")
if st.button("Send"):
    responses = client.chat.completions.create(model= "llama-3.3-70b-versatile",
                            temperature=1,
                            messages=[
                                {"role": "system", "content":f"{system_prompt}"},
                                {"role":"user","content":f"{text}"}])
    chatbox = responses.choices[0].message.content
    st.session_state.history.append({"user":text,"bot":chatbox})
    
            
    for i in st.session_state.history:
        st.write(f" *You:* {i['user']}")
        st.write(f" *Bot:* {i['bot']}")
        
if st.button("Chat history"):
            st.write(st.session_state.history) 
    
