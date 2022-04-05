from asyncore import write
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# 開始には streamlit run main.py

st.title('streamlit super rookie!!')

st.write('Dataframe')

df = pd.DataFrame(
    np.random.rand(100, 2) / [50,50] + [35.69, 139.70], # 20x3のランダム行列を作る
    columns = ['lat','lon']
)
st.map(df)
# st.line_chart(df)
# st.area_chart(df)

# st.write(df) #DFを出すときはWriteよりDataframeの方が優秀

# st.dataframe(df.style.highlight_max(axis = 0))

# st.table(df.style.highlight_max(axis = 0)) # スタティック（降順などの機能がない）な表を作れる

# markdown気泡を適用できる
""" 
# 章
## 節
### 項

``` python
import streeamlit as st
import numpy as np
import pandas as pd
```
"""

# `3つで囲むとコードが描ける 最初にpythonとか描いて言語を指定

left_column, right_column = st.columns(2)
button = left_column.button('left column text appeard!')
if button:
    right_column.write('💩')

expander = st.expander('Accsess')
expander.write('Accsess Address')

st.write('intaractiveなwidget')

if st.checkbox('Show image'):
    st.write('display image')
    img = Image.open('god.jpg')
    st.image(img, caption='god',use_column_width = True)

option = st.sidebar.selectbox(
    'Fav Num', list(range(1,11)), 
)



txt=st.sidebar.text_input('your fav phrase','💩')
cond = st.sidebar.slider('your condision', 0, 100, 0)

'your fav num is', option, '.'
'your fav num is', txt, '.'
'condition', cond, '.'


st.write('progress bar')

latest_iteration = st.empty() # iteration を先に設置
bar = st.progress(int(0))

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}') # iteration をに値を設定&For文で加算
    bar.progress(i + 1) # barの値を設定
    time.sleep(0.1)
