from django.shortcuts import render
from .models import Organization_Worker
from django.core.paginator import Paginator
# from .models import Organization

# Create your views here.

def organization_worker(request):
    # organization = Organization.objects.get(id=1, is_church=True)
    organization_worker = Organization_Worker.objects.all()

    # Set Up Pagination
    p = Paginator(organization_worker, 1)
    page = request.GET.get('page')
    staffs = p.get_page(page)
    nums = "a" * staffs.paginator.num_pages

    context = {
        # 'organization': organization,
        'organization_worker': organization_worker,
        'staffs': staffs,
        'nums': nums,
    }

    return render(request, 'team/meet_our_team.html', context)



def staff_detail(request, organization_worker_id):
    staff_detail = Organization_Worker.objects.get(id=organization_worker_id)

    context = {
        'staff_detail': staff_detail,
    }

    return render(request, 'team/staff_detail.html', context)
