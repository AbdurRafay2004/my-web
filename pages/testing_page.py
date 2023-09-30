import streamlit as st
from streamlit.hello.utils import show_code

st.write(":orange[wiill be testing out experimental codes in this page] (～￣▽￣)～")


# Define your password and store it in your app secrets
password = st.secrets["password"]

# Create a text input widget that hides the user's input with asterisks
user_input = st.text_input(label="Enter the password to see the code", type="password")

# Compare the user's input with the password and display the code only if they match
if user_input == password:
    # Use st.markdown to display code with markdown formatting
    st.markdown("""
    ```python
    # This is a Python code block
    def hello():
        print("Hello, Streamlit!")
    ```
    """)
else:
    # Display a message if the password is incorrect
    st.write(":blue[Ehehe, dm me for the pass~]")
