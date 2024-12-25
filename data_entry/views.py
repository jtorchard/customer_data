# Create your views here.
from django.http import HttpResponse
from django.views import generic

from .models import Customer


class IndexView(generic.ListView):
    template_name = "data_entry/index.html"
    context_object_name = "customer_list"

    def get_queryset(self):
        """Return the last five published customers."""
        return Customer.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Customer
    template_name = "data_entry/detail.html"


def vote(request, customer_id):
    return HttpResponse("You're voting on customer %s." % customer_id)
