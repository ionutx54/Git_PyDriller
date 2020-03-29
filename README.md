# Git_PyDriller
retrieving data from git repos using pydriller lib.

# Materie: CES
# Subpunctele A2 si A3

	# In cadrul acestor 2 subpuncte, am folosit libraria de Python PyDriller.
	# Referinta si documentatia se afla la adresa: https://readthedocs.org/projects/pydriller/downloads/pdf/latest/
	# Metodele folosite sunt: ContributorsCount, LinesCount si CommitsCount.
	# Sunt similare, ca argumente iau folderul in care se afla repo de git, hash-ul primul commit si al ultimului din pct.
	# Pentru a afla Hashul commit-urilor de inceput si sfarsit trebuie apelata comanda: git log --format=%H | tail -
	# Metodele returneaza un obiect de tip dictionar: <class 'dict'>
	# Dupa ce am facut rost de date, le-am scris intr-un fisier text
	# Scrierea facuta cu ajutorul unui tuplu de cheie, valoare, unde cheia reprezinta numele fisierului si valoarea ceea ce a returnat functia respectiva, de ex nr de linii:



	# Analiza s-a facut pe repo-ul urmator: git clone https://github.com/spring-projects/spring-framework.git	
