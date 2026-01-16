import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 파일 이름 정의 (반드시 맨 위쪽에!)
file_name = '국토교통부_주택 공시가격 정보(2025)_샘플데이터.csv'

# 2. 한글 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.title("🏠 주택 공시가격 분석기")

try:
    # 3. 데이터 읽기 (정의된 file_name 사용)
    df = pd.read_csv(file_name, encoding='utf-8-sig')
    
    st.subheader("📍 시군구별 주택 분포")
    counts = df['시군구'].value_counts()
    
    # 4. 그래프 그리기
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=counts.index, y=counts.values, ax=ax, palette='viridis')
    
    # [핵심] 글자를 45도 회전하고 오른쪽 정렬해서 바르게 표시
    plt.xticks(rotation=45, ha='right', fontsize=12) 
    plt.title("시군구별 주택 수", fontsize=15)
    plt.tight_layout() # 글자가 잘리지 않게 조정
    
    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"❌ 파일을 찾을 수 없습니다: {file_name}")
except Exception as e:
    st.error(f"❌ 에러 발생: {e}")