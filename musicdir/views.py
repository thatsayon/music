from django.shortcuts import render
from first_app.models import MusicModel, AlbumModel

def home(request):
    mdata = MusicModel.objects.all()
    adata = AlbumModel.objects.all()
    
    return render(request, 'home.html', {'mdata': mdata, 'adata': adata})