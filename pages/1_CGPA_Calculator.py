import streamlit as st
from streamlit.hello.utils import show_code

st.title("CGPA calculator")
st.write("---")

# Create a slider widget with label, min, max, and default values
choice = st.number_input(label="How many courses did you take?: ", min_value=1, max_value=20, value=None, placeholder="Enter course count" )

# Display the selected value
st.write(f"You selected {choice} courses.")

if choice is not None and choice >= 1:
    for i in range(1, choice + 1):
        st.subheader(f"Course {i}:")
        ch_key = f"ch_c{i}"
        gp_key = f"gp_c{i}"
        ch_c = st.number_input(label="Credit Hour of this course: ", min_value=0, max_value=20, value=None, format="%d", placeholder="Enter your Credit Hour", key=ch_key)
        gp_c = st.number_input(label="Your Grade Point of this course: ", min_value=0.0, max_value=4.0, value=None, format="%.3f", placeholder="Enter your Grade Point", key=gp_key)

    calculate = st.button("Calculate")

    if calculate:
        TGP = 0
        TCH = 0

        for i in range(1, choice + 1):
            ch_key = f"ch_c{i}"
            gp_key = f"gp_c{i}"
            ch_c = st.session_state[ch_key]
            gp_c = st.session_state[gp_key]

            TGP += ch_c * gp_c
            TCH += ch_c

        CGPA = TGP / TCH

        st.write(f"\nTotal Credit of this semester: {TCH}")
        st.write(f"Your CGPA for this semester: {CGPA:.3f}\n")

st.write("---")
st.title("Extra")
st.markdown("""
I found out I can create a loop to iterate through the courses and create the input widgets dynamically  \nLoop made life easier (●'◡'●)  \nψ(｀∇´)ψ  finally I can sleeeeeeeeeeep
    """)

# Define your password and store it in your app secrets
password = st.secrets["password"]

# Create a text input widget that hides the user's input with asterisks
user_input = st.text_input(label=":red[Enter the password to see the code for] :orange[CGPA Calculator]", type="password")

# Compare the user's input with the password and display the code only if they match
if user_input == password:
    # Use st.markdown to display code with markdown formatting
    st.markdown("""
    ```python
    # This is a Python code block
import streamlit as st
from streamlit.hello.utils import show_code

st.title("CGPA calculator")
st.write("---")

# Create a slider widget with label, min, max, and default values
choice = st.slider(label="How many courses did you take? (1 to 13 courses): ", min_value=0, max_value=13, value=0)

# Display the selected value
st.write(f"You selected {choice} courses.")

if choice >= 1:
    for i in range(1, choice + 1):
        st.subheader(f"Course {i}:")
        ch_key = f"ch_c{i}"
        gp_key = f"gp_c{i}"
        ch_c = st.number_input(label="Credit Hour of this course: ", min_value=0, max_value=10, value=None, format="%d", placeholder="Enter your Credit Hour", key=ch_key)
        gp_c = st.number_input(label="Your Grade Point of this course: ", min_value=0.0, max_value=4.0, value=None, format="%.3f", placeholder="Enter your Grade Point", key=gp_key)

    calculate = st.button("Calculate")

    if calculate:
        TGP = 0
        TCH = 0

        for i in range(1, choice + 1):
            ch_key = f"ch_c{i}"
            gp_key = f"gp_c{i}"
            ch_c = st.session_state[ch_key]
            gp_c = st.session_state[gp_key]

            TGP += ch_c * gp_c
            TCH += ch_c

        CGPA = TGP / TCH

        st.write(f"\nTotal Credit of this semester: {TCH}")
        st.write(f"Your CGPA for this semester: {CGPA:.3f}\n")

    ```
    """)
else:
    # Display a message if the password is incorrect
    st.write(":blue[Ehehe, dm me for the pass~]")