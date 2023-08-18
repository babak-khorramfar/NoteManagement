from django.shortcuts import get_object_or_404, render, redirect
from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.all()
    context = {
        'notes': notes,
        
    }
    return render(request, 'notes/noteManager.html', context)

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    context = {
        'form': form,
    }

    return render(request, 'notes/noteManager.html', context)

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    context = {
        'form': form,
    }

    return render(request, 'notes/noteManager.html', context)