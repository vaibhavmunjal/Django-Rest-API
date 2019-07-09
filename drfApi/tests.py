from django.test import TestCase

# Create your tests here.
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

# serialize (json) data
serializer = SnippetSerializer(snippet)
print(serializer.data)

# streaming the data (bytes)
content = JSONRenderer().render(serializer.data)
print(content)


import io

# stream to json
stream = io.BytesIO(content)
data = JSONParser().parse(stream)


serializer = SnippetSerializer(data=data)
# true
print(serializer.is_valid())

# ordered dict (deserialized)
print(serializer.validated_data)
serializer.save()


from .serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))