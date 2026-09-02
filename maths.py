import streamlit as st
from langchain_groq import ChatGroq
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor, tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()


@tool
def calculator(a: float, b: float, operation: str) -> str:
    """Perform a basic mathematical calculation. operation can be:
    add/addition, subtract/subtraction, multiply/multiplication,
    divide/division, or percent/percentage."""

    op = operation.strip().lower()

    if op in ["add", "addition", "+"]:
        return str(a + b)
    if op in ["subtract", "subtraction", "-"]:
        return str(a - b)
    if op in ["multiply", "multiplication", "*", "x"]:
        return str(a * b)
    if op in ["divide", "division", "/"]:
        if b == 0:
            return "Cannot divide by zero."
        return str(a / b)
    if op in ["percent", "percentage", "%"]:
        return str((a * b) / 100)

    return f"Unknown operation: '{operation}'. Use add, subtract, multiply, divide, or percentage."


@tool
def solve_algebra(a: float, b: float, c: float) -> str:
    """Solve a simple equation of the form ax + b = c."""
    x = (c - b) / a
    return f"x = {x}"

tools=[calculator,solve_algebra]

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

system_message = """You are a text-to-math assistant.Use the calculator tool for arithmetic and percentage questions.
Solve the problem step by step.Don't Answer by own without using the tools which are provided to you for solving the problem.
Never replace or change a result returned by a tool.Keep the explanation simple and clear.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("human", "{input}"),
    MessagesPlaceholder("agent_scratchpad")
])

agent = create_tool_calling_agent(
    llm=llm, 
    tools=tools, 
    prompt=prompt
    )

agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True
    )

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Text-to-Math Agent")

question = st.text_input("Enter a math word problem:")

if st.button("Solve") and question.strip():
    with st.spinner("Solving..."):
        result = agent_executor.invoke({"input": question})
        answer = result["output"]

    st.session_state.history.append((question, answer))

st.subheader("Conversation History")

for q, a in reversed(st.session_state.history):
    st.markdown(f"Q: {q}")
    st.markdown(f"A: {a}")