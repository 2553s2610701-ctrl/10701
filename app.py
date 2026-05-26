`app.py`에는 이런 표시 없이 **코드만** 들어가야 합니다.

아래 코드를 그대로 복사해서 넣으면 정상 실행됩니다.

```python
import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="학급의 우정과 배려",
    page_icon="🤝",
    layout="centered"
)

# 제목
st.title("🤝 학급의 우정과 배려")
st.subheader("즐거운 교실 분위기를 위한 작은 프로그램")

# 설명
st.write("""
친절하고 배려하는 학급 분위기는 학생들이 서로를 존중하고,
함께 협력하며 즐겁게 학교생활을 할 수 있도록 도와줍니다.
""")

# 좋은 행동 목록
tips = [
    "😊 친구들에게 웃으며 인사하기",
    "🗣️ 다른 사람의 의견 존중하기",
    "🤝 어려운 친구 도와주기",
    "📚 모둠 활동에 적극 참여하기",
    "💬 상처 주는 말 하지 않기",
    "🎉 친구의 성공 함께 축하하기"
]

# 랜덤 조언 버튼
if st.button("좋은 행동 보기"):
    st.success(random.choice(tips))

# 설문조사
st.header("📊 우리 반 분위기 조사")

friendliness = st.slider(
    "우리 반은 얼마나 친절한가요?",
    1, 10, 5
)

st.write(f"현재 선택: {friendliness}/10")

# 의견 작성
message = st.text_area(
    "우리 반이 더 친해질 수 있는 방법을 적어보세요:"
)

if st.button("제출하기"):
    if message:
        st.balloons()
        st.success("좋은 의견 감사합니다!")
        st.write("💡 작성한 의견:", message)
    else:
        st.warning("의견을 입력해주세요.")

# 하단 문구
st.markdown("---")
st.caption("Streamlit으로 제작 ❤️")
