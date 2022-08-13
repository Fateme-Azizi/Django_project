from django.views.generic import ListView
from django.http import HttpResponse
from .models import DimCompany, FactStatement

# Create your views here.


def home(request):
    return HttpResponse('<h1>hello world</h1>')


class PostListView(ListView):
    pass
    # model = Post
    # template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    # context_object_name = 'posts'
    # ordering = ['-date_posted']
    # paginate_by = 3
