from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Dictionary


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


def words_list_db(request):
    dictionary = Dictionary.objects.all().values()
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


def adding_words_db(request):
    if request.method == 'GET':
        return render(request, 'adding_words.html')
    else:
        data = request.POST
        original = data['original']
        translate = data['translate']
        comment = data['comment']
        new_word = Dictionary()
        new_word.add_new_word(original, translate, comment)
        print(original, translate)
        word = Dictionary.objects.filter(english='lift').first()
        print(word.russian)
        url = reverse('home')
        return HttpResponseRedirect(url)


def edit_words_db(request, word_id):
    word = Dictionary.objects.get(id=word_id)
    if request.method == 'GET':
        context = {
            'word': word
        }
        return render(request, 'editing.html', context=context)
    else:
        data = request.POST
        print(dict(data))
        word.make_changes(dict(data))
        # word.english = data['word1']
        # word.russian = data['word2']
        # word.comments = data['comment']
        word.save()
        url = reverse('home')
        return HttpResponseRedirect(url)