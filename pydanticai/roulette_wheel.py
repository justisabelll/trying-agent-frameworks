from pydantic_ai import Agent, RunContext
import random
from dotenv import load_dotenv

load_dotenv()


roulette_agent = Agent(
    model="claude-3-5-haiku-latest",
    deps_type=int,
    result_type=bool,
    system_prompt=('Use the `roulette_wheel` function to see '
                   'if the customer has won based on the number they provided.')
)


@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], winner_number: int) -> str:
    """check if the sqaure is a winner"""
    return 'winner' if ctx.deps == winner_number else 'loser'


# take user input
user_input = input("Enter a number between 1 and 36: ")


success_number = random.randint(1, 36)
result = roulette_agent.run_sync(
    "Put my money on the correct number being {user_input}", deps=success_number)

print(success_number)
print(result.data)


# result = roulette_agent.run_sync(
#     "I bet five is the winner", deps=success_number)
# print(result.data)
