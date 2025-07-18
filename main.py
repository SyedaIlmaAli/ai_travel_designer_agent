from agents import Agent, RunConfig, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Tool: get_flights
@function_tool
def get_flights(destination: str) -> list[str]:
    """
    Returns a list of mock flight options for a given destination.
    """
    flights = {
        "Bali": ["PKR 120,000 - Emirates", "PKR 135,000 - Qatar Airways"],
        "Paris": ["PKR 145,000 - Turkish Airlines", "PKR 160,000 - Emirates"],
        "Las Vegas": ["PKR 180,000 - Qatar Airways", "PKR 200,000 - American Airlines"]
    }
    return flights.get(destination, ["No flights found."])

# Tool: suggest_hotels
@function_tool
def suggest_hotels(destination: str) -> list[str]:
    """
    Returns a list of mock hotel options for a given destination.
    """
    hotels = {
        "Bali": ["Ubud Heaven Villa", "Bali Garden Beach Resort"],
        "Paris": ["Hotel Le Meurice", "Novotel Paris Centre"],
        "Las Vegas": ["Bellagio", "MGM Grand"]
    }
    return hotels.get(destination, ["No hotels found."])

@function_tool
def explore_local(destination: str) -> dict:
    """
    Suggests top attractions and food options in the given location.
    """
    data = {
        "Bali": {
            "attractions": ["Ubud Monkey Forest", "Tegallalang Rice Terraces"],
            "food": ["Nasi Goreng", "Babi Guling"]
        },
        "Paris": {
            "attractions": ["Eiffel Tower", "Louvre Museum"],
            "food": ["Croissants", "Ratatouille"]
        }
    }
    return data.get(destination, {"attractions": [], "food": []})

destination_agent = Agent(
    name="DestinationAgent",
    instructions="You help users find destinations based on mood like relax, adventure, etc.",
    model= model
)

booking_agent = Agent(
    name="BookingAgent",
    instructions="You book flights and hotels. Use tools to get mock data.",
    tools=[get_flights, suggest_hotels],
    model=model
)

explorer_agent = Agent(
    name="ExploreAgent",
    instructions="You suggest attractions and food in a destination using explore_local tool.",
    tools=[explore_local],
    model=model
)

agent = Agent(name = "AI Travel Designer Agent",
              model= model, 
              instructions = """You are a smart and friendly AI travel planner.
                                Your job is to guide users through planning their entire trip in three steps:
                                1. First, ask the user's mood or interest (e.g., relax, adventure, romantic) and hand off to the DestinationAgent to recommend places.
                                2. Once a destination is chosen, hand off to the BookingAgent to get mock flight and hotel options.
                                3. Finally, hand off to the ExploreAgent to suggest local attractions and food experiences for the chosen place.
                                Coordinate between these agents to deliver a seamless and delightful travel plan.""",
              handoffs=[booking_agent, explorer_agent, destination_agent])

result = Runner.run_sync(agent, """I am looking for:
                                    1. Mid-range
                                    2. Karachi, Pakistan
                                    3. Next month
                                    4. Couple
                                    5. Beach and spa relaxation
                                    6. Please avoid places like Dubai or Thailand — already visited them."""
, run_config = config)

print(result.final_output)

def main():
    print("Hello from ai-travel-designer-agent!")


if __name__ == "__main__":
    main()
