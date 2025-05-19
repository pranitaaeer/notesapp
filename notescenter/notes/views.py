from django.shortcuts import render,redirect,get_object_or_404
from .forms import NoteForm
from .models import Note
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def note_list(request):
    if request.method=='POST':
        notes=Note.objects.filter(user=request.user)
        # notes=Note.objects.all()
        return render(request,'notes/note_list.html',{'notes':notes})
    else:
        notes=Note.objects.filter(user=request.user)
        # notes=Note.objects.all()
        return render(request,'notes/note_list.html',{'notes':notes})
        
@login_required    
def create_note(request):
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            note=form.save(commit=False)
            note.user=request.user
            note.save()
            return redirect('note_list') 
    else:
        form=NoteForm()
        return render(request,'notes/create_note.html',{'form':form})    

@login_required
def edit_note(request,note_id):
    note=get_object_or_404(Note,pk=note_id,user=request.user)
    if request.method=='POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            note=form.save(commit=False)
            note.user=request.user
            note.save()
            return redirect('note_list') 
    else:
        form=NoteForm()
        return render(request,'notes/create_note.html',{'form':form})  

@login_required
def note_delete(request,note_id):
   note=get_object_or_404(Note,pk=note_id,user=request.user)
   
   if request.method=="POST":
      note.delete()
      return redirect('note_list')
   return render(request,'notes/note_confirm_delete.html',{'note':note})
