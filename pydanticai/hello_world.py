from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model="claude-3-5-haiku-latest",
    system_prompt="Be concise, reply with one sentence.",

)

result = agent.run_sync('Where does "Hello World" come form ?')
print(result)
