import requests

# Shuffle the deck and get the deck_id
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
shuffle_response = requests.get(shuffle_url)
shuffle_data = shuffle_response.json()

# Extract the deck_id from the response
deck_id = shuffle_data['deck_id']
print(f"Deck ID: {deck_id}\n")

# Draw 5 cards from the shuffled deck
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response = requests.get(draw_url)
draw_data = draw_response.json()

# Print the value and suit of each drawn card
print("The 5 drawn cards are:")
for card in draw_data['cards']:
    value = card['value']
    suit = card['suit']
    print(f"{value} of {suit}")

# Print remaining cards in the deck
remaining_cards = draw_data['remaining']
print(f"\nRemaining cards in the deck: {remaining_cards}")