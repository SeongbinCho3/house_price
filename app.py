import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.title("🏠 2025 주택 공시가격 분석기")

# 2. 파일 이름 (내 컴퓨터에 있는 실제 파일명과 똑같아야 함)
file_name = '국토교통부_주택 공시가격 정보(2025)_샘플데이터.csv'

try:
    # 3. 데이터 읽기
    df = pd.read_csv(file_name, encoding='utf-8-sig')
    st.success("✅ 데이터를 성공적으로 불러왔습니다!")

    # 4. 가로 막대 그래프 그리기 (글자 안 겹치게)
    st.subheader("📍 지역별 주택 분포")
    counts = df['시군구'].value_counts()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(x=counts.values, y=counts.index, ax=ax, palette='viridis')
    
    plt.title("시군구별 주택 수", fontsize=15)
    plt.xlabel("주택 수 (채)")
    plt.ylabel("지역명")
    
    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"❌ 파일을 찾을 수 없습니다: {file_name}")
    st.info("💡 CSV 파일이 app.py와 같은 폴더에 있는지 확인해주세요.")
except Exception as e:
    st.error(f"❌ 에러가 발생했습니다: {e}")