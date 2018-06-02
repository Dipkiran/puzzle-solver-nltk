from django.shortcuts import render
import nltk
from nltk.corpus import wordnet
# Create your views here.
def page(request):
    query = request.GET.get("q")
    if query:
        puzzles= []
        puzzle_letters = nltk.FreqDist(query)
        wordlist = nltk.corpus.words.words()
        for i in range(1,len(query)):
            puzzle = [w for w in wordlist if len(w) == i+1 and nltk.FreqDist(w) <= puzzle_letters]
            print(puzzle)
            puzzles.append(puzzle)
        context = {
                'puzzle' : puzzles,
        }
        return render(request,"puzzle.html",context)
    return render(request,"hello.html")
