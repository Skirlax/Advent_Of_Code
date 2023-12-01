class Solve:
    def __init__(self):
        self.content = self.load_file()
        self.scores = {"X": 1, "Y": 2, "Z": 3}
        self.marks = {"X": "A", "Y": "B", "Z": "C", "A": "X", "B": "Y", "C": "Z"}
        self.winning_states = ["C X", "B Z", "A Y"]
        self.losing_states = {"A": "Z", "B": "X", "C": "Y"}
        self.winning_states_dict = {"C": "X", "B": "Z", "A": "Y"}

    @staticmethod
    def load_file():
        with open("inputs/input2.txt") as f:
            ct = f.read()
            f.close()
        return ct

    def solve(self):
        score = 0
        for state in self.content.split("\n\n"):
            for line in state.split("\n"):
                if self.marks[line[2]] == line[0]:
                    score += 3

                elif line in self.winning_states:
                    score += 6
                else:
                    score += 0

                score += self.scores[line[2]]

        return score

    def solve_part_two(self):
        score = 0
        for state in self.content.split("\n\n"):
            for line in state.split("\n"):
                if line[2] == "Y":
                    score += self.scores[self.marks[line[0]]] + 3
                elif line[2] == "X":
                    score += self.scores[self.losing_states[line[0]]]
                else:
                    score += self.scores[self.winning_states_dict[line[0]]] + 6

        return score


if __name__ == "__main__":
    print(Solve().solve_part_two())
