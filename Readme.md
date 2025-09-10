# 🎯 Transcript Summarization with Prompt Engineering

This project demonstrates how to use Large Language Models (LLMs) for transcript summarization and **optimize prompt strategies** for accuracy and efficiency.  
The goal is to explore prompt engineering techniques to generate concise, high-quality summaries of transcripts.


## 🚀 Features
- Multiple prompt types: **Direct, Bullet Points, Role-Based, Optimized**
- Automatic evaluation of outputs:
  - Input vs. output length
  - Compression ratio
- Results saved to CSV for transparency
- Jupyter Notebook included for exploration


## 📂 Repository Structure
transcript-summarization-prompt-optimization/

│── README.md
│── requirements.txt
│── transcript_summarizer.py
│── data/
│── transcript_sample.txt
│── notebooks/
│── transcript_summarizer.ipynb
│── results/
│── results.csv

## 📊 Results

| prompt_type   | output                                                                                                   | input_words | output_words | compression_ratio |
|---------------|----------------------------------------------------------------------------------------------------------|-------------|--------------|-------------------|
| direct        | Q2 earnings grew 20% driven by new products, but costs rose due to supply chain issues.                  | 42          | 19           | 0.45              |
| bullet_points | - Revenue up 20% <br> - Driven by product launches <br> - Costs increased from supply chain issues        | 42          | 16           | 0.38              |
| role_based    | As a financial analyst: Q2 growth strong at 20%, though costs surged. Q3 outlook positive as logistics improve. | 42      | 22           | 0.52              |
| optimized     | Q2: +20% revenue from launches; costs rose on supply issues; Q3 margins expected to improve.             | 42          | 18           | 0.43              |


## Example block

### Example

**Transcript (input):**


Alice: Welcome everyone. Today we’ll review Q2 earnings.
Bob: Revenue increased by 20% year-over-year, driven by new product launches.
Carol: However, operational costs rose significantly due to supply chain issues.
Dave: Looking ahead, we expect stronger margins in Q3 as logistics stabilize.


**Optimized Prompt Summary (output):**  


Q2: +20% revenue from launches; costs rose on supply issues; Q3 margins expected to improve.

This shows the before and after effect at a glance.


## 🛠️ How to Run
```bash
# Clone repo
git clone https://github.com/your-username/transcript-summarization-prompt-optimization.git
cd transcript-summarization-prompt-optimization

# Install dependencies
pip install -r requirements.txt

# Run summarizer
python transcript_summarizer.py

