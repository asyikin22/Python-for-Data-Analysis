import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


#####################################################################################################################

# Sidebar with clickable sections
st.sidebar.title("Choose a Section:")

# Create a list of sections with buttons in the sidebar
sections = ["Geographical Overview", "State Population", "Gender - Ethnicity", "Diversity Index", "Sources"]

# Initialize a session state variable to track the selected section
if 'selected_section' not in st.session_state:
    st.session_state.selected_section = sections[0]  # Default to "Introduction"

    
# # Custom CSS for hover effect and styling
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
            margin-bottom: 10px;
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

# Add horizontal line after section buttons
st.sidebar.markdown('<div class="sidebar-line"></div>', unsafe_allow_html=True)


# Main content area based on the selected section
if st.session_state.selected_section == "Geographical Overview":
    st.title("Malaysia - Geographical Overview")
    st.subheader("The map shows Malaysian population across states from 1980 to 2020")
    import streamlit as st

    # Example of a justified paragraph with customized width
    st.markdown("""
        <div style="text-align: justify; width: 800px;">
            The map of Malaysia consists of two distinct regions: Peninsular Malaysia (also known as West Malaysia), 
            which is located on the southernmost tip of the Asian continent, and East Malaysia, which is situated on 
            the island of Borneo. The country is bordered by Thailand to the north, Singapore to the south, Brunei 
            and Indonesia to the east, and the South China Sea to the west. Malaysia features a diverse landscape of 
            coastal plains, mountain ranges, and tropical rainforests, with the iconic capital city, Kuala Lumpur, 
            located in the west.
        </div>
    """, unsafe_allow_html=True)

    # Load HTML map for population breakdown 
    with open("static/charts_html/map_pop2.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=600, width=1000)
                
elif st.session_state.selected_section == "State Population":
    st.title("Distribution of Population")
    
    st.subheader("Chart 1: Animated race chart")    
    st.write("The animated race chart shows population shift across states from 1980 to 2020 ")    
    with open("static/charts_html/race-charts-state.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=600, width=1000)  
    st.markdown(
    """
    <div style="width: 800px; text-align: justify;">
        In 1980, Perak had the highest population in Malaysia, followed by Johor, Selangor, Sarawak, and Kedah. 
        However, after 1985, Selangor, Johor, and Sabah surpassed Perak in population. 
        From that point on, Selangor led the state's population growth, with its population exceeding half a million in the early 2000s.
    </div>
    """, 
    unsafe_allow_html=True
)
    
    st.markdown("<hr style='border: 1px solid red; width: 800px;'>", unsafe_allow_html=True)

            
    st.subheader("Chart 2: Population across states from 1980 to 2020")
    st.write("The chart represents the trend of Malaysian population across states from 1980 to 2020")
    with open("static/charts_html/state-pop-trend.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=500, width=800)
    st.markdown(
    """
    <div style="width: 800px; text-align: justify;">
        In 1980, all states in Malaysia had populations below 2 million. By 1990, Several states had grown steadily and surpassed the 2 million mark. 
        Selangor experienced the most significant growth, nearing 7 million people to date, while Johor and Sabah followed with populations around 4 million. 
        Due to its small size, Perlis showed very slow growth, with a population of around 300,000 in 2020.
    </div>
    """, 
    unsafe_allow_html=True
)
    
    st.markdown("<hr style='border: 1px solid red; width: 800px;'>", unsafe_allow_html=True)
    
    st.subheader("Chart 3: State Population from 1980 to 2020")
    st.write("The chart shows breakdown of Malaysian population across states from 1980 to 2020")
    with open("static/charts_html/pop_state.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=400, width=800)
  
elif st.session_state.selected_section == "Gender - Ethnicity":
    st.title("Gender & Ethnicity Distribution")
    
    st.subheader("Chart 1: Gender & Ethnicity - Trend Across Population")
    st.write("The line chart shows the population trend by gender and ethnicity from 1980 to 2020")
    # Load and display the first chart (adjust the path to the chart)
    with open("static/charts_html/gender-eth-trend.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=450, width=1200)
        
    
    st.markdown("<hr style='border: 1px solid red; width: 1200px;'>", unsafe_allow_html=True)
    
    st.subheader("Chart 2: Gender & Ethnicity in General Population")
    st.write("The chart shows breakdown of Malaysian population by gender and ethnicity from 1980 to 2020")
    with open("static/charts_html/gender-eth.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=420, width=800)
    
    st.markdown("<hr style='border: 1px solid red; width: 800px;'>", unsafe_allow_html=True)
    
    st.subheader("Chart 3: Ethnicity Across States")
    st.write("The chart shows breakdown of Malaysian population by ethnicity across states from 1980 to 2020")
    with open("static/charts_html/bubble-charts-state.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=600, width=1200)
    
    st.markdown(
    """
    <div style="width: 800px; text-align: justify;">
        In 1980, Bumiputera was the dominant ethnicity across all states, with the highest populations in Sarawak, 
        followed by Johor, Kelantan, Perak, and Kedah, each with populations close to 1 million. Kuala Lumpur and Penang were exceptions, 
        where the Chinese dominated with populations around 500,000. Despite being the second-largest ethnic group, 
        the Chinese population was nearly equal to the Bumiputera in Johor, Melaka, Negeri Sembilan, Perak, and Selangor. 
        Kelantan and Terengganu had a significant racial disparity, with Bumiputera clearly outnumbering other races. 
        Bumiputera growth has been rapid, surpassing the initially dominant Chinese population in Kuala Lumpur by the early 2000s, 
        and more recently in Penang, where the populations of Bumiputera and Chinese are now almost equal. 
        Overall, Bumiputera has seen the highest growth across all states, reaching a population of 7 million in 2020.
    </div>
    """, 
    unsafe_allow_html=True
    )
    
    st.markdown("<hr style='border: 1px solid red; width: 800px;'>", unsafe_allow_html=True)
    
    
    st.subheader("Chart 4: Gender & Ethnicity Across States")
    st.write("The chart shows breakdown of Malaysian population by gender and ethnicity across states from 1980 to 2020")
    components.iframe("https://pop-dash.onrender.com/", height=600, width=700)

elif st.session_state.selected_section == "Diversity Index":
    st.title("Diversity Index Across States")
    st.write("This section shows visualizations of diversity analysis using Shannon-Wiener Index Diversity Index to measure the diversity across states in Malaysia from 1980 to 2020")
    
    with open("static/charts_html/div-index.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=400, width=1200)
    
    st.markdown("""
    <div style="text-align: justify; width: 800px; margin: auto;">
    Kuala Lumpur and Selangor, which are highly urbanized, have the highest diversity scores. 
    This reflects the mixed ethnicities in cities and the presence of many different groups. 
    Terengganu and Kelantan, which are less urbanized, have lower diversity scores, 
    likely due to higher concentrations of specific ethnic or racial groups, particularly the Malay population in these regions.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid red; width: 800px;'>", unsafe_allow_html=True)
    
        
    with open("static/charts_html/div-stats.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=400, width=1200)
    
    st.markdown(
    """
    <div style="width: 800px; text-align: justify;">
    Most states exhibit relatively low standard deviations, suggesting that the diversity index values are fairly consistent within each state. 
    Sabah has the highest standard deviation indicating more variability in ethnic diversity within the state compared to others. 
    The minimum and maximum diversity values show that all states, except for Terengganu, have considerable variation in their diversity indexes, 
    which is typical as regions with large cities will naturally have more diversity. The diversity across Malaysia is uneven, with some states exhibiting a greater ethnic mix than others.
    </div>
    """, unsafe_allow_html=True
    )
    
    st.markdown("<hr style='border: 1px solid red; width: 850px;'>", unsafe_allow_html=True)
    
    with open("static/charts_html/racial-trend.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=600, width=1200)

    st.markdown(
    """
    <div style="width: 800px; text-align: justify;">
        All states in Malaysia are experiencing a consistent decline in ethnic diversity, with Sabah and Perlis showing the steepest decline, indicating a growing racial gap. 
        Despite being among the most diverse states, Selangor, Negeri Sembilan, Kuala Lumpur, Perak, and Pulau Pinang are also seeing a decrease in diversity over time. 
        Johor, however, stands out as the only state exhibiting a stable and constant diversity trend, indicating it has managed to retain a relatively equal distribution of different ethnic groups.
    </div>
    """, unsafe_allow_html=True
    )
    
    st.markdown("<hr style='border: 1px solid red; width: 850px;'>", unsafe_allow_html=True)
    
    # Shannon Diversity Index Formula
    st.subheader("The formula for the Shannon Diversity Index (H'):")
    st.latex(r"H' = - \sum_{i=1}^S p_i \ln(p_i)")
        
    st.markdown("""
    - **H'**: Shannon Diversity Index (a measure of diversity in a community).
    - **S**: Total number of species (or categories) in the community.
    - **pᵢ**: Proportion of individuals belonging to species *i*:
    - \( pᵢ = \frac{nᵢ}{N} \)
    - \( nᵢ \): Number of individuals of species *i*.
    - \( N \): Total number of individuals across all species.
    - **ln**: Natural logarithm (base *e*).
    """)
    
    st.markdown("""
    ### Scoring the Shannon Diversity Index

    - **Higher values of H'** indicates greater diversity.
    - **Lower values of H'** indicates lower diversity.
    """)

elif st.session_state.selected_section == "Sources":
    st.title("Links")
    st.write("""
    - [My GitHub](https://github.com/asyikin22/Python-for-Data-Analysis/tree/main/PROJECTS/Population)  
    - [Malaysia's Official Open Data Portal](https://data.gov.my/)  
    - [Malaysia Informative Data Center](https://mysidc.statistics.gov.my/index.php?lang=en#)  
    - [Malaysia's National Statistic Organisation](https://open.dosm.gov.my/dashboard/population)  
    """)

    


