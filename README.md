# 🚀 AI Biography Analyzer & Trace Explorer
A specialized LLM application built with LangChain and Groq to perform deep biographical analysis. This project demonstrates professional LLMOps practices by integrating LangSmith for full execution tracing, performance monitoring, and prompt debugging.

# 🌟 Key Features
Structured Analysis: Automatically extracts summaries, interesting facts, achievements, and life stages from raw text.

Hybrid LLM Support: Seamlessly switch between cloud models (Groq/Llama 3) and local models (Ollama/Qwen) using LangChain Expression Language (LCEL).

Production-Grade Tracing: Integrated with LangSmith to monitor latency, token usage, and chain sequences in real-time.

Optimized Prompts: Uses decoupled PromptTemplate for better maintainability.

# 🛠️ Tech Stack
Framework: LangChain (LCEL)

Inference: Groq Cloud (Llama 3.1 8B)

Observability: LangSmith

Environment Management: python-dotenv & uv

# 📊 Observability with LangSmith
This project is fully instrumented with LangSmith. Every run tracks:

Input/Output: Detailed logs of the biographical raw data and the structured response.

Latency: Execution time for each component (Chain vs. Model).

Token Consumption: Precise count of prompt and completion tokens.

Snapshot: As seen in the traces, the RunnableSequence successfully processes complex historical data with clear visibility into the model's reasoning.

# 🚀 Getting Started
1. Prerequisites
Ensure you have Python installed (preferably using the uv package manager).

2. Environment Setup
Create a .env file in the root directory and add your credentials:

```bash
GROQ_API_KEY=your_groq_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT="AI-Bio-Analysis"
```
3. Installation & Usage

```bash
# Install dependencies
pip install langchain-core langchain-groq python-dotenv

# Run the analyzer
python main.py
```

# 📝 Example Output
The analyzer takes a raw biography (e.g., Sheikh Mohamed Bachir El Ibrahimi) and structures it into:

Summary: A concise overview of their historical impact.

Achievements: Key milestones like founding the Arab Academy of Damascus.

Life Chapters: Categorized professional and personal timelines.

Author: https://github.com/mohamedatr1/

Cybersecurity Researcher & Python Developer