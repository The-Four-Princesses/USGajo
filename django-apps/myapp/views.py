from cgitb import html
from hashlib import new
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import random

nextid = 4
topics = [
    {'id':1, 'title':'블로그 소개', 'body':'저희는 2022년도 SW 해외프로그램에 참가하게 된 \"사공주 가보자고\"입니다. 방문해주셔서 감사해요><!'},
    {'id':2, 'title':'SW 해외프로그램 소개', 'body':'퍼듀대 K-SW 가을학기 : ---\n USC SSP 프로그램 : ---'},
    {'id':3, 'title':'퍼듀대 : K_SW 가을학기', 'body':'퍼듀대 K-SW 가을학기 : ---+포스터 홍보 자료 등'},
    {'id':4, 'title':'프로그램 소개', 'body':'세부 모집 내용 및 구비 서류 관련'},
    {'id':5, 'title':'사진첩', 'body':'사진 업로드..기능 추가'},
    {'id':6, 'title':'희원\'s 일기', 'body':'안녕하세요! 희원이예요🙆‍♀️ 지금부터 제 이야기를 시작할께요!'},
    {'id':7, 'title':'한비\'s 일기', 'body':'안녕하세요! 한비예요🙆‍♀️ 지금부터 제 이야기를 시작할께요!'},
    {'id':8, 'title':'USC : SSP', 'body':'USC SSP 프로그램 : ----+포스터 홍보 자료 등'},
    {'id':9, 'title':'프로그램 소개', 'body':'세부 모집 내용 및 구비 서류 관련'},
    {'id':10, 'title':'사진첩', 'body':'사진 업로드..기능 추가'},
    {'id':11, 'title':'혜림\'s 일기', 'body':'안녕하세요! 혜림이예요🙆‍♀️ 지금부터 제 이야기를 시작할께요!'},
    {'id':12, 'title':'수정\'s 일기', 'body':'안녕하세요! 수정이예요🙆‍♀️ 지금부터 제 이야기를 시작할께요!'}
]

def htmltemplate(articleTag, id=None):
    global topics
    contextui = ''
    if id != None:
        contextui = f'''
            <li><a href="/update/{id}">update</a></li>
            <li>
                <form action="/delete/" method="POST">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
        '''
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">My profile</a></h1>
            <ol>
                {ol}
            </ol>
            {articleTag}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextui}
            </ul>
    </body>
    </html>
    '''

def index(request):
    article='''
    <h2>hello, guest thank for visiting my site!</h2>
    Let's start to travel!
    '''
    return HttpResponse(htmltemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id']==int(id):
            article=f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(htmltemplate(article, id))

@csrf_exempt
def create(request):
    global nextid
    if request.method == 'GET':
        article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(htmltemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextid, "title":title, "body":body}
        topics.append(newTopic)
        url = '/read/'+str(nextid)
        nextid = nextid+1
        return redirect(url)

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id=request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
    return redirect('/')

@csrf_exempt
def update(request, id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic['title'],
                    "body":topic['body']
                }    
        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
                <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(htmltemplate(article, id))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')