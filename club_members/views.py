from django.contrib.auth.decorators import user_passes_test
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Location, News


def index(request):
    return render(request, 'general/about_club.html')


def map_view(request, location_id):
    # Получаем местоположение по ID
    location = get_object_or_404(Location, pk=location_id)

    # Передаем данные местоположения в шаблон
    return render(request, 'buy_crayfish/map.html', {'location': location})


def locations_list(request):
    locations = Location.objects.all()
    return render(request, 'buy_crayfish/locations.html', {'locations': locations})


def news_list(request):
    news = News.objects.all()
    return render(request, 'general/news_list.html', {'news': news})


def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'general/news.html', {'news_item': news_item})


def documents_list(request):
    documents = Document.objects.all()
    return render(request, 'general/documents_list.html', {'documents': documents})


from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document


@user_passes_test(lambda u: u.is_staff)
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.pdf_data = request.FILES['pdf_file'].read()
            document.save()
            return redirect('documents_list')  # Перенаправление на список документов
    else:
        form = DocumentForm()

    return render(request, 'general/upload_document.html', {'form': form})


def download_document(request, slug):
    document = get_object_or_404(Document, slug=slug)
    response = HttpResponse(document.pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s"' % document.title
    return response


def export_news_json(request):
    news_items = serialize('json', News.objects.all())
    return HttpResponse(news_items, content_type="application/json")


def export_news_xml(request):
    news_items = serialize('xml', News.objects.all())
    return HttpResponse(news_items, content_type="application/xml")
