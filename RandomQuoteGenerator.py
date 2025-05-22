import random
quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Push yourself, because no one else is going to do it for you.",
    "Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",
    "Dream it. Wish it. Do it.",
    "Great things never come from comfort zones."
]

def display_random_quote():
    quote = random.choice(quotes)
    print(5*"*","Quote of the Day",5*"*")
    print(f"\"{quote}\"\n")

# Run the function
if __name__ == "__main__":
    display_random_quote()
