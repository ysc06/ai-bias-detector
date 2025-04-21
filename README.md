# 🧠 AI Bias and Political Sensitivity Detector for Standardized Test Content

This is a prototype AI-powered tool that detects biased or politically sensitive language in standardized test items. It flags sentences with potential fairness issues and suggests more neutral, inclusive rewrites.

## ✨ Key Features

- **Bias & Sensitivity Detection**: Identifies linguistic bias (e.g., gender, race, socioeconomic) and political sensitivity (e.g., tariffs, war, climate change).
- **Generative Rewriting**: Rewrites flagged sentences for neutrality and inclusiveness.
- **Structured Output**: Returns clear explanations in JSON format.
- **Agentic Reasoning**: Uses LangGraph logic to decide whether to rewrite or pass the item.
- **Interactive Web App**: Built with Streamlit for real-time user input and feedback.

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – for the frontend interface
- [Google Gemini](https://ai.google.dev) – for content evaluation and generation
- [LangGraph](https://github.com/langchain-ai/langgraph) – for agentic decision routing
- [LangChain](https://www.langchain.com/) – tool orchestration

## 🚀 How to Run Locally

1. **Clone this repo**

```bash
git clone https://github.com/ysc06/ai-bias-detector.git
cd ai-bias-detector

2. **Install dependencies
pip install -r requirements.txt

3. ** Add your API key

4. ** Run the app
streamlit run app.py

## Example Use Case
Input:
"Chinese merchandizes are becoming more expensive in the U.S. recently."

Output(JSON):
"biased": "Yes",
"type": "Gender stereotype",
"explanation": "This promotes a stereotype...",
"revised": "Caregiving skills are not determined by gender..."

## 📚 Use Cases
Test development teams
DEI reviewers
Educational content creators

## 🧩 To Do

Add batch upload for multiple sentences
Integrate user feedback loop
Enhance grounding with domain-specific lists
