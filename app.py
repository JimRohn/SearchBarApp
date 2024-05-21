from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import sqlite3
import openai  # Importing the OpenAI module

# Configure our API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to load OpenAI Model and provide SQL query as response to NLP query
def get_openai_response(question, prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt[0]},
                {"role": "user", "content": question}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

# Function to retrieve records from the student table
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except sqlite3.Error as e:
        st.error(f"Database error: {e}")
        return []

# Define your prompt
prompt = ["You are an expert in converting English questions to SQL query. The SQL database has the name STUDENT and has the following columns: NAME, CLASS, SECTION, MARKS. \n\nFor example, \nExample 1 - How many entries of records are present?, the SQL command will be something like this: SELECT COUNT(*) FROM STUDENT \nExample 2 - What is the name of the student who has scored the highest marks?, the SQL command will be something like this: SELECT NAME FROM STUDENT WHERE MARKS = (SELECT MAX(MARKS) FROM STUDENT); \nExample 3 - Tell me all the students studying in Data Science class. The SQL command will be something like this: SELECT NAME FROM STUDENT WHERE CLASS = 'Data Science'; \n\nNow, you can ask me any question related to the STUDENT table and I will convert it into SQL query for you."]

# Streamlit App
st.set_page_config(page_title="I can retrieve any SQL query", page_icon=":bar_chart:", layout="wide")
st.header("OpenAI App to Retrieve SQL Query")

question = st.text_input("Input:", key="input")

submit = st.button("Ask the question")

# If the submit button is clicked
if submit:
    response = get_openai_response(question, prompt)
    if response:
        st.write(f"Generated SQL Query: {response}")
        data = read_sql_query(response, 'student.db')
        st.subheader("The response is:")
        for row in data:
            st.write(row)
