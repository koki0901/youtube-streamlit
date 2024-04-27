import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time
 
st.title('Streamlit 入門')

# st.write('DataFrame')
# st.write('Dispaly Image')
# st.write('Interactive Widgets')
st.write('プログレスバーの表示')
'Start!!'

# option=st.selectbox(
#   'あなたが好きな数字を教えてください',
#   list(range(1,11))
# )

# サイドバー
# text=st.sidebar.text_input(
#   'あなたの趣味を教えてください',
# )
# 'あなたの趣味は、',text, 'です。'

# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
# 'コンディション：',condition

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.05)

'Done!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')


# if st.checkbox('Show Image'):
#   img = Image.open('MYPROTEIN - フレーバーレビュー｜りんご編.png')
#   st.image(img, caption='りんご', use_column_width=True)

# df = pd.DataFrame(
#   np.random.rand(20, 3),
#   columns=['a', 'b', 'c']
# )

# df = pd.DataFrame(
#   np.random.rand(100, 2)/[50, 50] + [35.69,139.70],
#   columns=['lat', 'lon']
# )

# st.map(df)

#折れ線グラフ
# st.line_chart(df)
# st.area_chart(df)
#棒グラフ
# st.bar_chart(df)

# df = pd.DataFrame({
#   '1列目':[1,2,3,4],
#   '2列目':[10,20,30,40]
# })

# インタラクティブなテーブル
# st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)

# 静的なテーブル
# st.table(df.style.highlight_max(axis=0))

# マークダウン
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

