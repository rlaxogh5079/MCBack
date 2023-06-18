from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(('GET',))
def index(request: Request) -> Response:
    return Response({"message": "success"}, status=status.HTTP_200_OK)