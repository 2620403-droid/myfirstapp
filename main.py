Skip to content
2620403-droid
myfirstapp
Repository navigation
Code
Issues
Pull requests
Actions
Projects
Wiki
Security and quality
Insights
Settings
Files
Go to file
t
T
README.md
main.py
myfirstapp
/
main.py
in
main

Edit

Preview
Indent mode

Spaces
Indent size

4
Line wrap mode

No wrap
Editing main.py file contents
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
import streamlit as st
import random
import urllib.parse


st.set_page_config(
    page_title="MBTI POP PICK",
    page_icon="☕",
    layout="centered"
)


# 디자인
st.markdown("""
<style>

body {
    background:#fff4fa;
}

.title {
    text-align:center;
    font-size:48px;
    font-weight:900;
    color:#ff4f91;
}

.subtitle {
    text-align:center;
    color:#777;
    font-size:18px;
}

.card {
    background:white;
    padding:35px;
Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
 
