
# 🤖 Smart Marketing Assistant (CrewAI + OpenRouter)

### 🧠 AI-Powered Marketing Strategy Generator with Built-in Evaluation Metrics

This project uses **CrewAI** to orchestrate multiple autonomous marketing agents — each with a specific expertise — to **research**, **plan**, and **optimize** marketing campaigns.  
It integrates **OpenRouter LLMs** and **Serper Search API** for real-world insights, and includes **automatic evaluation** (BLEU, Truthfulness, Perplexity) to assess quality.

---

## 🚀 Why You’ll Love This Project

✅ Runs on **free OpenRouter models** — no paid API keys required for basic use.  
✅ Modular, clean design: **agents**, **tasks**, **crew**, **evaluation**, **CLI runner**.  
✅ Built-in feedback loop with **quantitative metrics** like BLEU and Truthfulness.  
✅ Ready for **extension** (add agents, tools, or metrics easily).  

---
## 🧩 Project Architecture

```

smart_marketing_assistant/
│
├── agents.py                # Defines AI agents and their roles
├── tasks.py                 # Specifies the marketing tasks
├── crew.py                  # Builds and orchestrates the Crew workflow
├── main.py                  # CLI runner (entry point)
├── evaluation_matrix.py     # BLEU, Perplexity, and Truthfulness metrics
├── reference_strategy.txt   # Reference text for BLEU comparison
├── .env                     # Environment variables (NOT uploaded)
├── requirements.txt         # Dependencies list
└── README.md                # This file

````

---

## ⚙️ Setup Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<yourusername>/Smart-Marketing-Assistant-CrewAI.git
cd Smart-Marketing-Assistant-CrewAI
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
# Activate it:
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
pip install evaluate
```

### 4️⃣ Add Your `.env` File (Do NOT Upload It!)

Create a `.env` file in the root folder and add:

```bash
OPENROUTER_API_KEY=your_openrouter_key_here
SERPER_API_KEY=your_serper_key_here
CREWAI_TRACING_ENABLED=true
```

### 🧱 Example `.gitignore`

```
# Python
__pycache__/
.venv/

# Environment
.env
```

---

## 🧠 How It Works

| Phase               | Agent                   | Task                | Description                                   |
| ------------------- | ----------------------- | ------------------- | --------------------------------------------- |
| 🕵️‍♀️ **Research** | Market Research Analyst | `research_task`     | Studies competitors, audience, and trends     |
| 🎨 **Strategy**     | Campaign Strategist     | `strategy_task`     | Creates creative plan, audience & channel mix |
| 📈 **Optimization** | Performance Analyst     | `optimization_task` | Evaluates plan, proposes KPIs, and tracking   |

The **crew runs sequentially** → insights flow from one agent to the next.
Finally, results are cleaned and evaluated for coherence, similarity, and truthfulness.

---

## 💡 Example Run

```bash
python -m main
```

**CLI Prompt:**

```
Enter your product or campaign focus: Sustainable clothing brand targeting Gen Z
```

**Output Example:**

```
🤖 Launching Smart Marketing Assistant Crew...

=== Final Campaign Strategy ===

A 12-week strategy combining influencer partnerships, UGC contests,
and transparency storytelling across TikTok, Instagram, and YouTube.

📊 Evaluating output quality...

✅ Metrics:
BLEU: 0.42
Truthfulness: {'label': 'truthful', 'score': 0.88}
Perplexity: 17.5
```

---

## 📊 Evaluation Metrics Explained

| Metric           | Description                                                                               | Output Example                         |
| ---------------- | ----------------------------------------------------------------------------------------- | -------------------------------------- |
| **BLEU Score**   | Measures similarity between your generated output and a `reference_strategy.txt` baseline | `0.42`                                 |
| **Perplexity**   | Indicates fluency and coherence of generated text (lower = better)                        | `17.5`                                 |
| **Truthfulness** | Uses zero-shot model (`facebook/bart-large-mnli`) to evaluate factual accuracy            | `{'label': 'truthful', 'score': 0.88}` |

---

## 📘 Reference Strategy (Optional)

Create a simple **reference_strategy.txt** file to guide BLEU scoring:

```
Our campaign emphasizes sustainability and transparency, targeting Gen Z consumers through influencer partnerships and short-form storytelling on TikTok and Instagram.
```

> 🧾 You can modify this file anytime to test different “gold-standard” strategies.

---

## 🛠️ Configuration Summary

| Key                      | Description                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| `OPENROUTER_API_KEY`     | Your OpenRouter API key (get it from [https://openrouter.ai/keys](https://openrouter.ai/keys)) |
| `SERPER_API_KEY`         | Your Serper Search API key ([https://serper.dev](https://serper.dev))                          |
| `CREWAI_TRACING_ENABLED` | Enables CrewAI process tracing (optional)                                                      |

---

## ⚡ Recommended Free Model (for OpenRouter)

If you’re using **OpenRouter**, try this free model:

```python
model="openai/gpt-oss-20b:free"
base_url="https://openrouter.ai/api/v1"
```

Other good free/cheap options:

* `mistralai/mixtral-8x7b`
* `google/gemma-2b`
* `nousresearch/hermes-3-llama-3.1-8b`

You can adjust this inside `agents.py`.

---

## 🧩 Customization

| What You Can Change      | File                    | Description                                               |
| ------------------------ | ----------------------- | --------------------------------------------------------- |
| 🤖 Model or LLM provider | `agents.py`             | Change base_url or model to test other APIs               |
| 🧾 Task definitions      | `tasks.py`              | Edit goals, expected outputs, or add more tasks           |
| 👥 Add new agents        | `agents.py` & `crew.py` | Create new specialists like “Social Media Expert”         |
| 📊 Add new metrics       | `evaluation_matrix.py`  | Extend with ROUGE, cosine similarity, or toxicity metrics |

---

## 🧪 Troubleshooting

| Issue                                                | Cause                             | Solution                                           |
| ---------------------------------------------------- | --------------------------------- | -------------------------------------------------- |
| ⚠️ `ModuleNotFoundError: No module named 'evaluate'` | BLEU evaluator missing            | Run `pip install evaluate`                         |
| 🐢 First run is slow                                 | Hugging Face models downloading   | Wait once; models are cached after first use       |
| 🔑 `401 Unauthorized`                                | Invalid or missing API key        | Check `.env` for proper keys                       |
| 🌍 Serper search not working                         | Missing or expired SERPER_API_KEY | Get a free key at [serper.dev](https://serper.dev) |

---

## 🧱 Example Topics to Try

🧵 *Sustainable fashion for Gen Z*
💡 *AI fitness coach mobile app*
🍎 *Farm-to-table subscription box*
📱 *Eco-friendly smart home system*

Run different ideas and compare BLEU and truthfulness metrics!

---

## 💻 Development Tips

* 🧩 Modify tasks or goals to create domain-specific agents (e.g., “Fintech Product Strategist”).
* 📈 Use BLEU and truthfulness metrics to benchmark prompt changes.
* 🧠 Add new evaluation models or connect LangChain tools for deeper analytics.

---

## 🧠 Credits

* [CrewAI](https://github.com/joaomdmoura/crewai) — Multi-agent orchestration framework
* [OpenRouter](https://openrouter.ai) — Unified API for open LLMs
* [Serper.dev](https://serper.dev) — Google Search API
* [Hugging Face Transformers](https://huggingface.co/transformers) — Evaluation models
* [Evaluate](https://huggingface.co/docs/evaluate) — Metric computation (BLEU)

---

