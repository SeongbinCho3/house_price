import streamlit as st
import pandas as pd
import os

# 페이지 설정 (가장 먼저 실행되어야 함)
st.set_page_config(page_title="데이터 분석기", layout="wide")

st.title("🏠 주택 공시가격 분석기")

# 1. 현재 폴더에 어떤 파일들이 있는지 화면에 출력 (디버깅용)
st.subheader("📁 현재 서버 폴더 파일 목록")
files = os.listdir('.')
st.write(files)

# 2. 파일 읽기 시도
file_name = '국토교통부_주택 공시가격 정보(2025)_샘플데이터.csv'

if file_name in files:
    try:
        # 다양한 인코딩으로 시도 (흰 화면 방지)
        try:
            df = pd.read_csv(file_name, encoding='utf-8-sig')
        except:
            df = pd.read_csv(file_name, encoding='cp949')
            
        st.success(f"✅ '{file_name}' 데이터를 불러왔습니다!")
        st.write("### 📊 데이터 요약")
        st.dataframe(df.head())
        
        # 간단한 통계
        if '공시가격' in df.columns:
            st.write(f"**평균 공시가격:** {df['공시가격'].mean():,.0f} 원")
            st.bar_chart(df['시군구'].value_counts())
            
    except Exception as e:
        st.error(f"❌ 파일을 읽는 중 에러 발생: {e}")
else:
    st.error(f"❌ 파일을 찾을 수 없습니다: {file_name}")
    st.info("💡 깃허브에 CSV 파일이 제대로 올라갔는지 확인해 보세요!")