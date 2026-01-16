import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.set_page_config(page_title="주택 공시가격 분석", layout="wide")
st.title("🏠 2025 주택 공시가격 분석 및 통계표")

# 파일 이름 정의
file_name = '국토교통부_주택 공시가격 정보(2025)_샘플데이터.csv'

try:
    # 2. 데이터 로드
    df = pd.read_csv(file_name, encoding='utf-8-sig')
    
    # --- 상단 요약 통계표 ---
    st.subheader("📊 지역별 요약 통계표")
    
    # 시군구별로 주택수와 평균 공시가격을 계산합니다.
    summary_df = df.groupby('시군구').agg({
        '시군구': 'count',
        '공시가격': 'mean'
    }).rename(columns={'시군구': '주택 수(채)', '공시가격': '평균 공시가격(원)'})
    
    # 금액을 보기 좋게 콤마(,)가 포함된 숫자로 바꿉니다.
    summary_df['평균 공시가격(원)'] = summary_df['평균 공시가격(원)'].map('{:,.0f}'.format)
    
    # 화면에 표 출력
    st.table(summary_df)

    # --- 중간 가로 막대 그래프 ---
    st.divider()
    st.subheader("📍 지역별 주택 분포 (가로 그래프)")
    
    counts = df['시군구'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 가로형으로 그려서 글자가 똑바로 나오게 함
    sns.barplot(x=counts.values, y=counts.index, ax=ax, palette='viridis')
    plt.yticks(rotation=0, fontsize=12) # 지역명 글자 똑바로
    plt.xlabel("주택 수")
    st.pyplot(fig)

    # --- 하단 전체 데이터 표 ---
    st.divider()
    st.subheader("📋 전체 상세 데이터")
    # 검색이나 정렬이 가능한 데이터프레임 형식으로 출력
    st.dataframe(df, use_container_width=True)

except FileNotFoundError:
    st.error(f"❌ '{file_name}' 파일을 찾을 수 없습니다.")
except Exception as e:
    st.error(f"❌ 에러 발생: {e}")