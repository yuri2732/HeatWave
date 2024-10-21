#데이터 로드 및 전처리
import sklearn
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 데이터 업로드
uploaded_file_1 = st.file_uploader("연월별 폭염일수", type="xls")

# Streamlit 앱 제목
st.title("연월별 폭염일수")

# Excel 파일 읽기
df = pd.read_excel(uploaded_file_1)  # 첫 번째 시트 읽기

# 데이터 표시
st.write("데이터 프레임:")
st.dataframe(df)

# 그래프 그리기
st.subheader("데이터 그래프")

plt.figure(figsize=(10, 5))
plt.plot(df['x'], df['y'], marker='o')
plt.title('X vs Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
st.pyplot(plt)