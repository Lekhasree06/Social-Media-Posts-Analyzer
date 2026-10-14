
def get_prompt(post_text: str) -> str:
    prompt = f"""
You are a Social Media Post Analyzer.

Your task is to analyze the given social media post and classify it using only the provided text.

Return the output strictly in valid JSON format with the following keys:
- tone
- intent
- communication_style
- summary

Rules:
1. Do not include markdown.
2. Do not include explanations outside JSON.
3. Do not assume information not present in the post.
4. Keep the summary short and clear.
5. The output must be valid JSON.

Social Media Post:
\"\"\"{post_text}\"\"\"

Expected JSON format:
{{
  "tone": "string",
  "intent": "string",
  "communication_style": "string",
  "summary": "string"
}}
"""
    return prompt
