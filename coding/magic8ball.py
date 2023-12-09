import random

responses = [
    "Yes.",
    "No.",
    "Think about it and ask again.",
    "Ask your mother.",
    "Ask your father.",
    "It seems like a good idea.",
    "It seems like a bad idea.",
    "likely.",
    ".",
    ".",
    ".",
    ".",
    ".",
    ".",
    ".",
    ".",
    ".",
    ".",
    ".",
    "."
]

def coin():
    input("Ask the Magic 8-Ball a yes-or-no question: ")
    response = random.choice(responses)
    print(response)

if __name__ == "__main__":
    coin()