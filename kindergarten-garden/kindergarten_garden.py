class Garden:

    all_students = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry",
    ]

    plant_types = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    def __init__(self, diagram: str, students=all_students) -> None:
        self.garden = diagram.split()
        self.students_list = sorted(students)

    def plants(self, name: str) -> list[str]:
        n = self.students_list.index(name) * 2
        plants = self.garden[0][n : n + 2] + self.garden[1][n : n + 2]
        return [self.plant_types[letter] for letter in plants]
