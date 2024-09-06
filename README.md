## A short script for randomly selecting students to present exercises

### Running the script
Run the script in a terminal and give the name of a correctly
formatted CSV-file in the same directory when prompted (without the
`.csv` file ending), like so:

``` shell
$ python3 generator.py
> Which exercise sheet: test
> Done!
```
You get the results in a markdown [file](https://github.com/mzeuner/AssignPresentations/blob/main/presentations_test.md).

### Basic idea
The CSV-file that is parsed by the script should correspond
to one exercise sheet/session. Each row contains the name of a student,
the number of times the student has already presented an exercise in the course,
and for each exercise (or block of exercises) to be presented a 1 or 0,
indicating whether the student has handed in a solution to the exercise.
See [`test.csv`](https://github.com/mzeuner/AssignPresentations/blob/main/test.csv)
for an example.

The script then stores this information for each student together
with a random floating point number between 0 and 1. Given an exercise,
a student gets a score as follows: If they didn't do the exercise, their score is 0.
Otherwise, if their random score is `r` and they already presented `n` times,
they get a score of `r / (2^n)`.

The script goes through the exercises, starting with the hardest one (i.e. the
one solved by the fewest students), and picks the student with the highest score.
This way, students don't get selected for exercises they haven't done. A student
that already presented once is only half as likely to be picked over a student
who hasn't presented yet, only a quarter as likely if they presented twice and so on.
This way students can never be sure that they will not have to present again, but
the script will mostly select students that have presented less than others.
