from django.shortcuts import render
from organization.models import Organization, OrganizationOverview
from organization_worker.models import Organization_Worker
from blog.models import Article, Author, Paragraph
from gallery.models import Gallery


def home(request):
    organization = Organization.objects.get(id=1, is_church=True)
    organization_overview = OrganizationOverview.objects.get(organization=organization)
    organization_worker = Organization_Worker.objects.filter(organization=organization)
    gallery = Gallery.objects.filter(organization=organization)


    articles = Article.objects.all().order_by('-id')[:3]
    dispaly_paragraph = {}
    for article in articles:
        for paragraph in Paragraph.objects.filter(article=article):
            dispaly_paragraph[article.id] = ' '.join(paragraph.paragraph_content.split(' ')[:18]) + '...'
            break


    context = {
        'organization': organization,
        'organization_overview': organization_overview,
        'organization_worker': organization_worker,
        'articles': articles,
        'dispaly_paragraph': dispaly_paragraph,
        'gallery': gallery,
        'navbar': home,
    }

    return render(request, 'home.html', context)
