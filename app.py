import streamlit as st

# Page Settings
st.set_page_config(page_title="Module Grade Calculator", page_icon="📊")

# Light Brown Background
st.markdown("""
<style>
.stApp {
    background-color: #D2B48C;
}
h1 {
    text-align: center;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Grade Calculator")

# Student Details
name = st.text_input("Enter Your Name")
mother_name = st.text_input("Enter Mother's Name")
seat_no = st.text_input("Enter Seat Number")

st.subheader("Enter Module Marks")

m1 = st.number_input("Module 1 Marks", 0, 100)
m2 = st.number_input("Module 2 Marks", 0, 100)
m3 = st.number_input("Module 3 Marks", 0, 100)
m4 = st.number_input("Module 4 Marks", 0, 100)
m5 = st.number_input("Module 5 Marks", 0, 100)

if st.button("Calculate Grade"):

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    st.success("Result Generated Successfully")

    st.write("### Student Details")
    st.write("Name:", name)
    st.write("Mother's Name:", mother_name)
    st.write("Seat Number:", seat_no)

    st.write("### Result")
    st.write("Total Marks:", total)
    st.write(f"Percentage: {percentage:.2f}%")
    st.write("Grade:", grade)
