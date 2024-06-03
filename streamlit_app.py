import streamlit as st
#from langchain.llms import OpenAI
#from langchain_community.llms import Ollama
import os
from query_data import query_rag


# 파일 업로드 함수
# 디렉토리 이름, 파일을 주면 해당 디렉토리에 파일을 저장해주는 함수
def save_uploaded_file(directory, file):
    # 1. 저장할 디렉토리(폴더) 있는지 확인
    #   없다면 디렉토리를 먼저 만든다.
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # 2. 디렉토리가 있으니, 파일 저장
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('파일 업로드 성공!')

st.set_page_config(page_title="🦜🔗 Quickstart RAG App")
st.title('🦜🔗 Quickstart RAG App')

pdf_file = st.sidebar.file_uploader('pdf 파일을 업로드 하세요.', type=['pdf'])
if pdf_file is not None: # 파일이 없는 경우는 실행 하지 않음
  print(type(pdf_file))
  print(pdf_file.name)
  print(pdf_file.size)
  print(pdf_file.type)

  save_uploaded_file('data', pdf_file)
#openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  st.info(query_rag(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', '인사 관련 질문을 해주세요!')
  submitted = st.form_submit_button('Submit')
  generate_response(text)
  

  #if not openai_api_key.startswith('sk-'):
   # st.warning('Please enter your OpenAI API key!', icon='⚠')
  #if submitted and openai_api_key.startswith('sk-'):
