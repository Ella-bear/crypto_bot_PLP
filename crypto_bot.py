import time  # Imports the time module, which provides time-related functions (e.g., sleep, current time). Not used in this script.

from typing import Dict, List, Union 
# - Dict: for specifying dictionary types 
# - List: for specifying list types (used in function return types)
# - Union: for specifying variables that can be multiple types

# Sample cryptocurrency database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    },
    "Solana": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7
    },
    "Polkadot": {
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7
    }
}

class CryptoBot:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.personality = "friendly and informative"
    
    def find_cryptos_by_criteria(self, criteria: callable) -> List[str]:
        """Find cryptocurrencies that match the given criteria."""
        return [crypto for crypto, data in crypto_db.items() if criteria(data)]
    
    def get_rising_cryptos(self) -> str:
        """Get cryptocurrencies with rising price trends."""
        rising = self.find_cryptos_by_criteria(lambda x: x["price_trend"] == "rising")
        if not rising:
            return "I couldn't find any cryptocurrencies with rising prices right now."
        return f"Based on our data, {', '.join(rising)} {'is' if len(rising) == 1 else 'are'} trending upward. 📈"
    
    def get_stable_cryptos(self) -> str:
        """Get cryptocurrencies with stable price trends."""
        stable = self.find_cryptos_by_criteria(lambda x: x["price_trend"] == "stable")
        if not stable:
            return "I couldn't find any stable cryptocurrencies right now."
        return f"For stability, you might want to consider {', '.join(stable)}. {'It\'s showing' if len(stable) == 1 else 'They\'re showing'} consistent performance lately."
    
    def get_sustainable_cryptos(self) -> str:
        """Get environmentally sustainable cryptocurrencies."""
        sustainable = self.find_cryptos_by_criteria(lambda x: x["sustainability_score"] >= 7)
        if not sustainable:
            return "I couldn't find any highly sustainable cryptocurrencies right now."
        return f"For eco-friendly options, check out {', '.join(sustainable)}. {'It has' if len(sustainable) == 1 else 'They have'} lower environmental impact! 🌱"
    
    def get_best_overall(self) -> str:
        """Get cryptocurrencies that are both rising and sustainable."""
        best = self.find_cryptos_by_criteria(
            lambda x: x["price_trend"] == "rising" and x["sustainability_score"] >= 7
        )
        if not best:
            rising = self.find_cryptos_by_criteria(lambda x: x["price_trend"] == "rising")
            if rising:
                return f"For growth potential, {', '.join(rising)} {'is' if len(rising) == 1 else 'are'} trending upward, though not the most sustainable."
            return "I'm not seeing any cryptocurrencies that meet both profitability and sustainability criteria right now."
        return f"I'd recommend {', '.join(best)}! {'It\'s' if len(best) == 1 else 'They\'re'} both trending upward and environmentally friendly. 🚀🌱"
    
    def get_crypto_info(self, crypto_name: str) -> str:
        """Get detailed information about a specific cryptocurrency."""
        crypto = next((c for c in crypto_db.keys() if c.lower() == crypto_name.lower()), None)
        if not crypto:
            return f"I don't have information about {crypto_name} in my database."
        
        data = crypto_db[crypto]
        trend_emoji = "📈" if data["price_trend"] == "rising" else "➡️"
        eco_emoji = "🌱" if data["sustainability_score"] >= 7 else ""
        
        return f"""Here's what I know about {crypto}:
- Price trend: {data['price_trend']} {trend_emoji}
- Market cap: {data['market_cap']}
- Energy usage: {data['energy_use']}
- Sustainability score: {data['sustainability_score']}/10 {eco_emoji}"""
    
    def process_query(self, query: str) -> str:
        """Process user queries and return appropriate responses."""
        query = query.lower()

        # Check for greetings (match whole words only)
        greetings = {"hello", "hi", "hey", "what can you do"}
        query_words = set(query.replace("?", "").replace("!", "").split())
        if greetings & query_words:
            return f"Hey there! I'm {self.name}, your friendly crypto advisor. How can I help you today?"

        # Check for specific cryptocurrencies
        for crypto in crypto_db.keys():
            if crypto.lower() in query:
                return self.get_crypto_info(crypto)

        # Special case: Direct answer for a specific long-term growth question
        if "which crypto should i buy for long-term growth" in query:
            return (
                "For long-term growth, Bitcoin is often considered by many as a strong option due to its market dominance and adoption. "
                "However, always do your own research and remember: Crypto investments carry significant risk! This is educational content, not financial advice."
            )

        # Check for long-term growth queries (add 'buy' and 'which' for robustness)
        if (
            ("long-term" in query or "long term" in query)
            and ("growth" in query or "buy" in query or "which" in query)
        ):
            return f"For long-term growth, {self.get_best_overall()}\n\nRemember: Crypto investments carry significant risk! This is educational content, not financial advice."

        # Check for trending/price queries
        if any(word in query for word in ["trending", "trend", "going up", "rising", "price increase"]):
            return self.get_rising_cryptos()
        
        # Check for stability queries
        if any(word in query for word in ["stable", "consistent", "reliability", "safe"]):
            return self.get_stable_cryptos()
        
        # Check for sustainability queries
        if any(word in query for word in ["sustainable", "green", "eco", "environment", "friendly"]):
            return self.get_sustainable_cryptos()
        
        # Check for best overall investment queries
        if any(word in query for word in ["best", "recommend", "suggestion", "invest", "buy", "good choice"]):
            return f"{self.get_best_overall()}\n\nRemember: Crypto investments carry significant risk! This is educational content, not financial advice."
        
        return "I'm not sure how to help with that query. You can ask me about trending coins, sustainable options, or specific cryptocurrencies like Bitcoin or Ethereum!"

def main():
    bot = CryptoBot()
    print(f"Welcome to {bot.name}! Type 'quit' to exit.")
    print("Ask me about cryptocurrency trends, sustainability, and investment advice!")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'quit':
            print("\nThanks for chatting! Remember to always do your own research before investing. 👋")
            break
        
        print(f"\n{bot.name}: {bot.process_query(user_input)}")

if __name__ == "__main__":
    main()