from django.shortcuts import render
from django.http import HttpResponse,request

# Create your views here.

pupils = [
    {'id':1,'name': 'Inomjon Qurbonov',  1:{2,4,1}, 2:{4,10,5}, 3:{5,4}, 'jami': 37},
    {'id':2,'name': 'MuhammadYusuf Abdullayev', 1:{3,5,2}, 2:{5,10,4}, 3:{5,3}, 'jami': 36},
    {'id':3,'name': 'Shoxruxbek Turdaliyev', 1:{3,0,1},2:{3,10,3},3:{5,3},'jami': 29},
    {'id':4,'name': 'Samariddin Baxtiyorov', 1:{2,5,1},2:{4,10,5},3:{5,4},'jami': 37},
    {'id':5,'name': 'Ozodbek Axrorov', 1:{3,5,2},2:{5,10,4},3:{5,4},'jami': 40},
    {'id':6,'name': 'Javohir Otaboyev', 1:{0,4,0},2:{4,10,5},3:{5,4},'jami': 35},
    {'id':7,'name': 'Mubina Nusratullayeva', 1:{2,4,1},2:{1,10,2},3:{4,3},'jami': 31},
    {'id':8,'name': 'Ruslan Mamatanov', 1:{2,4,1},2:{5,10,4},3:{4,5},'jami': 35 },
    {'id':9,'name': 'Javlon Jorayev', 1:{2,4,1},2:{4,10,5},3:{5,4},'jami': 31},
    {'id':10,'name': 'Arabboy Yunusov', 1:{2,4,1},2:{5,10,4},3:{4,5},'jami': 36}
]




def pupil(request):
    global pupils
    return render(request,'list.html',context={'pupils': pupils})


def home(request):
    return render(request,'home.html')


def themes(request):
    return render(request,'themes.html')


def show_pupil(request,pk):
    global pupils
    return render(request,'baholar.html',context={'baho':pupils[pk-1]})
