import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        # charge = stripe.Charge.create(amount = 500,currency ='inr',description = 'Payment Gateway',source = request.POST['stripeToken'])
        return render(request,'charge.html',locals())
        # return redirect('charge',locals())