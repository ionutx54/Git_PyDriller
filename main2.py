from pydriller.metrics.process.lines_count import LinesCount
from pydriller.metrics.process.commits_count import CommitsCount
from pydriller.metrics.process.contributors_count import ContributorsCount


# Important!
# from_commit1 si to_commit1 se obtin prin apelarea in terminal a comenzii: git log --format=%H | tail -, si se adauga ultima valoare la from_commit1
# si prima valoare la to_commit1
# Aceste valori reprezinta formatul hash generat de github al commiturilor
# Codul a fost documentat de la adresa: https://readthedocs.org/projects/pydriller/downloads/pdf/latest/

from_commit1="8119659fb1e4ae6fabe8897c42ba7629fda07b21"
to_commit1="c2f7b6575156a7c3e049e17248acb6b580ba899f"

metric = ContributorsCount(path_to_repo='G:\\GIT_Repos\\spring-framework',
from_commit='8119659fb1e4ae6fabe8897c42ba7629fda07b21',
to_commit='c2f7b6575156a7c3e049e17248acb6b580ba899f')
count = metric.count()
print('Number of contributors per file: {}'.format(count))

# Get Number of lines / each file in the repo directory
metric = LinesCount(path_to_repo="G:\\GIT_Repos\\spring-framework", from_commit='8119659fb1e4ae6fabe8897c42ba7629fda07b21', to_commit='c2f7b6575156a7c3e049e17248acb6b580ba899f')
added_count = metric.count_added()
print(type(added_count))

# Get number of commits / each file in the repo directory
metric = CommitsCount(path_to_repo='G:\\GIT_Repos\\spring-framework',from_commit='8119659fb1e4ae6fabe8897c42ba7629fda07b21',to_commit='c2f7b6575156a7c3e049e17248acb6b580ba899f')
files = metric.count()


f = open("output.txt", "w")
# searching by key and value in dictionary, key means file name, value means actual commits number, etc, value retrieved by build in pydriller functions
for (key, value), (key2, value2), (key3, value3)  in zip(files.items(), added_count.items(), count.items()):
    f.write('Fisierul cu numele: ' + str(key) + ' are ' + str(value) + ' commits, ' + str(value2) + ' linii si ' +  str(value3) + ' autor(i): '  +  '\n')
f.close()
