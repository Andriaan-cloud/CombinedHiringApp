from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Response, Document
from .forms import DocumentForm, ProfileForm, UserRegisterForm
import fileinput
import sys
from subprocess import run, PIPE
import shutil
import zipfile
# Create your views here.


def job_requirement_survey(request):
    #context = {
        #'posts': Post.objects.all()
    #}
    #return render(request, 'blog/home.html',{'title': 'Survey'}) #context)

    context = {

                 "age": 67

              }
    return render(request, 'j_home.html', context)#{'title': 'Survey'}, context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def index(request):
    message = ''
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            cv_ = Document(docfile=request.FILES['CV'])
            cv_.save()
            id_ = Document(docfile=request.FILES['ID'])
            id_.save()
            trans = Document(docfile=request.FILES['Transcript'])
            trans.save()
            vid = Document(docfile=request.FILES['Video'])
            vid.save()

            # Redirect to the document list after POST
            return redirect('home')
        else:
            message = 'The form is not valid. Fix the following error:'
        shutil.make_archive('user_archive', 'zip', 'C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/text files/documents')
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)


def home(request):
    if request.method == "POST":
        global responsibilities
        responsibilities = request.POST['R']
        global t_skills
        t_skills = request.POST['T']
        global s_skills
        s_skills = request.POST['S']
        global out
        print(responsibilities, t_skills, s_skills)
        t = 'C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/text files/recruit/Sample CV text.txt'
        for lines in fileinput.FileInput(t, inplace=1):
            if 'Responsibilities:' in lines:
                lines = lines[:17]
                lines = lines.replace(lines, lines + '\n' + responsibilities)
            print(lines, end='')
        for lines in fileinput.FileInput(t, inplace=1):
            if 'Technical skills:' in lines:
                lines = lines[:17]
                lines = lines.replace(lines, lines + '\n' + t_skills)
            print(lines, end='')
        for lines in fileinput.FileInput(t, inplace=1):
            if 'Soft skills:' in lines:
                lines = lines[:12]
                lines = lines.replace(lines, lines + '\n' + s_skills)
            print(lines, end='')
        ins = Response(responsibilities=responsibilities, tech_skills=t_skills, soft_skills=s_skills)
        ins.save()
        out = run([sys.executable, 'C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/comparisons.py'], shell=False, stdout=PIPE)
        return redirect('success')
    print("The data has been written to the db")
    return render(request, 'home.html')


def success(request):
    if request.method == "POST":
        original = r'C:\Users\Lenovo-User\PycharmProjects\newApp\hiringApp\recruit\text files\recruit\Sample CV text.txt'
        target = r'C:\Users\Lenovo-User\PycharmProjects\newApp\hiringApp\recruit\responses\Sample CV text.txt'
        shutil.copyfile(original, target)
        my_zip = zipfile.ZipFile('report.zip', 'w')
        my_zip.write('C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/responses/Sample CV text.txt')
        my_zip.write('C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/responses/response.txt')
        my_zip.close()
        ssw = open('C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/text files/recruit/Sample CV text.txt', 'w+')
        liner = 'Responsibilities:' + '\n' + '\n' 'Technical skills:' + '\n' + '\n' 'Soft skills:'
        ssw.write(liner)
        return redirect('profile')
    return render(request, 'success.html', {'result': out.stdout.decode('utf-8')})


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            print('Data Saved')
            return redirect('login')

    user_form = ProfileForm()
    return render(request, 'profile.html', {'form': user_form})


