class School(object):
    def __init__(self, name):
        self.schoolname = name
        self.students = {}
    def add(self, name, grade):
        if grade in self.students:
            self.students[grade].append(name)
        else:
            self.students[grade] = [name]
    def grade(self, n):
        if n not in self.students:
            return set()
        return self.students[n]
    def sort(self):
        s = []
        for i in self.students:
            s.append(tuple((i, tuple(sorted(self.students[i])))))
        return s
