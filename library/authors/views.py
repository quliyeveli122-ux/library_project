from rest_framework.views import APIView, Response, status
from rest_framework.generics import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from django.core.exceptions import FieldError

from .models import Author
from .serializer import AuthorSerializer


class AuthorCreateAPIView(APIView):
    @swagger_auto_schema(request_body=AuthorSerializer)
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Author created successfully!"}, 
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {"message": "Invalid data. Please check the fields!"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    

class AuthorListAPIView(APIView):
    def get(self, request):
        author_list = Author.objects.all()

        country = request.query_params.get("country")
        birth_year = request.query_params.get("birth_year")
        order_by = request.query_params.get("ordering")

        try:

            if country:
                author_list = author_list.filter(country=country)
            if birth_year:
                author_list = author_list.filter(birth_date__year=birth_year)
            if order_by:
                author_list = author_list.order_by(order_by)

        except (ValueError, FieldError):
            return Response(
                {"error": "Invalid query parameters provided for filtering or ordering!"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AuthorSerializer(author_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AuthorDetailAPIView(APIView):
    @swagger_auto_schema(operation_description="Retrieve a specific author by their ID.")
    def get(self, request, author_id):
        author = get_object_or_404(Author, pk=author_id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AuthorDeleteAPIView(APIView):
    @swagger_auto_schema(operation_description="Delete a specific author by their ID.")
    def delete(self, request, author_id):
        author = get_object_or_404(Author, pk=author_id)
        author.delete()
        return Response(
            {"message": "Author deleted successfully!"}, 
            status=status.HTTP_200_OK
        )
    

class AuthorUpdateAPIView(APIView):
    @swagger_auto_schema(
        request_body=AuthorSerializer, 
        operation_description="Update an existing author's information by their ID."
    )
    def put(self, request, author_id):
        author = get_object_or_404(Author, pk=author_id)
        serializer = AuthorSerializer(author, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Author updated successfully!"}, 
                status=status.HTTP_200_OK
            )
        
        return Response(
            {"message": "Update failed. Please check the provided data!"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
