import streamlit as st
import streamlit.components.v1 as components

# st.title("Hello, I'm Asyikin")
# st.write("This is running in VS code")

import streamlit as st
import streamlit.components.v1 as components

# Set the page config for layout
st.set_page_config(page_title="Sidebar with Clickable Sections", layout="wide")

# Sidebar with clickable sections
st.sidebar.title("Choose a Section")

# Create a list of sections with buttons in the sidebar
sections = ["General Population", "State Population", "Gender - Ethnicity", "Diversity Index"]

# Initialize a session state variable to track the selected section
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = sections[0]  # Default to "Introduction"
    
# Custom CSS for hover effect and styling
st.markdown("""
    <style>
        /* Remove margin and padding from sidebar */
        .css-1d391kg {  /* Sidebar container */
            padding-top: 0px !important;
            margin-top: 0px !important;
        }

        .css-1d391kg .element-container {
            padding-top: 0px !important;
            margin-top: 0px !important;
        }
        .stButton > button {
            width: 80% !important;
            padding: 10px !important;
            text-align: left !important;
            border: none !important;
            border-radius: 5px !important;
            margin-bottom: 5px;
            transition: background-color 0.3s ease;
        }
        
        .stButton > button:hover {
            background-color: #f1f1f1 !important;  /* Light grey on hover */
        }
    </style>
""", unsafe_allow_html=True)

# Display clickable buttons for each section
for section in sections:
    if st.sidebar.button(section):
        st.session_state.selected_section = section

# Main content area based on the selected section
if st.session_state.selected_section == "General Population":
    st.title("Population Breakdown Across States")
    st.write("The map shows Malaysian population across states from 1980 to 2020")
    
    # Load HTML map for population breakdown (assuming the file exists)
    with open("charts_html/map_pop.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=600, width=900)
        
elif st.session_state.selected_section == "State Population":
    st.title("Distribution of Population Across States")
    
    st.subheader("Chart 1: State Population from 1980 to 2020")
    st.write("The chart shows breakdown of Malaysian population across states from 1980 to 2020")
    # Load and display the second chart (adjust the path to the chart)
    with open("charts_html/pop_state.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=400, width=800)
    
    with open("charts_html/race-charts-state.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=600, width=1000)  
  
elif st.session_state.selected_section == "Gender - Ethnicity":
    st.title("Gender & Ethnicity Distribution")
    
    st.subheader("Chart 1: Gender & Ethnicity in General Population")
    st.write("The chart shows breakdown of Malaysian population by gender and ethnicity from 1980 to 2020")
    # Load and display the first chart (adjust the path to the chart)
    with open("charts_html/gender-eth.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=420, width=800)
    
    st.subheader("Chart 2: Ethnicity Across States")
    st.write("The chart shows breakdown of Malaysian population by ethnicity across states from 1980 to 2020")
    with open("charts_html/bubble-charts-state.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=600, width=1200)
    
    st.subheader("Chart 3: Gender & Ethnicity Across States")
    st.write("The chart shows breakdown of Malaysian population by gender and ethnicity across states from 1980 to 2020")
    components.iframe("http://127.0.0.1:8042", height=600, width=700)

elif st.session_state.selected_section == "Diversity Index":
    st.title("Diversity Index Across States")
    st.write("This section shows visualizations of the data.")
    
    with open("charts_html/div-index.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=400, width=1200)
        
    with open("charts_html/div-stats.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=400, width=1200)
    
    with open("charts_html/racial-trend.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=600, width=1200)
    
# Adding GitHub and source links at the bottom of the sidebar
st.sidebar.markdown("### Links")
st.sidebar.markdown("[GitHub - My Project](https://github.com/yourusername)")
st.sidebar.markdown("[Source 1 - Data Analysis Methodology](https://source1.com)")
st.sidebar.markdown("[Source 2 - Visualization Techniques](https://source2.com)")
st.sidebar.markdown("[Source 3 - Research Paper on Topic](https://source3.com)")
