import streamlit as st

st.set_page_config(
	layout = "wide",
	initial_sidebar_state = "auto"
)

st.title('Price and Season-Sale Prediction Solutions')

st.header('What is it?')
st.write('''
In order to improve and develop myself within the field of data science, the creation of this solution works both as a topic of study and as a portfolio project.
\n To create the solution, I created a scenario where it would be necessary to deliver the MVP of a data science project, with the objective of predicting the liquidity of the property price as well as the best period of the year for this property to be sold. In this scenario, the solution would be used by people from the business area (data citizens), so one of the goals would be to build a self-service solution, with a simple and intuitive interface.
\n As a data science solution that can be used by the business area, the model was built using statistical and AI methods in conjunction with business rules, seeking a balance between intelligence and experience.
''')

st.header('How to use?')
st.write('''
For self service use, the solution was built in _web app_ format, where you can see the presence of three distinct options, presented in the sidebar. Each of the options leads to a page, which are:
* **HOME**: solution's home page (YOU ARE HERE!), where the solution's operation is briefly reported and a brief explanation of how to use it;
* **PRICE PREDICTION SOLUTION**: page with the price prediction solution. In the main body of the page it will be possible to find the requested information fields, which must be filled in based on the characteristics of the property to be evaluated. After filling in the information, it is only necessary to click on the "PRICE EVALUATION" button so that the solution returns the expected value for the property; 
* **SEASON-SALE SOLUTION**: page with the season-sale solution. In the main body of the page it will be possible to find the requested information fields, which must be filled in based on the characteristics of the property to be evaluated. After filling in the information, it is only necessary to click on the "SEASON-SALE EVALUATION" button so that the solution returns the expected value for the property;
''')

st.header('Important informations!')
st.write('''
* It is important to mention that we are dealing with a statistical model, where there are always associated errors. The objective proposed here would be the delivery of an MVP that can be used by the business area, which can be improved in subsequent development cycles;
''')