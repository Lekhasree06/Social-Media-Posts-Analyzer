
import streamlit as st
from prompt import get_prompt
from model import get_gemini_response
from parser import parse_response


st.set_page_config(
    page_title="Social Media Post Analyzer",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Social Media Post Analyzer")
st.write("Analyze the tone, intent, communication style, and summary of a social media post using Gemini AI.")

post_text = st.text_area(
    "Enter your social media post:",
    height=180,
    placeholder="Example: We are excited to launch our new AI-powered learning platform next week. Stay tuned for more updates!"
)

analyze_button = st.button("Analyze Post")

if analyze_button:
    if not post_text.strip():
        st.warning("Please enter a social media post.")
    else:
        with st.spinner("Analyzing post..."):
            try:
                prompt = get_prompt(post_text)
                raw_response = get_gemini_response(prompt)
                parsed_output = parse_response(raw_response)

                if "error" in parsed_output:
                    st.error(parsed_output["error"])
                    st.write(parsed_output)
                else:
                    st.success("Analysis completed!")

                    st.subheader("Structured Output")
                    st.json(parsed_output)

                    st.subheader("Result Breakdown")
                    st.write(f"**Tone:** {parsed_output['tone']}")
                    st.write(f"**Intent:** {parsed_output['intent']}")
                    st.write(f"**Communication Style:** {parsed_output['communication_style']}")
                    st.write(f"**Summary:** {parsed_output['summary']}")

            except Exception as e:
                st.error("Something went wrong.")
                st.write(str(e))
