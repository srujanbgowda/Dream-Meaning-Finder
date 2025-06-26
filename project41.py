# Dream Meaning Finder

dream_dictionary = {
    "water": "Emotions, subconscious thoughts, or a cleansing process.",
    "flying": "Freedom, ambition, or rising above a situation.",
    "teeth falling": "Anxiety about appearance or loss of control.",
    "snake": "Hidden fears, transformation, or healing.",
    "death": "End of something old, start of something new.",
    "baby": "New beginnings, innocence, or vulnerability.",
    "chased": "Avoiding a situation you should confront.",
    "falling": "Insecurity, fear of failure, or feeling out of control.",
    "money": "Self-worth, success, or opportunities.",
    "mirror": "Self-reflection or seeing things clearly."
}

print("💤 Welcome to the Dream Meaning Finder!")
user_input = input("Enter a key symbol or word from your dream: ").lower()

meaning = dream_dictionary.get(user_input)

if meaning:
    print(f"🔮 The meaning of '{user_input}' in dreams: {meaning}")
else:
    print("😴 Sorry, no meaning found. Try a different word.")