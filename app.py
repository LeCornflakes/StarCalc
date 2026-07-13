import streamlit as st

st.set_page_config(
    page_title="StarCalc",
    layout="centered"
)

st.title("StarCalc")

if "display" not in st.session_state:
    st.session_state.display = ""

def add_number(number):
    st.session_state.display += str(number)

def add_operator(operator):
    st.session_state.display += operator

def clear():
    st.session_state.display = ""

def calculate():
    try:
        result = eval(st.session_state.display)
        st.session_state.display = str(result)

    except:
        st.session_state.display = "Error"

st.text_input(
    "Display",
    value=st.session_state.display,
    disabled=True
)

col1, col2, col3, col4 = st.collumns(4)

with col1:
    st.button("7", on_click=add_number, args=(7,))
    st.button("4", on_click=add_number, args=(4,))
    st.button("1", on_click=add_number, args=(1,))
    st.button("C", on_click=clear)

with col2:
    st.button("8", on_click=add_number, args=(8,))
    st.button("5", on_click=add_number, args=(5,))
    st.button("2", on_click=add_number, args=(2,))
    st.button("0", on_click=add_number, args=(0,))

with col3:
    st.button("9", on_click=add_number, args=(9,))
    st.button("6", on_click=add_number, args=(6,))
    st.button("3", on_click=add_number, args=(3,))
    st.button("=", on_click=calculate)

with col4:
    st.button("+", on_click=add_operator, args=("+",))
    st.button("-", on_click=add_operator, args=("-",))
    st.button("x", on_click=add_operator, args=("*",))
    st.button("÷", on_click=add_operator, args=("/",))