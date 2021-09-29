import streamlit as st
from gtts import gTTS

st.title("Text to Speech Convertor")

#Adding a selectbox for voice selection
voices = ["English-UK","English-IN","English-US"]
voice = st.sidebar.selectbox("Select Voice", voices)

if voice == "English-UK":
    language = 'en'
    tld_lang = 'co.uk'
elif voice == "English-IN":
    language = 'en'
    tld_lang = 'co.in'
elif voice == "English-US":
    language = 'en'
    tld_lang = 'com'

#Adding radio for speed
rad = st.sidebar.radio("Select the speed of the speech",("Fast","Slow"))

if rad == "Slow":
    speed = True
else:
    speed = False


uploaded_file = st.file_uploader("Add text file")

if uploaded_file is not None:
    #Asking the file name from user
    fileName = st.text_input("Enter the name of the output file", "Type Here")

    raw_text = str(uploaded_file.read(),"utf-8")
    st.write(raw_text)

    output = gTTS(text = raw_text, lang = language, tld=tld_lang, slow = speed)
    output.save(fileName)


    audio_file = open(fileName, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg',start_time=0)
