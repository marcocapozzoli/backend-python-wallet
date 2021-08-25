from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request):
    return Response({
        'link1': 'Link1',
        'link2': 'Link2',
    })
    
# List

# Detail