from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics
from json import loads, dumps
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

# Django REST Framework
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# Vanilla REST
@csrf_exempt
def get_create_data(request):
    if request.method == 'GET':
        data = (Snippet.objects
                        .values('id',
                                'title',
                                'code',
                                'linenos',
                                'language',
                                'style'))
        data_list = list(data)
        return JsonResponse(data_list, safe=False)

    elif request.method == 'POST':
        data = loads(request.body)
        post_data = Snippet(
                            title=data.get('title', ''),
                            code=data.get('code', ''),
                            linenos=data.get('linenos', False),
                            language=data.get('language', ''),
                            style=data.get('style', ''))
        try:
            post_data.save()
            post_data = list(Snippet.objects
                                    .values('id',
                                            'title',
                                            'code',
                                            'linenos',
                                            'language',
                                            'style'))[-1]
        except:
            post_data={"status":"500"}
        return JsonResponse(post_data, safe=False)

    else:
        data = {"method-accept":["get", "post"]}
        return JsonResponse(data, safe=False)


@csrf_exempt
def retrieve_put_patch_delete(request, pk, method=["GET", "PUT", "PATCH", "DELETE"]):
    try:
        data = Snippet.objects.get(pk=pk)
    except:
        data = {"data": "Not exist"}
        return JsonResponse(data, safe=False)

    if request.method == "GET":
        data = model_to_dict(data)
        return JsonResponse(data, safe=False)

    elif request.method == "PUT":
        request_data = loads(request.body)
        data.title=request_data.get('title', '')
        data.code=request_data.get('code', '')
        data.linenos=request_data.get('linenos', False)
        data.language=request_data.get('language', '')
        data.style=request_data.get('style', '')
        data.save()
        data = model_to_dict(data)
        return JsonResponse(data, safe=False)

    elif request.method == "PATCH":
        request_data = loads(request.body)
        data.title=request_data.get('title', data.title)
        data.code=request_data.get('code', data.code)
        data.linenos=request_data.get('linenos', data.linenos)
        data.language=request_data.get('language', data.language)
        data.style=request_data.get('style', data.style)
        data.save()
        data = model_to_dict(data)
        return JsonResponse(data, safe=False)

    elif request.method == "DELETE":
        post_data = model_to_dict(data)
        data.delete()
        return JsonResponse(post_data, safe=False)


    else:
        data = {"request": "unknown!!!"}
        return JsonResponse(data, safe=False)

