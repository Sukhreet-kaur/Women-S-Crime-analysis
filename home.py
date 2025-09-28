import streamlit as st
import pandas as pd
import seaborn as  sb 
import matplotlib.pyplot as plt
# =============================
# Load data with cache
# =============================
@st.cache_data
def load_data():
    return pd.read_csv("women_crime_india_2001_2021_cleaned.csv")
st.markdown("""
<style>
            #MainMenu{
            visibility:hide;
            display:None;}
            .stMainMenu st-emotion-cache-czk5ss e8lvnlb8{
            display:None;
            }
</style>""",unsafe_allow_html=True)
df = load_data()
columns={'Rape':['rape','murder_with_rape','attempt_to_rape','gang_rape'],"Domestic Violence":['dowry_deaths','dowry_prohibition_act','cruelty_by_husband_or_relatives_498A','dowry_harassment']
         ,"Posco Cases":['pocso_rape','pocso_assault','pocso_harassment','child_marriage_prohibition_act','procuration_of_minor_girls','importation_of_girls'],
         "Outdoor Crime":['sexual_harassment_workplace','attempt_to_kidnap','cyber_stalking_bullying_against_women','cyber_crime_obscenity_against_women','trafficking','stalking_354D','acid_attack','attempt_to_acid_attack']}
# =============================
# Page setup (only once at top)
# =============================
st.set_page_config(
    page_title="Women's Crime",
    page_icon="👧"
)

# =============================
# CSS for styling
# =============================
st.markdown(
    """
    <style>
    #analysing-two-decades-of-crime{
        text-align:center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============================
# Session state navigation
# =============================
if "page" not in st.session_state:
    st.session_state.page = "home"  # default page

def go_to(page_name: str):
    st.session_state.page = page_name


# =============================
# HOME PAGE
# =============================
if st.session_state.page == "home":
    
    st.title("Women Crime in India (2001-2020)")
    st.subheader("Analysing Two decades of crime")
    st.markdown("  ")
    st.divider()

    st.text(
        "This project analyses women-related crime in India over two decades (2001-2020) "
        "to understand patterns, trends, and regional disparities. Studying crime over a "
        "long period helps identify persistent issues, emerging threats, and the effectiveness "
        "of policies and interventions. By examining this data, we can raise awareness, inform "
        "policymakers, and work towards creating safer environments for women across the country."
    )

    st.divider()
    st.markdown("### Let's have a look at our dataset first")

    n = st.number_input(
        label="How many starting rows you want to see",
        max_value=10000,
        min_value=0,
        step=1,
        placeholder=0
    )
    st.dataframe(df.head(n))

    st.markdown("#### Our data has the following configurations")
    st.markdown("- The number of rows and columns of our data is:")
    st.write(df.shape)

    if st.checkbox("Do you want to see various columns", value=False):
        st.markdown("- The various columns in our dataset are")
        st.write(df.columns)

    st.markdown("- For deeper analysis of the data")
    if st.checkbox("Do you want to search more about the DataFrame", value=False):
        b = st.multiselect(
            label="Select the columns you want to view",
            options=df.columns.tolist()
        )
        col = st.text_input("Enter an additional column name (optional)")
        cols_to_show = b.copy()

        if col:
            cols_to_show.append(col)

        if cols_to_show:
            missing_cols = [c for c in cols_to_show if c not in df.columns]
            if missing_cols:
                st.warning(f"These columns do not exist in the DataFrame: {missing_cols}")
            else:
                state_name = st.text_input("Enter the state name you want to explore")
                year_search = st.number_input(
                    "Enter the year if you want to search a particular year",
                    min_value=2001, step=1, format="%d"
                )

                if state_name and year_search > 0:
                    if state_name in df['state'].values and year_search in df['year'].values:
                        filtered_df = df[(df['state'] == state_name) & (df['year'] == int(year_search))]
                        st.dataframe(filtered_df[cols_to_show])
                    else:
                        st.warning("State or year not found in the DataFrame")

                elif state_name:
                    if state_name in df['state'].values:
                        filtered_df = df[df['state'] == state_name]
                        st.dataframe(filtered_df[cols_to_show])
                    else:
                        st.warning("State not found in the DataFrame.")

                elif year_search > 0:
                    if year_search in df['year'].values:
                        filtered_df = df[df['year'] == int(year_search)]
                        st.dataframe(filtered_df[cols_to_show])
                    else:
                        st.warning("Year not found!")

                st.write("The above data is settled as per the state and their districts in our DataFrame")
        else:
            st.info("Please select or enter columns to view.")

    st.divider()
    st.subheader("Visualize total cases as per state or year")
    if st.checkbox("Do you want to see the visualization", value=False):
        
        op = st.radio(label="Choose the Parameter to Analyse", index=None, options=("state", "year", "clear"))
        if op == "clear":
            pass
        else:
            if op!=None :
                r = df.groupby(op)['total_cases'].sum().reset_index()
                if op == 'year':
                    fig, ax = plt.subplots(figsize=(10, 8))
                    sb.lineplot(data=r, y='total_cases', x=op, color="red", ax=ax,marker='o')
                else:
                    fig, ax = plt.subplots(figsize=(15, 15))
                    sb.barplot(data=r, x='total_cases', y=op, color="darksalmon", hue='total_cases', ax=ax)

                st.pyplot(fig)
    st.divider()
    dcolumns=['rape', 'attempt_to_rape', 'gang_rape',
       'murder_with_rape', 'kidnapping_and_abduction', 'dowry_deaths',
       'dowry_prohibition_act', 'cruelty_by_husband_or_relatives_498A',
       'acid_attack', 'attempt_to_acid_attack', 'assault_on_women_modesty_354',
       'assault_intent_disrobe_354B', 'voyeurism_354C', 'stalking_354D',
       'insult_to_modesty_509', 'trafficking', 'procuration_of_minor_girls',
       'importation_of_girls', 'immoral_traffic_act',
       'indecent_representation_of_women', 'women_killed_in_honour_killing',
       'witch_hunting', 'cyber_crime_obscenity_against_women',
       'cyber_stalking_bullying_against_women',
       'child_marriage_prohibition_act', 'pocso_rape', 'pocso_assault',
       'pocso_harassment', 'pocso_unnatural_offences', 'pocso_other',
       'abduction_for_marriage', 'abduction_for_illicit_intercourse',
       'attempt_to_kidnap', 'domestic_violence_act_cases',
       'abetment_to_suicide_women', 'attempt_to_murder_women',
       'insult_outraging_modesty_other', 'sexual_harassment_workplace',
       'dowry_harassment', 'marital_rape_reports', 'total_cases']
    st.subheader("Understand the correlation between different types of crimes")
    if st.checkbox("Do you want to see the correlation", value=False):
        crime = st.multiselect("Choose the type of Crime", options=dcolumns, placeholder=None)
        if len(crime) < 2:
            st.info("Please select at least two columns to view the correlation.")
        else:
            op = st.radio("Choose the type of plot", options=('Scatter', 'Heatmap'), index=None)
            if op == 'Scatter':
                if len(crime) == 2:
                    st.write("If the regression coefficient is positive, the line will be upward, otherwise downward")

                    # Toggle to choose raw vs normalized
                    use_normalized = st.checkbox("Use Normalized Data (per total cases)", value=False)

                    if use_normalized:
                        x_data = df[crime[0]] / df["total_cases"]
                        y_data = df[crime[1]] / df["total_cases"]
                    else:
                        x_data = df[crime[0]]
                        y_data = df[crime[1]]

                    fig, ax = plt.subplots(figsize=(10, 8))
                    sb.regplot(x=x_data, y=y_data, ax=ax)
                    ax.set_title(f"Regression Correlation between {crime[0]} and {crime[1]}")
                    st.pyplot(fig)
                else:
                    st.info("Please choose exactly two Crime Category")
            if op == "Heatmap":
                df_normalized = df[dcolumns]
                for col in dcolumns:
                    df_normalized[col] = df[col] / df['total_cases']
                corr = df_normalized[crime].corr()
                fig, ax = plt.subplots()
                sb.heatmap(data=corr, cmap='Blues', ax=ax, annot=True)
                plt.title("Correlation between variables")
                st.pyplot(fig)
    st.divider()
    st.markdown("### From the above data we are now familiar with the columns")
    st.write("Now choose the category of crime you want to analyse:")
    st.write("Kindly scroll to the top after clicking the button as new page will load")
    a = st.selectbox(
        label="Select the category to analyse",
        options=("Rape Cases", "Domestic Violence", "Posco Cases", "Outdoor Crime"),
        index=None,
        placeholder="Choose one..."
    )

    def handle_navigation():
        if a == "Rape Cases":
            go_to("rape")
        elif a == "Domestic Violence":
            go_to("domestic")
        elif a == "Posco Cases":
            go_to("posco")
        elif a == "Outdoor Crime":
            go_to("outdoor")

    st.button("Show Analysis", on_click=handle_navigation)



# =============================
def crime_analysis_page(case_name, columns):
    
    st.title(f"{case_name} Cases Analysis")
    st.write("Double click the button to go back to")
    if st.button("⬅ Back to Home"):
        go_to("home")

    st.subheader(f"This Section will analyse the {case_name} cases")

    # =============================
    # Data preview for selected state/year
    # =============================
    if st.checkbox(f"Want to see the {case_name} data", value=False):
        state_name = st.text_input("Enter the state name you want to explore", placeholder=None)
        year_search = st.number_input("Enter the year if you want to search a particular year",
                                      min_value=2001, step=1, format="%d")
        if state_name and year_search > 0:
            if state_name in df['state'].values and year_search in df['year'].values:
                filtered_df = df[(df['state'] == state_name) & (df['year'] == int(year_search))]
                st.dataframe(filtered_df[["state", "year"] + columns])

    st.divider()
    st.subheader("This area helps us to analyse the frequency of the cases")
    st.write("With the help of the histogram we will analyse the frequency of the crime")

    op = st.selectbox("Select the type of case", options=columns, index=None, placeholder="Choose One")
    ryear = st.number_input("Choose a particular year", min_value=2001, step=1, format="%d")
    hide_plot = st.checkbox("Hide Graph", value=False)

    if hide_plot:
        st.info("Your Graph data is hidden!!")
    else:
        df1 = df[df['year'] == ryear]
        if op:
            fig, ax = plt.subplots()
            sb.histplot(data=df1, x=op, kde=True, ax=ax)
            plt.title(f"The frequency of {op} cases in India")
            st.write("It also helps to check the skewness of data")
            st.pyplot(fig)
        else:
            st.info("Select a Valid Option")

    st.divider()
    st.subheader("Check the trend of Crime with year")
    op_line = st.selectbox("Select the type of case", options=columns, index=None,
                           placeholder="Choose One", key=f"line_{case_name}")
    if op_line:
        fig, ax = plt.subplots()
        sb.lineplot(data=df, y=op_line, x=df['year'], ax=ax)
        plt.title("Crime rate over different years")
        st.pyplot(fig)

    st.divider()
    st.subheader("Analyse Crime either by state or year")
    op = st.radio("Choose the first Parameter to Analyse", index=None, options=("state", "year", "clear"))
    crime = st.radio("Choose the type of Crime", options=columns + ["clear"], index=None)
    if st.checkbox("Hide", value=False, key=f"multi_data_{case_name}"):
        st.info("You have to Unhide to see the analysis")
    else:
        if op == "clear" or crime == "clear":
            pass
        else:
            if op!=None and crime!=None :
                r = df.groupby(op)[crime].sum().reset_index()
                if op == 'year':
                    fig, ax = plt.subplots(figsize=(10, 8))
                    r = df.groupby('year')[crime].sum().reset_index()
                    sb.barplot(data=r, y=crime, x=op, color="skyblue", hue=crime, ax=ax)
                else:
                    fig, ax = plt.subplots(figsize=(15, 15))
                    sb.barplot(data=r, x=crime, y=op, color="darksalmon", hue=crime, ax=ax)
                st.pyplot(fig)

    st.divider()
    st.subheader("Multiple Parameter Analysis")
    crime = st.multiselect("Choose the type of Crime", options=columns + ["clear"], placeholder=None)
    crime = [c for c in crime if c != 'clear']
    rstate = st.text_input("Enter the Particular State", placeholder=None)
    ryear = st.number_input("Choose a year", min_value=2001, step=1, format="%d", key=f"year_{case_name}")

    if len(crime) != 2:
        st.info("Please Select just two type of Crime Category")
    else:
        if rstate and ryear:
            r = df.groupby(['state', 'year'])[crime].sum().reset_index()
            r = r[(r['state'] == rstate) & (r['year'] == ryear)]
            if st.checkbox("Hide", value=False, key=f"multianalysis_{case_name}"):
                st.info("You have to Unhide to see the analysis")
            else:
                fig, ax = plt.subplots()
                sb.lineplot(data=df, x=crime[0], y=crime[1], ax=ax)
                plt.title("Analysis of two Crime in Particular state and year")
                st.pyplot(fig)

    st.divider()
    st.subheader("Some Statistical Analysis")
    st.write("For Clearing the graph just deselect the parameters")
    if st.checkbox("Do you want to see the Statistical Analysis", value=False, key=f"stat_{case_name}"):
        crime = st.multiselect("Choose the type of Crime", options=columns,
                               key=f'statcrime_{case_name}', placeholder=None)
        op = st.radio("Choose the plots you want to Analyse", options=('Scatter', 'Heatmap'), index=None)

        if op == 'Scatter':
            if len(crime) == 2:
                st.write("If the regression coefficient is positive, the line will be upward, otherwise downward")
                fig, ax = plt.subplots(figsize=(10, 8))
                plt.title("Regression Correlation between two variables")
                sb.regplot(data=df, x=crime[0], y=crime[1])
                st.pyplot(fig)
            else:
                st.info("Please choose exactly two Crime Category")
        if op == "Heatmap":
            cor = df[crime].corr()
            fig, ax = plt.subplots()
            sb.heatmap(data=cor, cmap='Blues', ax=ax, annot=True)
            plt.title("Correlation between variables")
            st.pyplot(fig)
######################
# Rape Page

def go_to(page_name: str):
    st.session_state.page = page_name

if "page" not in st.session_state:
    st.session_state.page = "home"  # default page

elif st.session_state.page == "rape":
    # rape_columns = ["rape", "murder_with_rape", "gang_rape", "attempt_to_rape"]
    crime_analysis_page("Rape", columns['Rape'])

# Domestic Violence Page
elif st.session_state.page == "domestic":
    
    crime_analysis_page("Domestic Violence", columns['Domestic Violence'])
elif st.session_state.page=='posco':
    crime_analysis_page("Posco Cases",columns['Posco Cases'])
elif st.session_state.page=='outdoor':
    crime_analysis_page("Posco Cases",columns["Posco Cases"])
print(df.columns)
