from dotenv import load_dotenv
import streamlit as st
import os

from htmlTemplates import css, bot_template, user_template
from instagram.main import run

import sys
from instagram.crew import InstagramCrew
import datetime

def main():
    load_dotenv()
    st.set_page_config(page_title="Social Media Marketing Chatbot", page_icon=":iphone:")
    st.write(css, unsafe_allow_html=True)

    st.header("Chat with the Digital Marketing Team :iphone:")
    
    with st.sidebar:
        st.header('Enter Research Details')
        
        page = st.text_input("Enter the instagram page description here: "),
        topic= st.text_area("What topic would you like to research?: ")

    if st.button('Run Research'):
        if not page or not topic:
            st.error("Please fill all the fields.")
        else:
            #inputs = f"instagram_description: {page}\n topic_of_the_week: {topic}"
            #research_crew = 
            
            inputs = {
                'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
                'instagram_description': page,
                'topic_of_the_week': topic,
            }
            result = InstagramCrew().crew().kickoff(inputs=inputs)
            st.subheader("Final Content Strategy: ")
            st.write(result)

if __name__ == '__main__':
    main()