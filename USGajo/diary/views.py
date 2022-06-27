from django.shortcuts import render, redirect
from .models import Diary
# from .forms import DiaryForm

# Create your views here.
def diaryList(request):
    diarylist = Diary.objects.all()
    return render(request, 'diary/diaryList.html', {'diarylist': diarylist})

#write diary
def diaryWrite(request):
    if request.method == 'POST':
        date = request.POST['date']
        weather = request.POST['weather']
        contents = request.POST['contents']
        mainphoto = request.FILES.get('mainphoto')
        diary = Diary.objects.create(date=date, weather=weather, contents=contents,
                                     mainphoto=mainphoto)
        diary.save()
        return redirect('diary:diaryList')
    return render(request, 'diary/diaryWrite.html')



#see the detail post of diary
def diaryDetail(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    diary = Diary.objects.get(pk=pk)
    context = {'diary': diary}
    return render(request, 'diary/diaryDetail.html', context)

def diaryDelete(request, pk):
    diary = Diary.objects.get(pk=pk)
    diary.delete()
    return redirect('diary:diaryList')

def diaryUpdate(request, pk):
    diary = Diary.objects.get(pk=pk)
    if request.method == "POST":
        diary.date = request.POST['date']
        diary.weather = request.POST['weather']
        diary.contents = request.POST['contents']
        diary.mainphoto = request.FILES.get('mainphoto')
        diary.save()
        return redirect('diary:diaryList')
    else:
        diary = Diary()
        return render(request, 'diary/diaryUpdate.html', {'diary':diary} )


