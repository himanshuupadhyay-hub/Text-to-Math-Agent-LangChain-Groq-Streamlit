# 🧮 Text-to-Math Agent

An AI-powered **Text-to-Math Agent** built with **LangChain, Groq, and Streamlit** that understands natural-language math problems and uses dedicated tools to perform calculations and solve simple algebraic equations.

Instead of relying entirely on the LLM to calculate answers, the agent is instructed to **use tools for mathematical operations**, making the results more reliable and transparent.

## 🚀 Live Demo

**Live Demo:** Add your Streamlit deployment URL here

> Example: `https://your-app-name.streamlit.app`

## 📌 Features

* 🧠 Natural-language understanding of math word problems
* 🔧 LangChain tool-calling agent
* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* 📊 Percentage calculations
* 📐 Simple algebraic equation solving
* 🤖 Groq-powered LLM
* 💬 Conversation/history of previously solved problems
* ⚡ Interactive Streamlit interface
* 🛡️ Tool-based calculation instead of relying solely on LLM-generated arithmetic

## 🏗️ Architecture

```text
                 User
                   │
                   ▼
          ┌─────────────────┐
          │    Streamlit    │
          │       UI        │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │  LangChain      │
          │ Tool-Calling    │
          │     Agent       │
          └────────┬────────┘
                   │
            ┌──────┴──────┐
            │             │
            ▼             ▼
     ┌─────────────┐ ┌───────────────┐
     │ Calculator  │ │ Solve Algebra │
     │    Tool     │ │     Tool      │
     └─────────────┘ └───────────────┘
            │             │
            └──────┬──────┘
                   ▼
              Final Answer
```

## 🛠️ Tech Stack

| Technology        | Purpose                           |
| ----------------- | --------------------------------- |
| Python            | Core programming language         |
| Streamlit         | Web application interface         |
| LangChain         | Agent and tool orchestration      |
| LangChain Classic | Tool-calling agent implementation |
| LangChain Core    | Prompt and message handling       |
| Groq              | LLM inference                     |
| GPT-OSS-20B       | Language model                    |
| python-dotenv     | Environment variable management   |

## 🔧 Tools

### 1. Calculator

The `calculator` tool handles basic mathematical operations:

* Addition
* Subtraction
* Multiplication
* Division
* Percentage

Example:

```text
Input:
What is 25% of 400?

Tool:
calculator(400, 25, "percentage")

Result:
100
```

### 2. Algebra Solver

The `solve_algebra` tool solves equations in the form:

```text
ax + b = c
```

The solution is calculated using:

```text
x = (c - b) / a
```

Example:

```text
Input:
Solve 5x + 10 = 35

Tool:
solve_algebra(5, 10, 35)

Result:
x = 5
```

## 🧠 How It Works

1. The user enters a mathematical word problem.
2. The Streamlit application sends the question to the LangChain agent.
3. The Groq-powered LLM determines which mathematical tool is required.
4. The agent calls the appropriate tool.
5. The tool performs the calculation.
6. The tool result is returned to the agent.
7. The final answer is displayed in the Streamlit interface.
8. The question and answer are stored in the session history.

## 📂 Project Structure

```text
text-to-math-agent/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/text-to-math-agent.git
cd text-to-math-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your `.env` file to GitHub.

Add this to `.gitignore`:

```text
.env
.venv/
__pycache__/
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 Example Problems

You can try questions such as:

```text
What is 25% of 800?
```

```text
Calculate 125 multiplied by 24.
```

```text
What is 500 divided by 25?
```

```text
Solve 4x + 12 = 32.
```

```text
If a product costs $800 and has a 15% discount, what is the discount amount?
```

## 🎯 Key Learning Outcomes

This project demonstrates practical implementation of:

* LLM-powered applications
* LangChain agents
* Tool calling
* Custom LangChain tools
* Prompt engineering
* Function/tool-based reasoning
* Groq LLM integration
* Streamlit application development
* Environment variable management
* Session-state-based conversation history

## 🔮 Future Improvements

Possible improvements include:

* Support for quadratic equations
* Support for fractions and mixed numbers
* Scientific calculator operations
* Mathematical expression parsing
* Step-by-step solution generation
* Equation visualization
* Chat-based interface
* Persistent conversation history
* Error handling for invalid equations
* Additional mathematical tools
* Voice-based math problem input

## 👨‍💻 Author

**Himanshu Upadhyay**

AI/ML & Generative AI Developer

### Skills Demonstrated

`Python` `LangChain` `LLM Agents` `Tool Calling` `Groq` `Streamlit` `Generative AI`

---

⭐ If you found this project useful, consider giving the repository a star!
