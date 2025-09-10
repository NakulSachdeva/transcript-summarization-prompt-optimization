# 📝 Transcript Summarization with Prompt Optimization

This project demonstrates how to **summarize meeting transcripts using LLMs** (Large Language Models) with different prompt engineering strategies.  
We compare approaches like **direct summaries, bullet points, role-based summaries, and optimized prompts** to evaluate how prompt design affects output.

---

## 🚀 Features
- Compare multiple prompt engineering strategies  
- Measure **compression ratios** (how much text is reduced)  
- Visualize results with charts  
- Easy-to-run notebook for experimentation  

---

## ⚙️ Setup

1. **Clone this repo**
   ```bash
   git clone https://github.com/your-username/transcript-summarization-prompt-optimization.git
   cd transcript-summarization-prompt-optimization
Install dependencies

pip install -r requirements.txt
Run the notebook

Open notebooks/transcript_summarizer.ipynb

Add your OPENAI_API_KEY in a .env file or environment variable

Execute cells to generate summaries and results

📊 Results
Tabular Comparison
prompt_type	output	input_words	output_words	compression_ratio
direct	Q2 earnings grew 20% driven by new products, but costs rose due to supply chain issues.	42	19	0.45
bullet_points	- Revenue up 20%
- Driven by product launches
- Costs increased from supply chain issues	42	16	0.38
role_based	As a financial analyst: Q2 growth strong at 20%, though costs surged. Q3 outlook positive as logistics improve.	42	22	0.52
optimized	Q2: +20% revenue from launches; costs rose on supply issues; Q3 margins expected to improve.	42	18	0.43

📊 Visual Insights
Compression Ratio by Prompt Type

<img width="1200" height="800" alt="compression_ratio" src="https://github.com/user-attachments/assets/8747b06c-e94f-4627-aa7a-3902cb7d8ddd" />

Input vs. Output Word Counts

<img width="1200" height="800" alt="word_counts" src="https://github.com/user-attachments/assets/c9908a90-94a7-4397-b6b6-58d603ab5ec8" />

🔍 Example
Transcript (input):

Alice: Welcome everyone. Today we’ll review Q2 earnings.  
Bob: Revenue increased by 20% year-over-year, driven by new product launches.  
Carol: However, operational costs rose significantly due to supply chain issues.  
Dave: Looking ahead, we expect stronger margins in Q3 as logistics stabilize.  

Optimized Prompt Summary (output):

Q2: +20% revenue from launches; costs rose on supply issues; Q3 margins expected to improve.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.
