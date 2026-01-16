import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. 파일 이름 정의 (이게 그래프 코드보다 먼저 와야 합니다!) ---
file_name = '국토교통부_주택 공시가격 정보(2025)_샘플데이터.csv'

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.title("🏠 주택 공시가격 분석기")

try:
    # --- 2. 데이터 읽기 ---
    df = pd.read_csv(file_name, encoding='utf-8-sig')
    
    # --- 3. 그래프 그리기 (시군구 글자 바르게 설정) ---
    st.subheader("📍 시군구별 주택 분포")
    
    counts = df['시군구'].value_counts()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=counts.index, y=counts.values, ax=ax, palette='viridis')
    
    # [핵심] 글자를 바르게(45도 회전) 표시하여 겹침 방지
    plt.xticks(rotation=45, ha='right', fontsize=12) 
    plt.title("시군구별 주택 수", fontsize=15)
    
    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"❌ 파일을 찾을 수 없습니다: {file_name}")