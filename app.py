import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.title("🏠 주택 공시가격 분석 (최종 확인 버전)")

# 1. 파일 이름 확인 (공백이나 괄호 주의!)
file_name = '국토교통부_주택 공시가격 정보(2025)_샘플데이터.csv'

st.write(f"🔍 '{file_name}' 파일을 찾는 중...")

try:
    # 2. 데이터 불러오기 (utf-8 시도)
    # 한국 공공데이터는 utf-8 또는 utf-8-sig가 많습니다.
    df = pd.read_csv(file_name, encoding='utf-8')
    
    st.success("✅ 데이터를 성공적으로 불러왔습니다!")
    
    # 데이터 요약 정보 출력
    st.subheader("📋 데이터 미리보기")
    st.dataframe(df.head())

    # 3. 간단한 그래프 그리기
    st.divider()
    st.subheader("📊 지역별 데이터 분포")
    
    if '시군구' in df.columns:
        counts = df['시군구'].value_counts()
        st.bar_chart(counts)
    else:
        st.warning("'시군구' 컬럼을 찾을 수 없습니다. 컬럼명을 확인하세요.")

except FileNotFoundError:
    st.error(f"❌ 파일을 찾을 수 없습니다. 파일명이 '{file_name}' 인지 확인하세요.")
    st.info("팁: 깃허브 데스크탑에서 CSV 파일도 함께 Push 했는지 확인해 보세요!")
    
except Exception as e:
    # 어떤 에러인지 화면에 직접 뿌려줍니다.
    st.error(f"❌ 실행 중 에러가 발생했습니다: {e}")
    st.write("상세 에러 내용:", e)