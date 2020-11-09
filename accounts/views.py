from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import MessOwnerSerializer, ConsumerSerializer, FeastaUserSerializer
from .forms import MessOwnerSignUpForm, ConsumerSignUpForm
from .models import FeastaUser, MessOwner, Consumer
from django.urls import reverse_lazy
from rest_framework import permissions
# Create your views here.

# class MessOwnerSignUpView(CreateView):
#     model =  MessOwner
#     form_class = MessOwnerSignUpForm
#     success_url = reverse_lazy('consumer')
#     template_name = 'registration/mess.html'

# class ConsumerSignUpView(CreateView):
#     model = Consumer
#     form_class = ConsumerSignUpForm
#     success_url = reverse_lazy('messowner')
#     template_name = 'registration/signup.html'


class HomePageView(TemplateView):
    template_name = 'base.html'
    
class FeastaUserViewSet(viewsets.ModelViewSet):
    queryset = FeastaUser.objects.all()
    serializer_class = FeastaUserSerializer

    """
        This view will return data about all Users
    """

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            FeastaUser.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status' : 'Bad Request',
            'message' : 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


    def get(self,request):
        # method: GET
        # Return about FeastaUsers
        queryset = FeastaUser.objects.all()
        serializer = FeastaUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        # method: POST
        # Add Details about FeastaUsers

        serializer = FeastaUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, username):
        # Method: GET
        # Return data about prticular FeastaUser
        queryset = self.get_detail(username)
        serializer = FeastaUserSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, username):
        # Method : PUT
        # Update a particular FeastaUser detail
        queryset = self.get_detail(username)
        serializer = FeastaUserSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, username):
        # Method: DELETE
        # Delete a record
        queryset = self.get_detail(username)
        queryset.delete()
        return Response(data={'status': 'Done'}, status=status.HTTP_204_NO_CONTENT)

    def get_detail(self, user_username):
        try:
            print(user_username)
            return FeastaUser.objects.get(username=user_username)
        except FeastaUser.DoesNotExist:
            raise Http404


class MessOwnerViewSet(viewsets.ModelViewSet):
    queryset = MessOwner.objects.all()
    serializer_class = MessOwnerSerializer

    """
        This view will return data about all Mess Owners
    """

    def get(self,request):
        # method: GET
        # Return about MessOwners
        queryset = MessOwner.objects.all()
        serializer = MessOwnerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        # method: POST
        # Add Details about MessOwners

        serializer = MessOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, user):
        # Method: GET
        # Return data about prticular Messowner
        queryset = self.get_detail(user)
        serializer = MessOwnerSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, user):
        # Method : PUT
        # Update a particular Messowner detail
        queryset = self.get_detail(user)
        serializer = MessOwnerSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, user):
        # Method: DELETE
        # Delete a record

        # Uncomment this if you are deleting messowner account 
        # to delete FeastaUser account simultaneously.
        # 
        # parent = FeastaUser.objects.get(id=user)
        queryset.delete()
        queryset = self.get_detail(user)
        # parent.delete()
        return Response(data={'status': 'Done'}, status=status.HTTP_204_NO_CONTENT)

    def get_detail(self, messowner):
        try:
            print(messowner)
            return MessOwner.objects.get(user=messowner)
        except MessOwner.DoesNotExist:
            raise Http404


class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer

    """
        This view will return data about all Consumers
    """
    def get(self,request):
        # method: GET
        # Return about Consumer
        queryset = Consumer.objects.all()
        serializer = ConsumerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        # method: POST
        # Add Details about Consumer

        serializer = ConsumerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, user):
        # Method: GET
        # Return data about particular mess
        queryset = self.get_detail(user)
        serializer = ConsumerSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, user):
        # Method : PUT
        # Update a record
        queryset = self.get_detail(user)
        serializer = ConsumerSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, user):
        # Method: DELETE
        # Delete a record
        # Uncomment this if you are deleting consumer account 
        # to delete FeastaUser account simultaneously.
        # 
        # parent = FeastaUser.objects.get(id=user)
        queryset = self.get_detail(user)
        queryset.delete()
        # parent.delete()
        return Response(data={'status': 'Done'}, status=status.HTTP_204_NO_CONTENT)

    def get_detail(self, consumer):
        try:
            return Consumer.objects.get(user=consumer)
        except Consumer.DoesNotExist:
            raise Http404
