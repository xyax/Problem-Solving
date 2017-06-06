__author__ = 'xyax'
import sys
import operator

turma = dict()
for line in sys.stdin:
    aluno, nota = map(int, line.split())
    if not(aluno in turma.keys()):
        turma[aluno] = 0
    turma[aluno] += nota

out = sorted(turma.items(), key=operator.itemgetter(0))
out.sort(key=operator.itemgetter(1), reverse=True)

for o in out:
    print ' '.join(map(str, o))