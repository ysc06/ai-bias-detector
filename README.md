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
