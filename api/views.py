from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
import time

from .serializers import NumberSerializer
from .utils import NumberTooLargeError, number_to_english

class NumberToEnglishAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Convert number to English",
        responses={200: "Number converted successfully", 400: "Invalid number format or too large"},
        query_serializer=NumberSerializer
    )
    def get(self, request):
        serializer = NumberSerializer(data=request.GET)
        if serializer.is_valid():
            try:
                num = serializer.validated_data["number"]
                return Response({"status": "ok", "num_in_english": number_to_english(num)}, status=status.HTTP_200_OK)
            except NumberTooLargeError:
                return Response({"status": "error", "message": "Number is too large to process"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "error", "message": "Invalid number format"}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Convert number to English",
        responses={200: "Number converted successfully", 400: "Invalid number format or too large"},
        request_body=NumberSerializer
    )
    def post(self, request):
        serializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            try:
                num = serializer.validated_data["number"]
                time.sleep(5)
                return Response({"status": "ok", "num_in_english": number_to_english(num)}, status=status.HTTP_200_OK)
            except NumberTooLargeError:
                return Response({"status": "error", "message": "Number is too large to process"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "error", "message": "Invalid number format"}, status=status.HTTP_400_BAD_REQUEST)