# streamlit-custom-sidebar

Streamlit component that allows you to do buid a more flexible customizable sidebar that does not look buggy when rendered. Usually when we try to adjust the native streamlit sidebar it gets rendered after all the streamlit default settings are rendered. With this, your default settings are rendered when the page loads but it still uses streamlit's sidebar mative settings - css like its open and close animation and buttons.  

Uses other custom components I created:
[local storage](https://pypi.org/project/streamlit-local-storage/)
[session storage](https://pypi.org/project/streamlit-browser-session-storage/)

## Installation instructions

```sh
pip install streamlit-custom-sidebar
```

## Usage instructions

```python
import streamlit as st
from streamlit_custom_sidebar import CustomSidebarDefault
import streamlit_float # recommended


streamlit_float.float_init(include_unstable_primary=False)

data_ = [
            {"index":0, "label":"Example", "page":"example", "href":"http://localhost:8501/"},
            {"index":1, "label":"Page", "page":"page", "icon":"ri-logout-box-r-line", "href":"http://localhost:8501/page"}
        ]

if "currentPage" not in st.session_state: # required as component will be looking for this in session state to change page via `switch_page`
    st.session_state["currentPage"] = data_[0] 
else:
    st.session_state["currentPage"] = data_[0] 


with st.container():
    defaultSidebar = CustomSidebarDefault(closeNavOnLoad=False, backgroundColor="brown", loadPageName="example", data=data_, LocalOrSessionStorage=1, serverRendering=False, webMedium="local") 
    defaultSidebar.load_custom_sidebar()
    defaultSidebar.change_page()
    
    streamlit_float.float_parent(css="display:fixed; top:-1000px;") # gets rid of the whitespace created from the iframes used to build the component - no big forehead.

# The above must be rendered atop every streamlit page

```
