import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 파일 이름 정의 (이름이 아래와 정확히 같아야 빨간 줄이 안 생깁니다)
target_file = '국토교통부_주택 공시가격 정보(2025)_샘플데이터.csv'

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.title("🏠 주택 공시가격 분석 (가로 그래프 버전)")

try:
    # 2. 데이터 읽기
    df = pd.read_csv(target_file, encoding='utf-8-sig')
    
    st.subheader("📍 시군구별 주택 분포 (글자 똑바로 보기)")

    # 데이터 개수 세기
    counts = df['시군구'].value_counts()

    # 3. 그래프 그리기 (가로 막대 그래프)
    # figsize에서 세로(8)를 조금 더 길게 주면 글자 간격이 넓어져서 더 잘 보입니다.
    fig, ax = plt.subplots(figsize=(10, 8)) 
    
    # x와 y를 바꿔주면 가로 그래프가 됩니다!
    # x에 숫자(values), y에 이름(index)을 넣으세요.
    sns.barplot(x=counts.values, y=counts.index, ax=ax, palette='viridis')

    # 그래프 꾸미기
    plt.title("시군구별 주택 수", fontsize=15)
    plt.xlabel("주택 수 (채)")
    plt.ylabel("지역명")
    
    # 이 설정은 글자를 기울이지 않고 똑바로(0도) 둡니다.
    plt.yticks(rotation=0, fontsize=12) 
    
    plt.tight_layout() # 그래프 요소들이 겹치지 않게 자동 조정
    st.pyplot(fig)

    # 4. 데이터 표
    st.divider()
    st.dataframe(df.head())

except FileNotFoundError:
    st.error(f"❌ 파일을 찾을 수 없습니다: {target_file}")
except Exception as e:
    st.error(f"❌ 에러 발생: {e}")