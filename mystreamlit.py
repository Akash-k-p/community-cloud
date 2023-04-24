import streamlit as st
import requests

URL1 = "https://hopethisworks.onrender.com/load"
URL2 = "https://hopethisworks.onrender.com/getjson"

st.write("running")
uploaded_file = None
# if st.button('Upload File'):
uploaded_file = st.file_uploader("Choose a image file", type=["png", "jpg", "jpeg", "gif"])
if uploaded_file is not None:
    file = uploaded_file.read()
    files = {'file': file}
    r1 = requests.post(url=URL1, files=files)
    # st.write(r1.json())
    r = requests.get(url=URL2).json()

    st.write("NAME :",r['name'])
    st.write("AADHAAR NUMBER :",r['aadhaar_no'])
    st.write("GENDER :",r['gender'])
    st.write("DOB :",r['dob'])
    st.write("ADDRESS :",r['address'])
    st.write("ENROLLMENT NO :",r['enrollment_no'])
    st.write("VID :",r['vid'])
    st.write("PHONE NUMBER :",r['phonenumber'])
    # st.write(r.)
    # print(type(file))

    st.write("------------------------------------------------------")
    st.write("UPLOAD SUCCESSFULL")

     #TODO able to upload front and back , both sides , and pdf files too

# print(type(uploaded_file))