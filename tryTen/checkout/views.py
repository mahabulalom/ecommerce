from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

secretKey = settings.STRIPE_SECRET_KEY
stripe.api_key = "sk_test_j8bqZ2xihn5zrfchqKchedM5"

# Create your views here.
@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY 
	if request.method =='POST':
		token = request.POST['stripeToken']
       
	context = {'publishKey': publishKey}
	template = 'checkout.html'
	return render(request,template,context)

	
	
	