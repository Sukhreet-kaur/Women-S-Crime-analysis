import streamlit as st

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'notes' not in st.session_state:
    st.session_state.notes = []
if 'editing_note_index' not in st.session_state:
    st.session_state.editing_note_index = None

def login_page():
    st.title("Login")
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Email")
    with col2:
        password = st.text_input("Password", type="password")

    if st.button("Enter"):
        if email == "user@example.com" and password == "password":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials")

def home_page():
    st.title("📝 My Notes")

    if st.button("+ Add Note"):
        new_note = {'title': 'Untitled Note', 'content': ''}
        st.session_state.notes.append(new_note)
        st.rerun()

    if not st.session_state.notes:
        st.info("No notes yet. Click + to add one!")
    else:
        for i, note in enumerate(st.session_state.notes):
            col1, col2 = st.columns([4, 1])
            with col1:
                if st.button(note['title'] if note['title'] else 'Untitled Note', key=f"tile_{i}"):
                    st.session_state.editing_note_index = i
                    st.rerun()
            with col2:
                if st.button("❌", key=f"delete_{i}"):
                    del st.session_state.notes[i]
                    st.rerun()

    if st.session_state.editing_note_index is not None:
        edit_index = st.session_state.editing_note_index
        st.subheader("✏️ Edit Note")

        title = st.text_input("Title", value=st.session_state.notes[edit_index]['title'], key="edit_title")
        content = st.text_area("Content", value=st.session_state.notes[edit_index]['content'], key="edit_content", height=200)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save"):
                st.session_state.notes[edit_index]['title'] = title
                st.session_state.notes[edit_index]['content'] = content
                st.session_state.editing_note_index = None
                st.rerun()
        with col2:
            if st.button("Cancel"):
                st.session_state.editing_note_index = None
                st.rerun()

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.notes = []
        st.session_state.editing_note_index = None
        st.rerun()

if not st.session_state.logged_in:
    login_page()
else:
    home_page()
