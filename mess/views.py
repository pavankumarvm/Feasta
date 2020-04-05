from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from mess.serializer import MessSerializer, MenuSerializer
from mess.models import Mess, Menu
from django.http import Http404
from rest_framework import viewsets
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'base.html'


class MessApiView(viewsets.ModelViewSet):
    """
    This view will return data about mess
    """
    queryset = Mess.objects
    serializer_class = MessSerializer

    def get(self, request):
        # method: GET
        # Return about Mess
        queryset = Mess.objects.all()
        serializer = MessSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        # method: POST
        # Add details about Mess
        parsers_class = (FileUploadParser,)

        file = request.FILES["profile_img"]
        print(file)
        serializer = MessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    This view will return data about a give mess
    ,update and delete the data
    """

    def retrieve(self, request, id):
        # Method: GET
        # Return data about particular mess
        queryset = self.get_detail(id)
        serializer = MessSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, id):
        # Method : PUT
        # Update a record
        queryset = self.get_detail(id)
        serializer = MessSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id):
        # Method: DELETE
        # Delete a record
        queryset = self.get_detail(id)
        queryset.delete()
        return Response(data={'status': 'Done'}, status=status.HTTP_204_NO_CONTENT)

    def get_detail(self, mess_id):
        try:
            return Mess.objects.get(id=mess_id)
        except Mess.DoesNotExist:
            raise Http404


class MenuApiView(viewsets.ModelViewSet):
    """
    This view will return menu from mess
    """
    queryset = Menu.objects
    serializer_class = MenuSerializer


    def get(self, request):
        # Method: GET
        # Return mess menu
        queryset = Menu.objects.all()
        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Method: POST
        # Add menu for a given mess
        print(request.data)
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # This view will return data about a particular menu
        # ,update and delete the data

    def get_data(self, request, menu_id):
        # Method: GET
        # @param: mess_id( !pass mess id to api endpoint)
        # @return: List all mess with that mess_id
        queryset = Menu.objects.filter(mess_id=menu_id)
        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, menu_id):
        # Method : PUT
        # Update a menu
        # @param: menu_id
        # @return:  Updated a record of menu
        queryset = self.get_detail(menu_id)
        serializer = MenuSerializer(queryset, data=request.data, partial=True)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, menu_id):
        print(menu_id)
        # Method: DELETE
        # Delete a record
        queryset = self.get_detail(menu_id)
        queryset.delete()
        return Response(data={'status': 'Done'}, status=status.HTTP_204_NO_CONTENT)

    def get_detail(self, menu_id):
        try:
            return Menu.objects.get(menu_id=menu_id)
        except Menu.DoesNotExist:
            raise Http404
