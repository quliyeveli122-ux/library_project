from rest_framework.views import APIView, Response, status
from rest_framework.generics import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from django.core.exceptions import ValidationError, FieldError

from .models import Book
from .serializer import BookSerializer


class BookCreateAPIView(APIView):
    @swagger_auto_schema(request_body=BookSerializer)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Book created successfully!"}, 
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {"message": "Invalid data. Please check the fields!"}, 
            status=status.HTTP_400_BAD_REQUEST
        )


class BookListAPIView(APIView):
    def get(self, request):
        book_list = Book.objects.all()

        author_id = request.query_params.get("author_id")
        is_available = request.query_params.get("is_available")
        price_min = request.query_params.get("price_min")
        price_max = request.query_params.get("price_max")
        year = request.query_params.get("year")
        search = request.query_params.get("search")
        order_by = request.query_params.get("ordering")
        search = request.query_params.get("search")

        try:

            if author_id:
                book_list = book_list.filter(author_id=author_id)
            if is_available:
                book_list = book_list.filter(is_available=is_available)
            if price_min:
                book_list = book_list.filter(price__gte=price_min)
            if price_max:
                book_list = book_list.filter(price__lte=price_max)
            if year:
                book_list = book_list.filter(published_date__year=year)
            if search:
                book_list = book_list.filter(title__icontains=search)
            if order_by:
                book_list = book_list.order_by(order_by)
            if search:
                book_list = book_list.order_by(search)

        except (ValueError, ValidationError, FieldError):
            return Response(
                {"error": "Invalid query parameters provided for filtering or ordering!"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = BookSerializer(book_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetailAPIView(APIView):
    @swagger_auto_schema(operation_description="Retrieve a specific book by their ID.")
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BookDeleteAPIView(APIView):
    @swagger_auto_schema(operation_description="Delete a specific book by their ID.")
    def delete(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return Response(
            {"message": "Book deleted successfully!"}, 
            status=status.HTTP_200_OK
        )


class BookUpdateAPIView(APIView):
    @swagger_auto_schema(
        request_body=BookSerializer, 
        operation_description="Update an existing book's information by their ID."
    )
    def put(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Book updated successfully!"}, 
                status=status.HTTP_200_OK
            )
        
        return Response(
            {"message": "Update failed. Please check the provided data!"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
