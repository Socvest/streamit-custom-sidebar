import streamlit_float
import streamlit as st
from __init__ import CustomSidebarDefault
from streamlit_extras.switch_page_button import switch_page
from custom_sidebar_icons import Set_Nav_Emojis as set_Nav

st.set_page_config(layout="wide")

# icons_sidebar = set_Nav(None)
# icons_sidebar.Load_All_CDNs()


streamlit_float.float_init()

data_ = [
            {"index":0, "label":"Example", "page":"example", "href":"http://localhost:8501/"},
            {"index":1, "label":"Page", "page":"page", "icon":"ri-logout-box-r-line", "href":"http://localhost:8501/page"}
        ]

if "currentPage" not in st.session_state:
    st.session_state["currentPage"] = data_[0] 
else:
    st.session_state["currentPage"] = data_[0] 

if "sideNavSelection" not in st.session_state:
    st.session_state['sideNavSelection'] = None


with st.container():
    defaultSidebar = CustomSidebarDefault(closeNavOnLoad=True, backgroundColor="brown", loadPageName="example", data=data_, LocalOrSessionStorage=1, serverRendering=False, webMedium="local") #, data=data_, currentChoice=0, defaultV=0, key="page_selected_")
    defaultSidebar.load_custom_sidebar()
    st.session_state['sideNavSelection'] = defaultSidebar.change_page()
    
    streamlit_float.float_parent(css="top:-1000px;")

st.subheader("First Page")

st.write(["one", "two"][1])
