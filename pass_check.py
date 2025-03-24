import streamlit as st

st.markdown("**🔐Password check**")
st.write("Enter your password and check whether its weak, medium or strong.")

special_characters= "!@#$%^&*()-_=+;:'/.>,<`~?"
password_input= st.text_input("Enter Password")

strength= 0

if password_input:
    has_upper= any(char.isupper() for char in password_input)
    has_digit= any(char.isdigit() for char in password_input)
    has_special= any(char in special_characters for char in password_input)
    

    if has_upper:
        strength+=1
    else:
        st.write("⚠ Add a capital letter in your password")

    if has_digit:
        strength+=1
    else:
        st.write("⚠ Add a digit in your password")

    if has_special:
        strength+=1
    else:
        st.write("⚠ Add a special character in your password")        

    if strength== 0:
        st.write("❌Your password is **weak**")
    elif strength== 1:
        st.write("☑Your password **need improvement**")
    elif strength== 2:
        st.write("☑Your password is **medium**")  
    elif strength== 3:
        st.write("✅Your password is **strong**")    