from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, 'home.html')


def words_list(request):
    file = open("dict_file.txt", "r", encoding='utf-8').read().splitlines()
    dictionary = {}
    for line in file:
        word1, word2 = line.split("-")
        dictionary[word1] = word2
    # context = {"word1": words1, "word2": words2}
    context = {"dictionary": dictionary}
    return render(request, 'words.html', context=context)


def adding_words(request):
    if request.method == "GET":
        return render(request, 'adding_words.html')
    else:
        data = request.POST
        original = data['word1']
        translate = data['word2']
        print(original, translate)
        with open("dict_file.txt", "a", encoding='utf-8') as f:
            f.write(original + '-' + translate + "\n")
        url = reverse('home')
        return HttpResponseRedirect(url)