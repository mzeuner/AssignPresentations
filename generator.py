import random
import pandas as pd

class Student:
    def __init__(self, name, prevPres, exDone):
        self.name = name
        self.prevPres = prevPres
        self.rndNo = random.uniform(0, 1)
        self.exDone = exDone # dictionary { "4a" : 1, "4b" : 0, ... }

    def __str__(self):
        return self.name

    def score (self, ex):
        # change weight if needed
        return self.rndNo * self.exDone[ex] * 0.5 ** self.prevPres


def assignPres (exercises,students):
    presDict = {}
    for ex in exercises:
        students.sort(key = lambda x: x.score(ex))
        # need side effect depending on ex, can this be avoided?
        presDict[ex] = students.pop()
    return presDict


def makeExDone (df,exercises,index):
    return { ex : df[ex][index] for ex in exercises }


def makeStudent (df,exercises,index,row):
    return Student(row['name'], row['prev. pres.'],makeExDone(df,exercises,index))


def makeExercises(df):
    exercises = list(df)
    del exercises[0:2]

    # put hardest ex. first and remove unsolved ones
    exercises.sort(key=lambda ex: sum(df[ex]))
    return exercises


def main():

    infile = input("Which exercise sheet: ")
    df = pd.read_csv(infile+'.csv')

    exercises = makeExercises(df)

    # create list of students, this is very slow apparently!
    students = [ makeStudent(df,exercises,index,row) for index, row in df.iterrows() ]

    outfile = "presentations_" + infile + '.md'
    with open(outfile, 'w', encoding="utf-8") as f:
        for ex, stu in sorted(assignPres(exercises,students).items()):
            f.write(f"Exercise(s) `{ex}` will be presented by **{stu}**\n")

    print("Done!")

if __name__ == "__main__":
    main()
