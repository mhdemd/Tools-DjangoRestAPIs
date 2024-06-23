from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

@csrf_exempt
def products(request):
    if request.method == 'GET':
        products = Product.objects.all().values()
        return JsonResponse({"products":list(products)})
    elif request.method == 'POST':
        web_id = request.POST.get('web_id')
        name = request.POST.get('name')
        description = request.POST.get('description')
        product = Product(
            web_id = web_id,
            name = name,
            description = description,
        )
        try:
            product.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return JsonResponse(model_to_dict(product), status=201)
    