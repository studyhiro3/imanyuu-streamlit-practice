import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 入門")

st.write("DataFrame")

df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [10, 20, 30, 40]
})

st.write("st.writeを使用したとき")
st.write(df)


# dataframeだとwidthとheightの引数できるのはdataframe, writeは引数できない。
st.write("st.dataframeを使用したとき")
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

# staticな表を表示させたいときはtable
st.write("st.tableを使用したとき")
st.table(df)

# マークダウンとpythonコードの表記方法(マジックコマンド)
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"]
)

# API reference - Display chartsに詳細あり
st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)

# mapをプロット
# 渋谷あたりの座標情報を作成
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]
)

st.map(df)

# イメージを作成
# API reference - Display mediaに詳細あり
st.write("Interactive Widgets")

img = Image.open("kata_sakana.png")
st.image(img, caption="Kohei Imanishi", use_column_width=True)

# チェックボックスを用いて画像の表示/非表示を決める
if st.checkbox("Show Image"):
    img = Image.open("kata_sakana.png")
    st.image(img, caption="Kohei Imanishi", use_column_width=True)

# セレクトボックスの作成
option = st.selectbox(
    "あなたが好きな数字を教えて下さい。",
    list(range(1, 11))
)
# st.writeをしようしなくても記載できる。
"あなたの好きな数字は、", option, "です。"

# # テキスト入力
# text = st.text_input("あなたの趣味を教えて下さい。")
# "あなたの趣味：", text, "です"

# # スライダー
# condition = st.slider("あなたの今の調子は？", 0, 100, 50)
# "コンディション：", condition

# レイアウトを整える

# サイドバー
# テキスト入力
# text = st.sidebar.text_input("あなたの趣味を教えて下さい。")
# "あなたの趣味：", text, "です"

# # スライダー
# condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
# "コンディション：", condition

# 2カラムにする方法
left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

# エクスパンダー
expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")

expander1 = st.expander("問い合わせ")
expander1.write("問い合わせ1の回答")
expander2 = st.expander("問い合わせ")
expander2.write("問い合わせ2の回答")
expander3 = st.expander("問い合わせ")
expander3.write("問い合わせ3の回答")

# プログレスバー
st.write("プログレスバーの表示")
"Start!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)
