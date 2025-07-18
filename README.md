# 🧠 AI Travel Designer Agent

An intelligent multi-agent travel planning assistant built using the **OpenAI Agents SDK**.  
This project uses tools and agent-to-agent handoffs to plan a complete travel experience based on the user's mood, preferences, and budget.

---

## ✨ Features

- 🤖 Powered by **OpenAI Agents SDK + Runner**
- 🔁 Multi-agent handoff system (Destination → Booking → Exploration)
- 🛠️ Custom Tools for:
  - Flight recommendations
  - Hotel suggestions
  - Local exploration

---

## 📁 Project Structure

```
ai-travel-designer-agent/
│
├── travel_tools.py        # Tools used by agents (flights, hotels, food)
├── agents_setup.py        # Registers all 3 custom agents
├── main.py                # Main agent + runner logic for handoffs
├── .env                   # OpenAI API Key stored here
└── README.md              # Full project documentation
```

---

## ⚙️ Tools Used

### ✈️ `get_flights(destination: str)`
Simulates available flights to a given destination.  
Returns mock flight data for the BookingAgent.

```python
[
  {"airline": "Air PK", "price": "$210", "duration": "3h"},
  {"airline": "FlyEase", "price": "$240", "duration": "2.5h"}
]
```

---

### 🏨 `suggest_hotels(destination: str)`
Returns a list of mock hotels in the destination for BookingAgent.

```python
[
  {"name": "Relax Inn", "price": "$80/night", "amenities": ["Spa", Pool"]},
  {"name": "Sunset Resort", "price": "$110/night", "amenities": ["Beach Access", "Massage"]}
]
```

---

### 🍜 `explore_local(destination: str)`
Suggests top attractions and local food options for ExploreAgent.

```python
{
  "attractions": ["Beach Sunset Point", "Seaview Walk"],
  "food": ["Grilled fish", "Local Biryani"]
}
```

---

## 👥 Agents

### 🧭 DestinationAgent

- Asks travel questions:
  - "What's your budget?"
  - "What type of relaxation do you prefer (beach, spa, etc.)?"
- Filters out restricted/unwanted destinations.
- Suggests destinations based on mood, budget, and group type.

#### 🗣️ Sample Prompt:
```
I want a mid-range relaxing beach trip with spa options. I’ll be traveling with my partner, departing from Karachi.
```

---

### 🏨 BookingAgent

- Receives destination from `DestinationAgent`
- Uses `get_flights()` and `suggest_hotels()` tools
- Simulates hotel and flight bookings using mock data

---

### 🍽️ ExploreAgent

- Receives destination from `BookingAgent`
- Uses `explore_local()` to find food and attractions
- Suggests top places to visit, eat, and relax nearby

---

## 🔁 Agent Handoff Flow

```
[User Prompt] 
   ↓
[AI Travel Designer Agent]
   ↓
→ DestinationAgent 
     → suggests location
→ BookingAgent 
     → uses tools to simulate bookings
→ ExploreAgent 
     → suggests food & activities
   ↓
[User receives complete plan]
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-travel-designer-agent
cd ai-travel-designer-agent
```

### 2. Install dependencies

```bash
pip install openai python-dotenv
```

### 3. Create a `.env` file

```env
API_KEY=your-openai-api-key
```

### 4. Run the app

```bash
python main.py
```

---

## 💬 Example Output

```text
User: I’m looking for a relaxing spa vacation next month with my spouse. I prefer a beach destination but not Dubai or Thailand.

→ DestinationAgent:
   Recommends French Beach, Hawke's Bay, or Gadani Beach near Karachi

→ BookingAgent:
   Finds flight and hotel options to French Beach with mock prices

→ ExploreAgent:
   Suggests seafood restaurants, spa huts, and quiet beach spots

✅ Final Result:
You receive a complete travel plan with location, bookings, and activities!
```

---

## 💡 Use Cases

- AI-powered travel agency assistant
- Chat-based travel recommendation system
- OpenAI Agent SDK demo project
- Portfolio or hackathon showcase

---

## 🧪 Ideas for Future Enhancements

- Connect to live APIs (Skyscanner, Booking.com, Yelp, etc.)
- Add memory for multi-turn conversations
- Build a frontend with Streamlit or Next.js
- Use Redis or Pinecone for context storage

---

## 📜 License

MIT License © 2025 Syeda Ilma Ali

---

## 🙋‍♀️ Author

Built with ❤️ by [Syeda Ilma Ali](https://github.com/syedailmaali)  
Inspired by the power of OpenAI Agents SDK.
