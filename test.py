import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title('Streamlit 超入門')

st.write('Display Image')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
   latest_iteration.text(f'Iteration{i + 1}')
   bar.progress(i + 1)
   time.sleep(0.01)

columns = st.columns(2)
button = columns[0].button('右カラムに表示')
if button:
    columns[1].write('カラムに表示されました')
    
    expander = st.expander('お問い合わせ')
    expander.write('問い合わせ内容')


#text = st.text_input('あなたの趣味を教えてください')
#'あなたの趣味：', text
#option = st.sidebar.selectbox('あなたの好きな数字を教えてください',
 #               list(range(1, 11))
  #              )
#'あなたの好きな数字は', option, 'です。'
#if st.checkbox('Show Image'):
 #   img = Image.open('sample01.jpg') 
  #  st.image(img,caption='arita', use_column_width=True)
#condition = st.slider('あなたの調子は？',0, 100, 60)
#'あなたの趣味：', condition
#df = pd.DataFrame(
 #   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],  
  #  columns=['lat', 'lon'])

#st.map(df) 