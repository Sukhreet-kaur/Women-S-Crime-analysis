    r = df.groupby(op)[crime].sum().reset_index()
                if op == 'year':
                    fig, ax = plt.subplots(figsize=(10, 8))
                    r = df.groupby('year')[crime].sum().reset_index()
                    sb.barplot(data=r, y=crime, x=op, color="skyblue", hue=crime, ax=ax)
                else:
                    fig, ax = plt.subplots(figsize=(15, 15))
                    sb.barplot(data=r, x=crime, y=op, color="darksalmon", hue=crime, ax=ax)
                st.pyplot(fig)
