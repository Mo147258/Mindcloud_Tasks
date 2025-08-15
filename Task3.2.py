class VotingSystem:
    def __init__(self):

        self.__votes = {}

    def add_candidate(self, name):
        if name not in self.__votes:
            self.__votes[name] = 0
            print(f"Candidate '{name}' added successfully.")
        else:
            print(f"Candidate '{name}' already exists.")

    def remove_candidate(self, name):
        if name in self.__votes:
            del self.__votes[name]
            print(f"Candidate '{name}' removed successfully.")
        else:
            print(f"Candidate '{name}' does not exist.")

    def vote_to_candidate(self, name):
        if name in self.__votes:
            self.__votes[name] += 1
            print(f"Vote cast for '{name}'.")
        else:
            print(f"Candidate '{name}' not found.")

    def display_winner(self):
        if not self.__votes:
            print("No candidates available.")
            return
        max_votes = max(self.__votes.values())
        winners = [name for name, votes in self.__votes.items() if votes == max_votes]
        if len(winners) == 1:
            print(f"The winner is '{winners[0]}' with {max_votes} votes.")
        else:
            print(f"It's a tie between: {', '.join(winners)} with {max_votes} votes each.")

    def show_candidates(self):
        if not self.__votes:
            print("No candidates available.")
        else:
            print("\nCurrent Candidates & Votes:")
            for name, votes in self.__votes.items():
                print(f" - {name}: {votes} votes")
            print()

if __name__ == "__main__":
    system = VotingSystem()

    while True:
        print("\n===== Voting System Menu =====")
        print("1. Add Candidate")
        print("2. Remove Candidate")
        print("3. Vote for Candidate")
        print("4. Display Candidates")
        print("5. Show Winner")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter candidate name: ").strip()
            system.add_candidate(name)
        elif choice == "2":
            name = input("Enter candidate name to remove: ").strip()
            system.remove_candidate(name)
        elif choice == "3":
            name = input("Enter candidate name to vote for: ").strip()
            system.vote_to_candidate(name)
        elif choice == "4":
            system.show_candidates()
        elif choice == "5":
            system.display_winner()
        elif choice == "6":
            print("Exiting Voting System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
