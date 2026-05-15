import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Create pages as a flat list for dropdown behavior
pages = {
    "Navigation": [
        st.Page("./src/officegraph/pages/Home.py", title="Home", default=True),
        st.Page("./src/officegraph/pages/ChainOfCommand.py", title="Chain of Command")]
    }
    
pg = st.navigation(pages, position="top")
pg.run()