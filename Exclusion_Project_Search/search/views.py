from django.shortcuts import render
from django.db.models import Q, Case, When, Value, IntegerField
from django.core.paginator import Paginator
from .models import MainExclusions

def search_view(request):
    name_query = request.GET.get('name', '').strip()
    npi_query = request.GET.get('npi', '').strip()
    results = []
    total_count = 0

    if name_query or npi_query:
        filters = Q()
        if name_query:
            filters |= Q(last_name__icontains=name_query) | Q(first_name__icontains=name_query) | Q(business_name__icontains=name_query)
        if npi_query:
            filters |= Q(npi__icontains=npi_query)

        all_results = MainExclusions.objects.filter(filters).distinct()

        if name_query:
            all_results = all_results.annotate(
                # Which field matched: last_name=0, first_name=1, business_name=2
                match_field_rank=Case(
                    When(last_name__icontains=name_query, then=Value(0)),
                    When(first_name__icontains=name_query, then=Value(1)),
                    default=Value(2),
                    output_field=IntegerField()
                ),
                # How closely it matched: exact=0, starts with=1, contains=2
                match_quality_rank=Case(
                    When(last_name__iexact=name_query, then=Value(0)),
                    When(first_name__iexact=name_query, then=Value(0)),
                    When(last_name__istartswith=name_query, then=Value(1)),
                    When(first_name__istartswith=name_query, then=Value(1)),
                    default=Value(2),
                    output_field=IntegerField()
                )
            ).order_by('match_field_rank', 'match_quality_rank', 'last_name', 'first_name')
        else:
            all_results = all_results.order_by('last_name', 'first_name')

        total_count = all_results.count()

        paginator = Paginator(all_results, 100)
        page_number = request.GET.get('page', 1)
        results = paginator.get_page(page_number)

    return render(request, 'search/search.html', {
        'name_query': name_query,
        'npi_query': npi_query,
        'results': results,
        'total_count': total_count,
    })