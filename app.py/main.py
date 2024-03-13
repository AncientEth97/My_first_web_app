from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
# Find more emojis here https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieur1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html= True)

local_css("style/style.css")


# --- LOAD ASSETS ---
lottie_coding = load_lottieur1("https://lottie.host/b9a95161-1b06-47e3-a13f-c8ebbf6f6889/5z5nIaXbjB.json")
img_contact_form = Image.open("images/Professional_image.png")


# ---- HEADER SECTION ----
st.subheader("Hi, my name is Ethan Giovanni Herold :wave:")
st.title("I am an AWS solution architect from South Africa")
st.write("I am passionate about cloud technology and Python coding. I strive to architect the best AWS cloud solutions")
st.write("[Please see my LinkedIn page >](https://www.linkedin.com/in/ethan-herold-659542163/details/experience/")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header(" What I do")
        st.write("##")
        st.write(
            """
            I work on various AWS Architectures, ensuring that the architectures follow AWS best practices. This is done by conducting AWS Well Architected Reviews. I also enjoy creating carious projects using Python.
            
            My likes include:
            
            -Watching movies (my favorite movie is Pulp Fiction)
            
            -Playing video games (my favorite game is Mass Effect)
            
            -Coding various applications
            
            -Spending time with my beautiful wife Kasia
            
            -Learning new things everyday
            """
        )
        st.write("[View my AWS Academic transcript >](https://reliancecloudcoza-my.sharepoint.com/:b:/g/personal/ethanh_reliancecloud_co_za/EdKIAbEFCXFDiFLEzqhdMzMB9Gu_KlNexujYpNmBEJ2pMA?e=OCPd0l")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# --- AWS Badges Images ---
with st.container():
    st.write("---")
    st.header("My AWS Certified badges")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    st.image(img_contact_form)
    with text_column:
        st.subheader("AWS Certified Solutions Architect Professional")
        st.write(
            """
            This is my certified Solutions Architect Professional badge issued by AWS.
            This exam tests your understanding of AWS services in depth, requiring a deep understanding of AWS services in order to pass.
            """
        )
# --- CONTACT FORM---
with st.container():
    st.write("---")
    st.header("Get in Touch with me!")
    st.write("##")

# Documentation: Form submit. Change email address
contact_form = """
<form action="https://formsubmit.co/ancientthane@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email"placeholder="Your email" required>
     <textarea name="message"placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html= True)
    with right_column:
        st.empty()

