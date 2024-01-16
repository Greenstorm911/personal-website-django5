from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from home.models import Header, Home
from aboutme.models import AboutMe, Info
from skills.models import Skill, Skill_text
from comment.models import Comment
from certificate.models import Certificate_text, Certificate
import telebot
TOKEN = "6700654306:AAElY-6rjRUJ9WUWgH0esyutkiod_0YcUUY"
CHAT_ID = 1198382521

def index(request):
    context = {
                'Headers': Header.objects.all() ,
                'Home': Home.objects.all().last(),
                'aboutme': AboutMe.objects.all().last(),
                'info_texts': Info.objects.all(),
                'skills': Skill.objects.all(),
                'skill_texts': Skill_text.objects.all().last(),
                'certificate_text': Certificate_text.objects.all().last(),
                'certificates': Certificate.objects.all()

               }
    if request.method == 'POST':
        comment = Comment(name=request.POST.get('name'), email=request.POST.get('email'), comment=request.POST.get('comment'))
        comment.save()
        bot = telebot.TeleBot(TOKEN)
        bot.send_message(CHAT_ID, f"name: {request.POST.get('name')}\nemail: {request.POST.get('email')}\ncomment: {request.POST.get('comment')}")
        return redirect('/')
    return render(request, 'index/index-rtl.html', context)

