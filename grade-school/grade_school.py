class School:
    def __init__(self):
        self.rost = dict()
        self.add = []

    def add_student(self, name: str, grade: int) -> None:
        if grade not in self.rost:
            self.rost.update({grade: set()})

        if name not in School.roster(self):
            self.rost[grade].add(name)
            self.add.append(True)
        else:
            self.add.append(False)
        return None

    def added(self) -> list[bool]:
        return self.add

    def roster(self) -> list[str]:
        return [
            each
            for grade in sorted(self.rost)
            for each in School.grade(self, grade)
        ]

    def grade(self, grade: int) -> list[str]:
        return sorted(self.rost[grade]) if grade in self.rost else []
