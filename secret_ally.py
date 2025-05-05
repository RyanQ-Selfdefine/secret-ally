
import streamlit as st
import openai

# 设置页面和背景风格
st.set_page_config(page_title="神秘盟友 · Secret Ally", layout="centered")
st.markdown("""
<style>
html, body, .stApp {
    background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
    font-family: 'Segoe UI', sans-serif;
}
.response-box {
    background-color: rgba(255,255,255,0.85);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🤝 神秘盟友 · Secret Ally")
st.markdown("#### 把你此刻的感受告诉我，我会以盟友的身份回应你。")

# 输入 OpenAI API key（建议你运行时手动输入）
api_key = st.text_input("🔑 输入你的 OpenAI API Key（我们不会保存它）", type="password")

user_input = st.text_area("🗣️ 你现在的感受或烦恼是？", placeholder="比如：我最近总觉得自己不够好...")
language = st.radio("语言 Language", ["中文", "English"], horizontal=True)

if st.button("✨ 听听神秘盟友的回应"):
    if not api_key:
        st.error("请填写 API Key")
    elif not user_input.strip():
        st.error("请输入一些内容")
    else:
        with st.spinner("神秘盟友正在聆听你..."):
            openai.api_key = api_key

            system_prompt = {
                "中文": "你是一位温柔、深思、有智慧的神秘盟友。用温暖、肯定、真挚的语气，回应朋友的情绪，帮助他看到自己内在的价值，避免说教。",
                "English": "You are a thoughtful and gentle secret ally. Respond warmly and sincerely, affirming the user's feelings, and gently helping them see their worth without sounding preachy."
            }

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": system_prompt[language]},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.9
                )
                reply = response['choices'][0]['message']['content']
                st.markdown(f"<div class='response-box'>{reply}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"出错了：{e}")
