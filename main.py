import os
from fastapi import FastAPI, Request
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from .prompts import get_prompt


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL = os.getenv('MODEL', 'gpt-4o')


app = FastAPI()


class MessageIn(BaseModel):
message: str
user_id: str = "default_user"


# simple in-memory store of ConversationChain per user (for demo)
_chains = {}


@app.post('/api/chat')
async def chat(payload: MessageIn):
user = payload.user_id
if user not in _chains:
# create a new chain per user
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
llm = ChatOpenAI(model_name=MODEL, temperature=0.7, openai_api_key=OPENAI_API_KEY)
prompt = get_prompt()
chain = ConversationChain(llm=llm, prompt=prompt, memory=memory, verbose=False)
_chains[user] = chain


chain = _chains[user]
response = chain.run(payload.message)
return {"reply": response}


@app.get('/api/health')
async def health():
return {"status":"ok"}
