import os
import streamlit as st
from streamlit_local_storage import LocalStorage
from streamlit_session_browser_storage import SessionStorage
from streamlit_extras.switch_page_button import switch_page


class SidebarIcons:

    def __init__(self, append_CDN_to=None) -> None:
        self.append_CDN_to = append_CDN_to
    
    def Load_All_CDNs(self):
        """
        Load all the CDNs for the supported icon libraries. These include:
        - Google-material-symbols
        - Remix icon
        - Tabler Icons
        - Icon-8
        - line-awesome
        """

        linkJS = """
            <script>
                exists = window.parent.document.querySelectorAll('link[href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0"]')
             
                if (exists.length === 0 ){{
                    const GoogleEmoji = document.createElement("link");
                    GoogleEmoji.href = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0";
                    GoogleEmoji.rel = "stylesheet";
                    window.top.document.head.appendChild(GoogleEmoji);

                    const remixIcon = document.createElement("link");
                    remixIcon.href = "https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css";
                    remixIcon.rel = "stylesheet";
                    window.top.document.head.appendChild(remixIcon);

                    const tablerIcons = document.createElement("link");
                    tablerIcons.href = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/iconfont/tabler-icons.min.css";
                    tablerIcons.rel = "stylesheet";
                    window.top.document.head.appendChild(tablerIcons); 

                    const tablerIcons_2 = document.createElement("link");
                    tablerIcons_2.href ="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css";      
                    tablerIcons_2.rel = "stylesheet";
                    window.top.document.head.appendChild(tablerIcons_2);   

                    const tablerIcons_3 = document.createElement("script")
                    tablerIcons_3.src = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons-react/dist/index.umd.min.js"
                    window.top.document.head.appendChild(tablerIcons_3) 

                    const icon8_line_awesome = document.createElement("link");
                    icon8_line_awesome.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/font-awesome-line-awesome/css/all.min.css";
                    icon8_line_awesome.rel = "stylesheet";
                    window.top.document.head.appendChild(icon8_line_awesome);

                    const icon8_line_awesome2 = document.createElement("link");
                    icon8_line_awesome2.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css";
                    icon8_line_awesome2.rel = "stylesheet";
                    window.top.document.head.appendChild(icon8_line_awesome2);

                    removeJs = parent.document.querySelectorAll('iframe[srcdoc*="GoogleEmoji"]')[0].parentNode
                    removeJs.style = 'display:none;'
                }} else {{
                    
                    removeJs = parent.document.querySelectorAll('iframe[srcdoc*="GoogleEmoji"]')[0].parentNode
                    removeJs.style = 'display:none;'
                }}

            </script>
        """
        st.components.v1.html(linkJS, height=0, width=0)

    def Load_All_CDNs_to_streamlit_cloud(self):
        query = "iframe[title='streamlitApp']"

        linkJS = f"""
            <script>
                headToAppendIframe = window.top.document.querySelectorAll("{query}")[0].contentDocument.head

                exists = window.parent.document.querySelectorAll('link[href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0"]')

                if (exists.length === 0){{
                    const GoogleEmoji = document.createElement("link");
                    GoogleEmoji.href = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0";
                    GoogleEmoji.rel = "stylesheet";
                    headToAppendIframe.appendChild(GoogleEmoji);

                    const remixIcon = document.createElement("link");
                    remixIcon.href = "https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css";
                    remixIcon.rel = "stylesheet";
                    headToAppendIframe.appendChild(remixIcon);

                    const tablerIcons = document.createElement("link");
                    tablerIcons.href = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/iconfont/tabler-icons.min.css";
                    tablerIcons.rel = "stylesheet";
                    headToAppendIframe.appendChild(tablerIcons); 

                    const tablerIcons_2 = document.createElement("link");
                    tablerIcons_2.href ="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css";      
                    tablerIcons_2.rel = "stylesheet";
                    headToAppendIframe.appendChild(tablerIcons_2);   

                    const tablerIcons_3 = document.createElement("script")
                    tablerIcons_3.src = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons-react/dist/index.umd.min.js"
                    headToAppendIframe.appendChild(tablerIcons_3) 

                    const icon8_line_awesome = document.createElement("link");
                    icon8_line_awesome.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/font-awesome-line-awesome/css/all.min.css";
                    icon8_line_awesome.rel = "stylesheet";
                    headToAppendIframe.appendChild(icon8_line_awesome);

                    const icon8_line_awesome2 = document.createElement("link");
                    icon8_line_awesome2.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css";
                    icon8_line_awesome2.rel = "stylesheet";
                    headToAppendIframe.appendChild(icon8_line_awesome2);

                    removeJs = parent.document.querySelectorAll('iframe[srcdoc*="GoogleEmoji"]')[0].parentNode
                    removeJs.style = 'display:none;'
                }} else {{
                    removeJs = parent.document.querySelectorAll('iframe[srcdoc*="GoogleEmoji"]')[0].parentNode
                    removeJs.style = 'display:none;'
                }}

            </script>
        """
        st.components.v1.html(linkJS, height=0, width=0)

    def custom_query_for_my_app_head_tag_CDN(self):

        linkJS = f"""
            <script>
                headToAppendIframe = {self.append_CDN_to}

                exists = window.parent.document.querySelectorAll('link[href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0"]')

                if (exists.length === 0){{
                    const GoogleEmoji = document.createElement("link");
                    GoogleEmoji.href = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0";
                    GoogleEmoji.rel = "stylesheet";
                    headToAppendIframe.appendChild(GoogleEmoji);

                    const remixIcon = document.createElement("link");
                    remixIcon.href = "https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css";
                    remixIcon.rel = "stylesheet";
                    headToAppendIframe.appendChild(remixIcon);

                    const tablerIcons = document.createElement("link");
                    tablerIcons.href = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/iconfont/tabler-icons.min.css";
                    tablerIcons.rel = "stylesheet";
                    headToAppendIframe.appendChild(tablerIcons); 

                    const tablerIcons_2 = document.createElement("link");
                    tablerIcons_2.href ="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css";      
                    tablerIcons_2.rel = "stylesheet";
                    headToAppendIframe.appendChild(tablerIcons_2);   

                    const tablerIcons_3 = document.createElement("script")
                    tablerIcons_3.src = "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons-react/dist/index.umd.min.js"
                    headToAppendIframe.appendChild(tablerIcons_3) 

                    const icon8_line_awesome = document.createElement("link");
                    icon8_line_awesome.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/font-awesome-line-awesome/css/all.min.css";
                    icon8_line_awesome.rel = "stylesheet";
                    headToAppendIframe.appendChild(icon8_line_awesome);

                    const icon8_line_awesome2 = document.createElement("link");
                    icon8_line_awesome2.href = "https://maxst.icons8.com/vue-static/landings/line-awesome/line-awesome/1.3.0/css/line-awesome.min.css";
                    icon8_line_awesome2.rel = "stylesheet";
                    headToAppendIframe.appendChild(icon8_line_awesome2);

                    removeJs = parent.document.querySelectorAll('iframe[srcdoc*="GoogleEmoji"]')[0].parentNode
                    removeJs.style = 'display:none;'
                }} else {{
                    removeJs = parent.document.querySelectorAll('iframe[srcdoc*="GoogleEmoji"]')[0].parentNode
                    removeJs.style = 'display:none;'
                }}

            </script>
        """
        st.components.v1.html(linkJS, height=0, width=0)
        

class CustomSidebarDefault:

    """
    Create your very own custom side bar navigation in streamlit with more ideal features. 

    Args:
        - (optional) backgroundColor: background color of the sidebar
        - (optional) activeBackgroundColor: background color of active/currently clicked page/tab
        - (optional) navigationHoverBackgroundColor: color of navigation tab when you hover over it
        - (optional) labelIconSize: font size of the text (label) and icon
        - (optional) distanceIconLabel: distance between the icon and the label in the navigation tab
        - (optional) closeNavOnLoad: whether or not the sidebar should be closed when the page is first rendered.
        - (optional) loadPageName: manually set the page name so that it is displayed as 'active' (highlighted in the navigation tabs to show this is the current page). The component will try to seek out the page name set in the title tag of the page if this is set to None.
        - (optional) LocalOrSessionStorage: where to store the current page selected. choices are [0,1]. 0 = local storage, 1 = session storage
        - (optional) serverRendering: use href links to navigate to pages instead of streamlit's extra component `switch_page`
        - (required) data: data used to build the side bar navigation:
            args:
                - index: required 
                - label: required - name of the navigation tab
                - icon: option - icon to be used for navigation tab. icon libraries: - Google-material-symbols, - Remix icon, - Tabler Icons, - Icon-8, - line-awesome
                - page: required - name of page as set in url. For example "http://localhost:8501/" would be "the name of the file" or "http://localhost:8501/data-test" would be "data-test"
                - href: optional - url to direct users to if using links to navigate to page. If `serverRendering` is True, this is required.
        - (optional) webMedium: Where is this page currently being displayed. Options: "local", "streamlit-cloud", "custom" - if you are using another service like AWS etc.
        - (optional) iframeContainer: Used to find head tag to append icon libraries so that they can be displayed. This is required if webMedium is `custom`.
    """

    def __init__(self, backgroundColor="black", activeBackgroundColor="red", navigationHoverBackgroundColor="gray", labelIconSize="17px", distanceIconLabel="12px", labelIconColor="white", closeNavOnLoad=True, loadPageName=None, LocalOrSessionStorage=0, serverRendering=False, data=None, webMedium="local", iframeContainer=None) -> None: 
        self.backgroundColor = backgroundColor
        self.activeBackgroundColor = activeBackgroundColor
        self.navigationHoverBackgroundColor = navigationHoverBackgroundColor
        self.labelIconSize = labelIconSize
        self.distanceIconLabel = distanceIconLabel
        self.labelIconColor = labelIconColor
        self.closeNavOnLoad = closeNavOnLoad
        self.loadPageName = loadPageName
        self.storageChoice = ["localStorage", "sessionStorage"][LocalOrSessionStorage]
        self.serverRendering = serverRendering
        self.data = data
        self.webMedium = webMedium
        self.iframeContainer = iframeContainer


    def defaultSidebarInit(self):
        """
        Create the sidebar when the page first loads. Set to make sure it only creates once if it already exists. 
        """

        if self.closeNavOnLoad:
            width = "0px"
            min_width = "0px"
            max_width = "0px"
            transform = "translateX(-336px)"
            padding="0px"
        else:
            width = "347px"
            min_width = "244px"
            max_width = "510px"
            transform = "none"
            padding="6rem 1rem"
        

        js_el = f'''

                    <script>
                        
                        
                        const sidebar = window.parent.document.body.querySelectorAll('section[class="custom-sidebar"]');
                        if (sidebar.length < 1){{
                            const createEL = parent.document.createElement("section");
                            createEL.className = "custom-sidebar";

                            if ("{self.loadPageName}" === "None"){{
                                pageName_ = window.parent.document.location.pathname.split("/")
                                pageName_ = pageName_[pageName_.length - 1]
                                if (pageName_ === ""){{
                                    pageName_to_save = {self.data}[0]["page"]
                                    {self.storageChoice}.setItem("currentPage", JSON.stringify({{"currentPage":pageName_to_save}}))
                                }} else {{
                                    
                                    {self.storageChoice}.setItem("currentPage", JSON.stringify({{"currentPage":pageName_}}))
                                }}
                                                             
                            createEL.style = "transition: width 300ms ease 0s, min-width 300ms ease 0s, max-width 300ms ease 0s, transform 300ms ease 0s; position:relative; height: 910px; box-sizing: border-box; flex-shrink:0; height:100vh; width:{width}; min-width:{min_width}; max-width:{max_width}; transform:{transform}; background-color:{self.backgroundColor}; color:white; z-index: 999991; padding:{padding};";
                            const body = window.parent.document.body.querySelectorAll('div[data-testid="stAppViewContainer"] > section[class*="main"]');
                            body[0].insertAdjacentElement('beforebegin',createEL);

                            const newSidebar = window.parent.document.body.querySelectorAll('section[class="custom-sidebar"]');
                            const containerForClose = document.createElement('div');
                            containerForClose.className = 'custom-sidebar-close-btn';
                            containerForClose.style = "position:absolute; top:2%; color:white; width:fit-content; right:15px; font-size:18px; cursor:pointer;";
                                                
                            const nav_emoji_close = document.createElement('i');
                            nav_emoji_close.className = 'ri-close-fill'; 

                            containerForClose.appendChild(nav_emoji_close)
                            newSidebar[0].appendChild(containerForClose)
                            
                            if ("{self.closeNavOnLoad}" === false){{
                                const containerForOpen = document.createElement('div')
                                containerForOpen.className = "custom-sidebar-open-button";
                                containerForOpen.style = "height:fit-content; visibility:hidden; padding-left:5px; padding-right:5px; color:black; z-index:999990; position:absolute; top:0.5rem; width:fit-content; left:0.5rem; font-size:18px; cursor:pointer;";

                                const nav_emoji_open = document.createElement('i');
                                nav_emoji_open.className = 'ri-arrow-right-s-line';
                                containerForOpen.appendChild(nav_emoji_open)
                                body[0].insertAdjacentElement('beforebegin',containerForOpen);
                            }}
                            

                            const parentElForNav = document.createElement('div');
                            parentElForNav.className = "navigation-container";

                            const listContainer = document.createElement('ul');
                            listContainer.className = "navigation";
                            listContainer.style = "list-style-type:none; padding-left:0px; margin-bottom:0px;";

                            {self.data}.forEach((el) => {{
                                const createListEl = document.createElement('li');

                                if ("{self.loadPageName}" === "None"){{
                                                               
                                    const currentPageLocalS = JSON.parse({self.storageChoice}.getItem("currentPage"))["currentPage"]
                                    
                                    if (el.page === currentPageLocalS){{
                                    
                                    createListEl.id = "active";
                                    createListEl.style.backgroundColor = "{self.activeBackgroundColor}";
                                    }} 
                                
                                }} else {{
                                    
                                    if (el.page === "{self.loadPageName}"){{
                                    createListEl.id = "active";
                                    createListEl.style.backgroundColor = "{self.activeBackgroundColor}";
                                    }} 

                                }}

                                if ("{self.serverRendering}" === "True"){{
                                    const navTabContent = document.createElement('a');
                                    navTabContent.className = "contents-container";
                                    navTabContent.style = "text-decoration:none; display:flex; flex-direction:row; cursor:pointer; padding:3px; padding-left:4px; border-radius:0.25rem; margin-left:5px; margin-right:5px; margin-bottom:3.5px;";
                                    navTabContent.href = el.href;

                                    if (el.icon){{
                                        const iconEl = document.createElement('i');
                                        iconEl.className = el.icon;
                                        iconEl.style.marginRight = "{self.distanceIconLabel}";
                                        iconEl.style.fontSize = "{self.labelIconSize}";
                                        iconEl.style.color = "{self.labelIconColor}";
                                        navTabContent.append(iconEl);
                                    }}

                                    

                                    const labelEl = document.createElement('span');
                                    labelEl.className = "navigation-label";
                                    labelEl.innerHTML = el.label;
                                    labelEl.style = "white-space:nowrap; display:table-cell;";
                                    labelEl.style.fontSize = "{self.labelIconSize}";
                                    labelEl.style.color = "{self.labelIconColor}";
                                    
                                    navTabContent.appendChild(labelEl);
                                    createListEl.append(navTabContent);
                                
                                    listContainer.appendChild(createListEl);
                                    createListEl.className = "label-icon-container"; 

                                }} else {{
                                    
                                    const navTabContent = document.createElement('div');
                                    navTabContent.className = "contents-container";
                                    navTabContent.style = "display:flex; flex-direction:row; cursor:pointer; padding:3px; padding-left:4px; border-radius:0.25rem; margin-left:5px; margin-right:5px; margin-bottom:3.5px;";
                                    
                                    if (el.icon){{
                                        const iconEl = document.createElement('i');
                                        iconEl.className = el.icon;
                                        iconEl.style.marginRight = "{self.distanceIconLabel}";
                                        iconEl.style.fontSize = "{self.labelIconSize}";
                                        iconEl.style.color = "{self.labelIconColor}";
                                        navTabContent.append(iconEl);
                                        //createListEl.appendChild(iconEl);
                                    }}


                                    const labelEl = document.createElement('span');
                                    labelEl.className = "navigation-label";
                                    labelEl.innerHTML = el.label;
                                    labelEl.style = "white-space:nowrap; display:table-cell;";
                                    labelEl.style.fontSize = "{self.labelIconSize}";
                                    labelEl.style.color = "{self.labelIconColor}";

                                    navTabContent.appendChild(labelEl);
                                    createListEl.append(navTabContent);
                                    
                                    listContainer.appendChild(createListEl);
                                    createListEl.className = "label-icon-container"; 
                                
                                }}                                                                                            

                            }})

                            parentElForNav.appendChild(listContainer)
                            
                            newSidebar[0].appendChild(parentElForNav);

                        }}
                    </script>


                '''
        st.components.v1.html(js_el, height=0, width=0)
    
    def active_navigation(self):
        """
        Configures the active navigation tabs - adds `active` id if tab is clicked, removes active style to tab clicked off and sets active style to newly clicked tab
        """

        js_el = f'''
                    
                    <script>
                        var navigationTabs = window.parent.document.querySelectorAll(".custom-sidebar > .navigation-container > .navigation > .label-icon-container");
                        navigationTabs.forEach((c) => {{
                            c.addEventListener("click", (e) => {{
                                
                                window.parent.document.querySelectorAll('#active')[0]?.removeAttribute('style')
                                window.parent.document.querySelectorAll('#active')[0]?.removeAttribute('id')
                                
                                c.id = "active";
                                c.style.backgroundColor = "{self.activeBackgroundColor}";
                                c.style.cursor = "pointer";
                                
                                {self.storageChoice}.setItem("currentPage", JSON.stringify({{"currentPage":c.querySelectorAll('span')[0].innerHTML.toLowerCase()}}))
                            }});
                        }});

                       
                    </script>

                '''
        st.components.v1.html(js_el, height=0, width=0)
    
    def disable_active_navigation_server_(self):
        """
        Relevant for server rendering - navigation via links. Deactivates active tab so that on click it does not redirect you back to the same page. 
        """

        custom_css = '''
                            <style>
                                li[id="active"] > a.contents-container {
                                    pointer-events: none;

                                }

                                li[id="active"] {
                                    cursor: pointer;
                                }
                            </style>
                        '''
        st.markdown(custom_css, unsafe_allow_html=True)

    
    def close_sidebar(self):
        """
        Configures sidebar being closed - uses streamlit native sidebar methods
        """


        js_el = f'''
                    <script>
                        
                            function closeSidebar() {{
                                const sidebar = window.parent.document.body.querySelectorAll('section[class="custom-sidebar"]');
                                sidebar[0].style = "transition: width 300ms ease 0s, min-width 300ms ease 0s, max-width 300ms ease 0s, transform 900ms ease 0s; width:0px; min-width:0px; max-width:0px; transform:translateX(-336px); position:relative; height: 910px; box-sizing: border-box; flex-shrink:0; background-color:{self.backgroundColor}; z-index: 999991; padding:6rem 1rem;";
                                const openNavBtn = window.parent.document.body.querySelectorAll('div[class="custom-sidebar-open-button"]');
                                openNavBtn[0].style = "padding-left:5px; padding-right:5px; visibility:visible; color:black; z-index:999990; position:absolute; top:0.5rem; width:fit-content; left:0.5rem; font-size:18px; cursor:pointer;";
                                openNavBtn[0].addEventListener('mouseover', function() {{
                                        openNavBtn[0].style = "padding-left:5px; padding-right:5px; background-color:rgba(237, 231, 225, 0.7); border-radius:6px; visibility:visible; color:black; z-index:999990; position:absolute; top:0.5rem; width:fit-content; left:0.5rem; font-size:18px; cursor:pointer;";
                            }});
                                openNavBtn[0].addEventListener('mouseout', function() {{
                                        openNavBtn[0].style = "padding-left:5px; padding-right:5px; visibility:visible; color:black; z-index:999990; position:absolute; top:0.5rem; width:fit-content; left:0.5rem; font-size:18px; cursor:pointer;";
                                }});
                                
                            }}
                            window.parent.document.querySelectorAll('.custom-sidebar-close-btn')[0].addEventListener("click", function(event) {{
                            
                                closeSidebar();
                                event.preventDefault();
                            }}, false);
                    </script>
                '''
        st.components.v1.html(js_el, height=0, width=0)

    def open_sidebar(self):
        """
        Configures sidebar being open - uses streamlit native sidebar methods
        """

        js_el = f'''
                    <script>
                        
                            function openSidebar() {{
                                const sidebar = window.parent.document.body.querySelectorAll('section[class="custom-sidebar"]');
                                sidebar[0].style = "transition: width 300ms ease 0s, min-width 300ms ease 0s, max-width 300ms ease 0s, transform 300ms ease 0s; transform:none; position:relative; height: 910px; box-sizing: border-box; flex-shrink:0; height:100vh; width:347px; min-width:244px; max-width:510px; background-color:{self.backgroundColor}; z-index: 999991; padding:6rem 1rem;";
                                const openNavBtn = window.parent.document.body.querySelectorAll('div[class="custom-sidebar-open-button"]');
                                openNavBtn[0].style = "visibility:hidden;"; 

                            }}
                            window.parent.document.querySelectorAll('.custom-sidebar-open-button')[0].addEventListener("click", function(event) {{
                            
                                openSidebar();
                                event.preventDefault();
                            }}, false);
                    </script>
                '''
        st.components.v1.html(js_el, height=0, width=0)
    
    def hoverOnLoad(self):
        """
        Configures open sidebar button being being hovered on. Rendered when page is loaded and uses st.markdown.
        """

        st.markdown(
            '''
                <style>
                    div[class="custom-sidebar-open-button"]:hover{
                        background-color: rgba(237, 231, 225, 0.7);
                        border-radius: 6px;
                        cursor: pointer;
                    }
                </style>
            ''',
            unsafe_allow_html=True
        )
    
    def hoverActiveNavigation(self):
        """
        Create hover effect for navigation tab, using st.markdown
        """

        st.markdown(
            f'''
                <style>
                    li[class="label-icon-container"]:hover{{
                        background-color: {self.navigationHoverBackgroundColor}; 
                        cursor: pointer;
                    }}

                    li[id="active"]:hover{{
                        background-color: {self.navigationHoverBackgroundColor} !important;
                    }}
                </style>
            ''',
            unsafe_allow_html=True
        )

    def hoverActiveNavigationJSExe(self):
        """
        Create hover effect for navigation tab, using javascript
        """

        js_el = f'''
                    <script>

                    var navigationTabs = window.parent.document.querySelectorAll("li.label-icon-container");
                    navigationTabs.forEach((c) => {{
                            
                            c.addEventListener('mouseover', function(e) {{
                                
                                    c.style.backgroundColor = "rgba(237, 231, 225, 0.7)" 
                                }});
                            c.addEventListener('mouseout', function(e) {{

                                if (c.id === "active"){{
                                    c.style.backgroundColor = "{self.activeBackgroundColor}"
                                }} else {{
                                    c.style.backgroundColor = "transparent" 
                                }}
                                    
                                    }});

                            console.log(c.style)

                            

                        }} )               
                        
                    </script>

                '''
        st.components.v1.html(js_el, height=0, width=0)


    def renderOpenBtn(self):
        """
        Renders open sidebar button when page loads. 
        """

        js_el = f'''
                    <script>
                            const containerForOpen = document.createElement('div');
                            containerForOpen.className = "custom-sidebar-open-button";
                            containerForOpen.style = "height:fit-content; visibility:visible; padding-left:5px; padding-right:5px; color:black; z-index:999990; position:absolute; top:0.5rem; width:fit-content; left:0.5rem; font-size:18px; cursor:pointer;";

                            const nav_emoji_open = document.createElement('i');
                            nav_emoji_open.className = 'ri-arrow-right-s-line';
                            containerForOpen.appendChild(nav_emoji_open);

                            const body = window.parent.document.body.querySelectorAll('div[data-testid="stAppViewContainer"] > section[class*="main"]');
                            body[0].insertAdjacentElement('beforebegin',containerForOpen);

                            
                    </script>
                '''
        
        st.components.v1.html(js_el, height=0, width=0)
                         
    def change_page(self):
        """
        Changes page using streamlit extras component `switch_page`. Gets the value of the current page from local or session storage and then changes page accordingly.
        """

        if self.storageChoice == "localStorage":
            localS = LocalStorage()
            pageSelect = localS.getItem("currentPage")
        else:
            sessionS = SessionStorage()
            pageSelect = sessionS.getItem("currentPage")
       
        if pageSelect != None and st.session_state["currentPage"]["page"] != pageSelect["storage"]["currentPage"]:
            switch_page(pageSelect["storage"]["currentPage"])

        
    
    def load_custom_sidebar(self):
        """
        Salad of methods used to create final sidebar
        """
        
        emojis_load = SidebarIcons(self.iframeContainer)
        if self.webMedium == "local":
            emojis_load.Load_All_CDNs()
        elif self.webMedium == "streamlit-cloud":
            emojis_load.Load_All_CDNs_to_streamlit_cloud()
        elif self.webMedium == "custom":
            emojis_load.custom_query_for_my_app_head_tag_CDN()
            
        self.defaultSidebarInit()
        self.active_navigation()
        self.renderOpenBtn()
        self.hoverOnLoad()
        self.open_sidebar()
        self.close_sidebar()
        self.hoverActiveNavigation()
        # self.hoverActiveNavigationJSExe()
        if self.serverRendering:
            self.disable_active_navigation_server_()

