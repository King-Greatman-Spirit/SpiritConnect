from django.shortcuts import render
from .models import Gallery
# from .models import Organization
from django.core.paginator import Paginator

# Create your views here.
def gallery(request):
    # organization = Organization.objects.get(id=1, is_church=True)
    gallery = Gallery.objects.all()

    # Set Up Pagination
    p = Paginator(gallery, 3)
    page = request.GET.get('page')
    pictures = p.get_page(page)
    nums = "a" * pictures.paginator.num_pages

    context = {
        # 'organization': organization,
        'gallery': gallery,
        'pictures': pictures,
        'nums': nums,
    }

    return render(request, 'gallery/gallery.html', context)



def gallery_detail(request, gallery_id):
    gallery_detail = Gallery.objects.get(id=gallery_id)

    context = {
        'gallery_detail': gallery_detail,
    }

    return render(request, 'gallery/gallery_detail.html', context)
