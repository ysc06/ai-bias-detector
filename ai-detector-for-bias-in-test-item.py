import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from langgraph.graph import StateGraph, END
from langchain_core.tools import tool
#Google API
!pip install -U google-generativeai
import google.generativeai as genai
genai.configure(api_key=st.secrets["api"]["YOUR API KEY"])  

model = genai.GenerativeModel(model_name = "models/gemini-1.5-flash-latest")

import streamlit as st

st.title("AI Detector for Bias and Politically Sensitivity in Test Content")

user_input = st.text_area("Enter your text:")
if st.button("Analyze"):
    output = graph.invoke({"text_1": user_input, "text_2": ""})
    st.subheader("🧠 Classification")
    st.json(output.get("result"))
    st.subheader("✍️ Revised")
    st.write(output.get("revised", "N/A"))



@tool
def classify_bias(text_1: str, text_2: str) -> dict:
    """
    Classifies one or two input sentences for bias or political sensitivity using Gemini.
    """

    if text_2.strip():
        # If both inputs are given
        prompt = f"""
You are a fairness evaluator reviewing test content for bias and political sensitivity in 2025.

Evaluate the following two sentences. Be especially sensitive to:
- Stereotypes bias (e.g., about gender, race, age)
- Political sensitivity (e.g., immigration, U.S.–China tensions)
- Socioeconomic bias (e.g., parental support, neighborhood quality)
- Cultural bias (e.g., East vs. West education)
- Language that may be interpreted differently by marginalized groups

Return a structured JSON response like this:

{{
  "text_1": {{
    "biased": "Yes/No",
    "type": "...",
    "explanation": "...",
    "confidence": 0.0–1.0
  }},
  "text_2": {{
    "biased": "Yes/No",
    "type": "...",
    "explanation": "...",
    "confidence": 0.0–1.0
  }}
}}

Text 1: {text_1}

Text 2: {text_2}
"""
    else:
        # If only text_1 is provided
        prompt = f"""
You are a fairness evaluator reviewing test content for bias and political sensitivity in 2025.

Evaluate the following sentence. Be especially sensitive to:
- Stereotypes bias (e.g., about gender, race, age)
- Political sensitivity (e.g., immigration, U.S.–China tensions)
- Socioeconomic bias (e.g., parental support, neighborhood quality)
- Cultural bias (e.g., East vs. West education)
- Language that may be interpreted differently by marginalized groups

Return a structured JSON response like this:

{{
  "text_1": {{
    "biased": "Yes/No",
    "type": "...",
    "explanation": "...",
    "confidence": 0.0–1.0
  }}
}}

Text 1: {text_1}
"""

    try:
        response = model.generate_content(prompt)
        return {
            "text_1": text_1,
            "text_2": text_2,
            "result": response.text
        }

    except Exception as e:
        return {
            "text_1": text_1,
            "text_2": text_2,
            "result": f"error: {str(e)}"
        }


# Agent will route to only if bias is dected

@tool
def generate_rewrite_prompt(text_1: str, text_2: str, result: str) -> dict:
    """
    Rewrites one or two input sentences to be neutral and inclusive for educational testing.
    """

    if text_2.strip():
        prompt = f"""
Rewrite the following two statements to be neutral and inclusive for educational testing.

Text 1: {text_1}
Text 2: {text_2}

Return both rewritten sentences in plain text.
"""
    else:
        prompt = f"""
Rewrite the following statement to be neutral and inclusive for educational testing.

Text 1: {text_1}

Return the rewritten sentence in plain text.
"""

    try:
        response = model.generate_content(prompt)
        return {
            "text_1": text_1,
            "text_2": text_2,
            "result": result,
            "revised": response.text
        }

    except Exception as e:
        return {
            "text_1": text_1,
            "text_2": text_2,
            "result": result,
            "revised": f"error: {str(e)}"
        }





