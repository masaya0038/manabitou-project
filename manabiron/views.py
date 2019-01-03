from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Manabiron
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url="/manabito/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image']:
            manabiron = Manabiron()
            manabiron.title = request.POST['title']
            manabiron.body = request.POST['body']
            manabiron.image = request.FILES['image']
            manabiron.pub_date = timezone.datetime.now()
            manabiron.manabitoauthor = request.user
            manabiron.save()
            return redirect('/manabiron/' + str(manabiron.id))
        else:
            return render(request, 'manabiron/create.html',{'error':'All fields are required'})
    else:
        return render(request, 'manabiron/create.html')

def detail(request, manabiron_id):
    manabiron = get_object_or_404(Manabiron, pk=manabiron_id)
    return render(request, 'manabiron/detail.html',{'manabiron':manabiron})

def upvote(request, manabiron_id):
    if request.method == 'POST':
        manabiron = get_object_or_404(Manabiron, pk=manabiron_id)
        manabiron.votes_total += 1
        manabiron.save()
        return redirect('/manabiron/' + str(manabiron.id))

def manabironhome(request):
    manabirons = Manabiron.objects
    return render(request, 'manabiron/home.html',{'manabirons':manabirons})
