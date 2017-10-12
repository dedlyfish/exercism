class Garden(object):
    def __init__(self, string, students = ['Alice','Bob','Charlie','David','Eve','Fred',
                                           'Ginny','Harriet','Ileana','Joseph','Kincaid','Larry']):
        FullGarden = ''
        self.cups = []
        self.children = dict(map(lambda x: (x[1], x[0]),enumerate(sorted(students))))
        for i in range(0, len(string.split()[0]),2):
            FullGarden += string.split()[0][i:i+2] + string.split()[1][i:i+2]
        for i in range(0, len(FullGarden), 4):
            self.cups.append(FullGarden[i:i+4])
            
    def plants(self, name):
        m = { 'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets' }
        return list(map(lambda x: m[x], self.cups[self.children[name]]))

