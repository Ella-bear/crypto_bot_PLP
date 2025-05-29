# Crypto Advisor Chatbot

# 1. Predefined crypto dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 0.3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 0.6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.8
    }
}

# 2. Define chatbot logic
def respond_to_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        # Find the coin with the highest sustainability score
        recommend = max(crypto_db, key=lambda coin: crypto_db[coin]["sustainability_score"])
        return f"🌱 I recommend {recommend}. It is eco-friendly and has good potential for the future. 🌍"

    elif "trending" in user_query or "rising" in user_query:
        trending_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        if trending_coins:
            return f"📈 The coins that are currently trending up are: {', '.join(trending_coins)}. 🚀"
        else:
            return "😕 There are no coins trending up at the moment."

    elif "long-term" in user_query or "investment" in user_query:
        # Choose coins that are rising and have a high market cap
        best_choices = [
            coin for coin in crypto_db
            if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"
        ]
        if best_choices:
            return f"⏳ For long-term growth, you might consider {best_choices[0]}. It has strong market support and good profit potential. 💰"
        else:
            return "🤔 I couldn't find a good option for long-term investment based on the data I have."
        
    elif "available coins" in user_query or "list all coins available" in user_query:
        # List all available coins
        available_coins = ", ".join(crypto_db.keys())
        return f"💰 Available coins: {available_coins}. You can ask about their trends, sustainability, or long-term growth potential. 📊"

    elif "defination" in user_query or "what is" in user_query:

        # Always return the same message for any definition request
        return "❓ Sorry, I couldn't find any defenition for that. Please ask about sustainability, trends, or long-term growth. 🤖"
    
    elif "energy use" in user_query or "energy consumption" in user_query:
        results = [f"{coin}: {crypto_db[coin]['energy_use']}" for coin in crypto_db]
        return "⚡ Energy use by coin:\n" + "\n".join(results)

    elif "add coin" in user_query:
        return "🛠️ Sorry, adding new coins is not supported yet."

# 3. Run chatbot interaction
print("👋 Hi, I’m CryptoBot, your crypto advisor! 🤖")
print("You can ask me things like: 'Which crypto is trending up?' or 'What’s the most sustainable coin?'\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("CryptoBot: Goodbye! Remember to always research before you invest.")
        break
    response = respond_to_query(user_input)
    print("CryptoBot:", response)
