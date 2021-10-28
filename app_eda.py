import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout='centered',
                   initial_sidebar_state='expanded',
                   page_title='Exploratory Data Analysis',
                   page_icon='📈')

#hide_menu_style = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)


st.image('https://image.freepik.com/vetores-gratis/dados-informam-o-conceito-de-ilustracao_114360-864.jpg')

col1, col2 = st.columns([1, 6])

# Web App Title
with col1:
    st.markdown('''<br>''', unsafe_allow_html=True)
    st.image('https://ciandt.com/themes/custom/ciandt_theme/logo.svg')

with col2:
    st.markdown('''
    # ** | Explory your Data**
    ''')


# Upload CSV data
with st.sidebar:
    st.image('https://ciandt.com/themes/custom/ciandt_theme/logo.svg')
    st.header('Explory your data')

    uploaded_file = st.sidebar.file_uploader("Upload your CSV file here", type=["csv"])

    st.header('How it works?')
    st.markdown('''
    This app allows for an analytical exploration of your dataframe, 
    showing the main features and statistical information, using a **Pandas Profiling**.
    
    If you want to know more about **Pandas Profiling**, [click here](https://github.com/pandas-profiling/pandas-profiling).''')


# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True, dark_mode=True)
    st.header('**Input DataFrame**')
    st.expander('Show RAW Data').write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)

else:
    st.info('Awaiting for CSV file to be uploaded.')



