#%%writefile app3.py
import streamlit as st
import cv2
import pytesseract
from PIL import Image   #Python Imaging Library to open the images in streamlit because streamlit doesn't images to display directly

pytesseract.pytesseract.tesseract_cmd='/app/.apt/usr/bin/tesseract'   #for heroku setup
st.set_option('deprecation.showfileUploaderEncoding',False)           #this line ignores any warning that comes up
st.title("OCR - Optical Character Recognition")                       #title for the web app
st.text("Upload the image")                                           #asking user to upload the image

uploaded_file = st.sidebar.file_uploader("Choose as image ",type = ["jpg","jpeg","png"])  #create a file upload
if uploaded_file is not None:     #only if a file is uploaded, then perform the below operations
  img=Image.open(uploaded_file)   #open the uploaded file
  st.image(img, caption='Upload Image', use_column_width=True)
  st.write("")      #prints a blank space

  if st.button('PREDICT'): # creates a button called predict and gives the OCR output below
    st.write("Result: ")
    info = pytesseract.image_to_string(img)
    st.title(info)          #prints the result
