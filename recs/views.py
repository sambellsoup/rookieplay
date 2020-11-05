from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Greeting, Document, Topic, Entry
from .forms import TopicForm, EntryForm

# recommendation packages
from .text_processing import document_to_text, compile_document_text, text_to_bagofwords, join_and_condense, vectorize_text, recommend_100, format_recommendations, top_100_categories, freq, viz_data, make_viz

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from rake_nltk import Rake
from tika import parser
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from pathlib import Path

# Job Search API
from serpapi import GoogleSearchResults

from time import time

# Create your views here.

def upload(request):
    context = {}
    if request.method == 'POST':
        """File handling"""
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        data_folder = Path("C:/Users/sambe/Projects/Cover_Letter_Analysis/data/documents/")
        document_path = str(data_folder) + '\\'+  uploaded_file.name
        """Recommendation functions"""
        resume_text = document_to_text(document_path)
        basic_documentdf = compile_document_text(resume_text)
        verbose_documentdf = text_to_bagofwords(basic_documentdf)
        recommend_df = join_and_condense(verbose_documentdf)
        cosine_sim = vectorize_text(recommend_df)
        recommended_jobs = recommend_100(recommend_df, cosine_sim)
        final_jobs = format_recommendations(recommended_jobs)


        context['recommendations'] = final_jobs
        context['recommendation_0'] = final_jobs[0]
        # final_jobs.pop(0)
        context['recommendation_1'] = final_jobs[1]
        # final_jobs.pop(0)
        context['recommendation_2'] = final_jobs[2]

    if request.is_ajax():
        text = request.GET.get('button_text')
        test = 'test'
        print()
        print(text)
        print()
        print('test')


   # if request.method == 'GET':
        # text = request.GET.get('button_text')
        # print()
        # print(text)
        # print()



        # final_jobs.pop(0)
    # if thumbs up button clicked:
        # scrape jobs related to that job title
        # put jobs in dictionary with keys of
        # job title, company, link to job application, description, date posted, location, full-time/part-time, remote?
    return render(request, 'rookieplays/upload.html', context)

# def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, "recs/index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "recs/db.html", {"greetings": greetings})

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'recs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entires."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'recs/topic.html', context)

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submittedl create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('recs:topics'))

    context = {'form': form}
    return render(request, 'recs/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; create a blank form.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('recs:topic', args=[topic_id]))

    context = {'topic': topic, 'form':form}
    return render(request, 'recs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #Initial request; pre=fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('recs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'recs/edit_entry.html', context)
