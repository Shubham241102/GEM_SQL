import streamlit as st
import google.generativeai as genai
import os

model=genai.configure(api_key=os.getenv("GOOGLE_API"))
model=genai.GenerativeModel('gemini-pro')

st.title(" SQL QUERY GENERATOR  🧑‍🚀:")
st.subheader("let's generate a SQL Query 🧾!!!!")


  
with st.sidebar:
    st.header("SQL Generator ")
    st.write('With an intuitive user interface and a user-friendly design, this  application invites users to embark on a creative odyssey. By simply providing few inputs from  user  the application harnesses the transformative power of Gemini Pro to generate a quality  SQL QUERY with Explaination .')

text_input=st.text_input("PLease enter your Query in Plain English: ")
submit=st.button("Generate Query")

if submit:

    with st.spinner("Please Wait....."):
        template="""
            Create a SQL Query using below text:

            '''
                {text_input}

            '''

            The SQL Query .

        """
        formatted_template=template.format(text_input=text_input)

        st.write(formatted_template)
        response=model.generate_content(formatted_template)
        
        sql_query=response.text
        st.write(sql_query)

        explanation="""
            Explain This SQL Query:

            '''
                {sql_query}

            '''

            Provide the simplest explanation for the query.

        """
        explanation_formatted=explanation.format(sql_query=sql_query)
        explanation=model.generate_content(explanation_formatted)
        explanation=explanation.text
        st.write(explanation)


        with st.container():
            st.success("SQL Query Generated Sucessfully !!")
            st.code(sql_query , language="sql")  #for formatiing as SQL Language

            st.success("Explanation for the SQL Query Will be :")
            st.markdown(explanation)
            
            st.snow()
            st.balloons()


