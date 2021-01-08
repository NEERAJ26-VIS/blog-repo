from django.shortcuts import render

# Create your views here.
def view1(request):
    myname="neeraj"
    fovplayer="virat"
    fovbird="parrot"
    fovsubject="humanity"
    d={'name':myname,'player':fovplayer,'subject':fovsubject,'bird':fovbird}
    return render(request,'staticapp1/1.html',d)