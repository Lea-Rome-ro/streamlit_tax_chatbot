# 가상환경이 아닌 global 환경의 python으로 실행될때는 
# 'Cmd + Shift + P'를 눌러 명령 팔레트를 켜고
# "Python: Select Interpreter"를 선택하여 가상환경의 python을 선택하면 됨
import streamlit as st

from llm import get_ai_response 
from dotenv import load_dotenv

st.set_page_config(page_title="소득세 chatbot", page_icon="🤖")

st.title("🤖 소득세 chatbot")
st.caption("소득세 관련된 모든것을 답해드립니다!")

load_dotenv()

# 입력값이 들어올때마다 페이지가 새로 로딩되기 때문에 입력값을 저장해야 함
# 이때 저장할 수 있도록 하는것이 Seession State 이다.
if 'message_list' not in st.session_state:
    st.session_state.message_list = []

# 메세지를 화면에 표시
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 메세지 받으면 message_list에 추가하고 AI 대답하기
if user_question:= st.chat_input(placeholder="소득세에 관련된 궁금한 내용들을 말씀해주세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("AI가 답변을 작성중입니다..."):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
        st.session_state.message_list.append({"role": "ai", "content": ai_message})

