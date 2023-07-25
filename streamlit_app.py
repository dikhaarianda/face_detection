import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np

FACE_CASCADE = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
EYE_CASCADE = cv2.CascadeClassifier('haarcascade_eye.xml')
SMILE_CASCADE = cv2.CascadeClassifier('haarcascade_smile.xml')

def main():
  """Face Detection APP"""
  st.title("Face Detection APP")
  st.text("Build with Streamlit and Open CV")

  activities = ["Home", "About"]
  choice = st.sidebar.selectbox("Select Activity", activities)

if __name__ == '__main__':
  main()