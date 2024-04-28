from .models import Organization

def church_link(request):
    church = Organization.objects.get(is_church=True)
    return dict(church=church)
