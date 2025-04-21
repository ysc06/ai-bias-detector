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

2. **Install dependencies**
pip install -r requirements.txt

3. ** Add your API key**

4. ** Run the app**
streamlit run app.py

## Example Use Case
Input:
"Recently, I found Chinese merchandizes have become expensive than before."

Output(JSON):
    "biased": "Yes",

    "type": "Political sensitivity, Socioeconomic bias, Potential cultural bias",

    "explanation": "This sentence exhibits several potential biases.  Firstly, it touches upon the sensitive area of U.S.-China relations, particularly concerning trade and economics. The phrasing 'Chinese merchandizes' could be interpreted as a generalization about all goods originating from China, potentially contributing to negative stereotypes about Chinese products or manufacturing practices.  Secondly, the statement implies a socioeconomic impact – the increased cost of goods affects consumers differently based on their income levels.  Higher prices disproportionately impact low-income individuals and families. Finally, the term 'merchandizes' might be perceived differently across cultures, potentially containing a subtle cultural bias if it is associated with a negative connotation in some cultural contexts.  While not explicitly stated, this sentence could inadvertently contribute to existing negative narratives surrounding China and potentially harmful stereotypes.",

    "Rewritten (if biased): The cost of goods from China has increased recentl

## 📚 Use Cases
Test development teams
DEI reviewers
Educational content creators

## 🧩 To Do

Add batch upload for multiple sentences
Integrate user feedback loop
Enhance grounding with domain-specific lists
