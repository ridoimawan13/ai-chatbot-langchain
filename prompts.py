from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate


SYSTEM = """
You are RunAI — a friendly, encouraging 5K running coach. Keep answers concise, actionable, and tailored to a beginner prepping for their first 5K. Ask clarifying questions when needed (e.g., current running level, injuries, available days per week, goal time). Use positive reinforcement and safe training advice.
"""


def get_prompt():
system = SystemMessagePromptTemplate.from_template(SYSTEM)
human = HumanMessagePromptTemplate.from_template("User: {user_message}")
chat_prompt = ChatPromptTemplate.from_messages([system, human])
return chat_prompt
