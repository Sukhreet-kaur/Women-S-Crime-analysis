
# =============================
# RAPE PAGE
# =============================
elif st.session_state.page == "rape":
    st.title("Rape Cases Analysis")

    if st.button("⬅ Back to Home",key='rape'):
        go_to("home")

    st.subheader("This Section will analyse the rape cases")

    if st.checkbox("Want to see the rape data", value=False):
        rstate_name=st.text_input("Enter the state name you want to explore",placeholder=None)
        ryear_search=st.number_input("Enter the year if you want to search a particular year",min_value=2001,step=1,format="%d")
        if rstate_name and ryear_search>0:
            if rstate_name in df['state'].values and ryear_search in df['year'].values:
                filtered_df=df[(df['state']==rstate_name) & (df['year']==int(ryear_search))]
                st.dataframe(filtered_df[["state","year","rape","murder_with_rape","gang_rape","attempt_to_rape"]])
    st.divider()
    st.subheader("This area helps us to analyse the frequency of the rape cases")
    st.write("With the help of the histogram we will analys ethe freqency of the crime")
    
    op=st.selectbox(label="Select the type of Rape case",options=("rape","murder_with_rape","gang_rape","attempt to rape"),index=None,placeholder="Choose One")
    ryear=st.number_input(label="Choose a particular year",min_value=2001,step=1,format="%d")
    hide_plot = st.checkbox("Hide Graph", value=False)
    
    if hide_plot:
        st.info("Your Graph data is hidden!!")
    else:
        df1=df[df['year']==ryear]
        if op=='rape':
            fig,ax=plt.subplots()
            sb.histplot(data=df1,x='rape',kde=True,ax=ax)
            plt.title("The frequency of Rape cases in India")
            st.write("It also helps to check the skewness of data")
            st.pyplot(fig)
        elif op=='murder_with_rape':
            fig,ax=plt.subplots()
            sb.histplot(data=df1,x='murder_with_rape',kde=True,ax=ax)
            plt.title("The frequency of Murder with Rape cases in India")
            st.write("It also helps to check the skewness of data")
            st.pyplot(fig)
        elif op=='attempt to rape':
            fig,ax=plt.subplots()
            sb.histplot(data=df1,x='attempt_to_rape',kde=True,ax=ax)
            plt.title("The frequency of Attempt to Rape cases in India")
            st.write("It also helps to check the skewness of data")
            st.pyplot(fig)
        elif op=='gang_rape':
            fig,ax=plt.subplots()
            sb.histplot(data=df1,x='gang_rape',kde=True,ax=ax)
            plt.title("The frequency of Gang Rape cases in India")
            st.write("It also helps to check the skewness of data")
            st.pyplot(fig)
        else:
            st.info("Select a Valid Option")
    st.divider()
    st.subheader("Check the trend of Crime with year")
    op_line=st.selectbox(label="Select the type of Rape case",options=("rape","murder_with_rape","gang_rape","attempt_to_rape"),index=None,placeholder="Choose One",key="line_rape")
    if op_line :
        fig,ax=plt.subplots()
        sb.lineplot(data=df,y=op_line,x=df['year'],ax=ax)
        plt.title("Crime rate over different years")
        st.pyplot(fig)
    st.divider()
    st.subheader("Analyse Crime either by state or year")
    op=st.radio(label="Choose the first Parameter to Analyse",index=None,options=("state","year","clear"))
    crime=st.radio(label="Choose the type of Crime",options=("rape","murder_with_rape","attempt_to_rape","gang_rape","clear"),index=None)
    if st.checkbox(label="Hide",value=False,key="multi_data"):
        st.info("You have to Unhide to see the analysis")
    else:
        if op=="clear" or crime=="clear":
            pass
        else:
            if(op!=None):
                r=df.groupby(op)[crime].sum().reset_index()
                if(op=='year'):
                    fig,ax=plt.subplots(figsize=(10,8))
                    r=df.groupby('year')[crime].sum().reset_index()
                    sb.barplot(data=r,y=crime,x=op,color="skyblue",hue=crime,ax=ax)
                else:
                    fig,ax=plt.subplots(figsize=(15,15))
                    sb.barplot(data=r,x=crime,y=op,color="darksalmon",hue=crime,ax=ax)
                
                st.pyplot(fig)
    st.divider()
    st.subheader("Multiple Parameter Analysis")
    # op=st.radio(label="Choose the first Parameter to Analyse",index=None,options=("state","year","clear"),key="rapemulti")
    crime=st.multiselect(label="Choose the type of Crime",options=("rape","murder_with_rape","attempt_to_rape","gang_rape","clear"),placeholder=None)
    crime = [c for c in crime if c != 'clear']
    rstate=st.text_input(label="Enter the Particular State",placeholder=None)
    ryear=st.number_input(label="Choose a year",min_value=2001,step=1,format="%d")
    if len(crime)!=2:
        st.info("Please Select just two type of Crime Category")
    else:
        if rstate and ryear:
            r=df.groupby(['state','year'])[crime].sum().reset_index()
            r=r[(r['state']==rstate) & (r['year']==ryear)]
            if st.checkbox(label="Hide",value=False,key="multianalysis"):
                st.info("You have to Unhide to see the analysis")
            else:
                fig,ax=plt.subplots()
                sb.lineplot(data=df,x=crime[0],y=crime[1],ax=ax)
                plt.title("Analysis of two Crime in Particular state and year")
                st.pyplot(fig)
    st.divider()
    st.subheader("Some Statistical Analysis")
    st.write("For Clearing the graph just deselect the parameters")
    if st.checkbox(label="Do you want to see the Statistical Analysis",value=False,key="stat"):

        crime=st.multiselect(label="Choose the type of Crime",options=("rape","murder_with_rape","attempt_to_rape","gang_rape"),key='statcrime',placeholder=None)
        op=st.radio(label="Choose the plots you wan to Analyse",options=('Scatter','Heatmap'),index=None)
        if op == 'Scatter':
            if(len(crime)==2):
                st.write("If the regression cofficient will be positive the line will be in upward direction otherwise in downword direction")
                fig,ax=plt.subplots(figsize=(10,8))
                    # r=df.groupby('year')[crime].mean().reset_index()
                plt.title("Regression Coorelation between two variables")
                sb.regplot(data=df,x=crime[0],y=crime[1])
                st.pyplot(fig)
            else:
                st.info("PLease choose exact two Crime Category")
        if op=="Heatmap":
            cor=df[crime].corr()
            fig,ax=plt.subplots()
            sb.heatmap(data=cor,cmap='Blues',ax=ax,annot=True)
            plt.title("Correlation between two variables")
            st.pyplot(fig)

# DOMESTIC VIOLENCE PAGE
# =============================
elif st.session_state.page == "domestic":
    st.title("Domestic Violence Cases Analysis")

    if st.button("⬅ Back to Home"):
        go_to("home")

    st.subheader("This Section will analyse the Domestic Violence cases")

    if st.checkbox("Want to see the Domestic Violence data", value=False):
        dstate_name = st.text_input("Enter the state name you want to explore", placeholder=None)
        dyear_search = st.number_input("Enter the year if you want to search a particular year",
                                       min_value=2001, step=1, format="%d")
        if dstate_name and dyear_search > 0:
            if dstate_name in df['state'].values and dyear_search in df['year'].values:
                filtered_df = df[(df['state'] == dstate_name) & (df['year'] == int(dyear_search))]
                st.dataframe(filtered_df[["state", "year", "cruelty_by_husband_or_relatives_498A",
                                          "dowry_prohibition_act", "dowry_deaths", "dowry_harassment"]])
    st.divider()
    st.subheader("This area helps us to analyse the frequency of Domestic Violence cases")
    st.write("With the help of the histogram we will analyse the frequency of the crime")

    op = st.selectbox(label="Select the type of Domestic Violence case",
                      options=("cruelty_by_husband_or_relatives_498A", "dowry_prohibition_act",
                               "dowry_deaths", "dowry_harassment"),
                      index=None, placeholder="Choose One")
    dyear = st.number_input(label="Choose a particular year", min_value=2001, step=1, format="%d")
    hide_plot = st.checkbox("Hide Graph", value=False)

    if hide_plot:
        st.info("Your Graph data is hidden!!")
    else:
        df1 = df[df['year'] == dyear]
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
    op_line = st.selectbox(label="Select the type of Domestic Violence case",
                           options=("cruelty_by_husband_or_relatives_498A", "dowry_prohibition_act",
                                    "dowry_deaths", "dowry_harassment"),
                           index=None, placeholder="Choose One", key="line_domestic")
    if op_line:
        fig, ax = plt.subplots()
        sb.lineplot(data=df, y=op_line, x=df['year'], ax=ax)
        plt.title("Crime rate over different years")
        st.pyplot(fig)

    st.divider()
    st.subheader("Analyse Crime either by state or year")
    op = st.radio(label="Choose the first Parameter to Analyse", index=None, options=("state", "year", "clear"))
    crime = st.radio(label="Choose the type of Crime",
                     options=("cruelty_by_husband_or_relatives_498A", "dowry_prohibition_act",
                              "dowry_deaths", "dowry_harassment", "clear"), index=None)
    if st.checkbox(label="Hide", value=False, key="multi_data_domestic"):
        st.info("You have to Unhide to see the analysis")
    else:
        if op == "clear" or crime == "clear":
            pass
        else:
            if op!=None or crime!=None:
                r = df.groupby(op)[crime].sum().reset_index()
                if op == 'year':
                    fig, ax = plt.subplots(figsize=(10, 8))
                    sb.barplot(data=r, y=crime, x=op, color="skyblue", hue=crime, ax=ax)
                else:
                    fig, ax = plt.subplots(figsize=(15, 15))
                    sb.barplot(data=r, x=crime, y=op, color="darksalmon", hue=crime, ax=ax)

                st.pyplot(fig)

    st.divider()
    st.subheader("Multiple Parameter Analysis")
    crime = st.multiselect(label="Choose the type of Crime",
                           options=("cruelty_by_husband_or_relatives_498A", "dowry_prohibition_act",
                                    "dowry_deaths", "dowry_harassment", "clear"), placeholder=None)
    crime = [c for c in crime if c != 'clear']
    dstate = st.text_input(label="Enter the Particular State", placeholder=None)
    dyear = st.number_input(label="Choose a year", min_value=2001, step=1, format="%d", key="year_domestic")

    if len(crime) != 2:
        st.info("Please Select just two type of Crime Category")
    else:
        if dstate and dyear:
            r = df.groupby(['state', 'year'])[crime].sum().reset_index()
            r = r[(r['state'] == dstate) & (r['year'] == dyear)]
            if st.checkbox(label="Hide", value=False, key="multianalysis_domestic"):
                st.info("You have to Unhide to see the analysis")
            else:
                fig, ax = plt.subplots()
                sb.lineplot(data=df, x=crime[0], y=crime[1], ax=ax)
                plt.title("Analysis of two Crime in Particular state and year")
                st.pyplot(fig)

    st.divider()
    st.subheader("Some Statistical Analysis")
    st.write("For Clearing the graph just deselect the parameters")
    if st.checkbox(label="Do you want to see the Statistical Analysis", value=False, key="stat_domestic"):
        crime = st.multiselect(label="Choose the type of Crime",
                               options=("cruelty_by_husband_or_relatives_498A", "dowry_prohibition_act",
                                        "dowry_deaths", "dowry_harassment"),
                               key='statcrime_domestic', placeholder=None)
        op = st.radio(label="Choose the plots you want to Analyse", options=('Scatter', 'Heatmap'), index=None)
        if op == 'Scatter':
            if len(crime) == 2:
                st.write("If the regression coefficient is positive the line will be in upward direction otherwise downward")
                fig, ax = plt.subplots(figsize=(10, 8))
                plt.title("Regression Correlation between two variables")
                sb.regplot(data=df, x=crime[0], y=crime[1])
                st.pyplot(fig)
            else:
                st.info("Please choose exact two Crime Category")
        if op == "Heatmap":
            cor = df[crime].corr()
            fig, ax = plt.subplots()
            sb.heatmap(data=cor, cmap='Blues', ax=ax, annot=True)
            plt.title("Correlation between two variables")
            st.pyplot(fig)
