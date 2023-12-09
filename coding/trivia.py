import random

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the most popular video game of all time?",
                "options": ["Minecraft", "Super Mario Bros.", "Tetris", "Fortnite"],
                "correct_answer": "Tetris",
            },
            {
                "question": "Which company developed the game 'The Legend of Zelda'?",
                "options": ["Nintendo", "Microsoft", "Sony", "Ubisoft"],
                "correct_answer": "Nintendo",
            },
            {
                "question": "What is the main character in the 'Assassin's Creed' series?",
                "options": ["Ezio Auditore", "Altair Ibn-La'Ahad", "Connor Kenway", "Bayek"],
                "correct_answer": "Ezio Auditore",
            },
            {
                "question": "In 'Minecraft,' what do you need to mine to obtain diamonds?",
                "options": ["Stone", "Gold Ore", "Diamond Ore", "Iron Ore"],
                "correct_answer": "Diamond Ore",
            },
            {
                "question": "Who is the main antagonist in 'Super Mario Bros.'?",
                "options": ["Bowser", "Luigi", "Toad", "Yoshi"],
                "correct_answer": "Bowser",
            },
            {
                "question": "Which game is known for its battle royale mode, 'Warzone'?",
                "options": ["Fortnite", "Call of Duty", "PUBG", "Apex Legends"],
                "correct_answer": "Call of Duty",
            },
            {
                "question": "What game features a block-building world with a creative mode?",
                "options": ["Roblox", "Terraria", "LEGO Worlds", "Minecraft"],
                "correct_answer": "Minecraft",
            },
            {
                "question": "Which game has a plumber named Mario as its main character?",
                "options": ["The Legend of Zelda", "Sonic the Hedgehog", "Super Mario Bros.", "Pac-Man"],
                "correct_answer": "Super Mario Bros.",
            },
            {
                "question": "In 'Pokémon,' what is the name of the electric mouse Pokémon?",
                "options": ["Jigglypuff", "Pikachu", "Charizard", "Squirtle"],
                "correct_answer": "Pikachu",
            },
            {
                "question": "What game features a battle royale mode called 'Blackout'?",
                "options": ["Fortnite", "Call of Duty: Black Ops 4", "PUBG", "Apex Legends"],
                "correct_answer": "Call of Duty: Black Ops 4",
            },{
                "question": "Which video game series allows you to explore the post-apocalyptic wasteland known as the Capital Wasteland?",
                "options": ["The Elder Scrolls", "Fallout", "Borderlands", "Metro Exodus"],
                "correct_answer": "Fallout",
            },
            {
                "question": "In 'The Legend of Zelda: Ocarina of Time,' what does Link use to travel back and forth in time?",
                "options": ["A time machine", "A magic sword", "The Ocarina of Time", "A time-traveling horse"],
                "correct_answer": "The Ocarina of Time",
            },
            {
                "question": "What is the name of the main character in the 'Halo' series?",
                "options": ["Master Chief", "Sergeant Johnson", "Cortana", "Arbiter"],
                "correct_answer": "Master Chief",
            },
            {
                "question": "Which video game is set in a fictional medieval kingdom called Lordran?",
                "options": ["The Witcher 3", "Dark Souls", "Skyrim", "Dragon Age: Inquisition"],
                "correct_answer": "Dark Souls",
            },
            {
                "question": "In 'World of Warcraft,' what is the name of the undead capital city?",
                "options": ["Stormwind", "Orgrimmar", "Dalaran", "Undercity"],
                "correct_answer": "Undercity",
            },
            {
                "question": "Which game features a battle royale mode called 'Blackout'?",
                "options": ["Fortnite", "Call of Duty: Black Ops 4", "PUBG", "Apex Legends"],
                "correct_answer": "Call of Duty: Black Ops 4",
            },
            {
                "question": "What is the name of the main character in 'Uncharted' game series?",
                "options": ["Nathan Drake", "Lara Croft", "Solid Snake", "Sam Fisher"],
                "correct_answer": "Nathan Drake",
            },
            {
                "question": "In 'Resident Evil,' what is the name of the fictional city plagued by zombie outbreaks?",
                "options": ["Raccoon City", "Silent Hill", "Arklay Mountains", "Umbrella Corporation"],
                "correct_answer": "Raccoon City",
            },
            {
                "question": "What is the name of the iconic hedgehog character created by Sega?",
                "options": ["Tails", "Knuckles", "Shadow", "Sonic"],
                "correct_answer": "Sonic",
            },
            {
                "question": "Which game allows you to build and manage your own virtual world with blocks?",
                "options": ["Roblox", "Terraria", "Minecraft", "The Sims"],
                "correct_answer": "Minecraft",
            },
]
        self.score = 0

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def display_question(self, question):
        print(question["question"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")

    def start_quiz(self):
        self.shuffle_questions()
        print("Welcome to the Video Game Trivia Quiz!")
        print("Answer the following questions:")
        for question in self.questions:
            self.display_question(question)
            player_answer = input("Enter the number of your answer: ")
            if self.check_answer(question, int(player_answer)):
                self.score += 1
                print("Correct! Great job!")
            else:
                print(f"Sorry, the correct answer is: {question['correct_answer']}")
        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")

    def check_answer(self, question, player_choice):
        correct_choice = question["options"].index(question["correct_answer"]) + 1
        return player_choice == correct_choice



if __name__ == "__main__":
    quiz = QuizGame()
    quiz.start_quiz()