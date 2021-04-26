import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")
st.write("プログレスバーの表示")
"Start"

#barの上にlatest_iterationのtextが表示される
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    #progressでバーが伸びる
    bar.progress(i + 1)
    time.sleep(0.01)
"Done!!!!"

left_column, right_column = st.beta_columns(2)#引数はカラム数
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ1の回答")
expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ2の回答")
expander3 = st.beta_expander("問い合わせ3")
expander3.write("問い合わせ3の回答")
# text = st.text_input("あなたの趣味を教えてください")
# #slider(テキスト, start, stop, default)
# condition = st.slider("あなたの今の調子は?", 0, 100, 50)

# "あなたの趣味:", text, "です"
# "コンディション:", condition


# if st.checkbox("Shouw Image"):
#     img = Image.open("suiren_edited.jpg")
#     #use_column_width=Trueで画面の横幅に合わせて表示させる
#     st.image(img, caption="Suiren", use_column_width=True)
