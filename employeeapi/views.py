from django.conf import settings
from .models import Employee
from .serializers import EmployeeSerializer
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView, RetrieveAPIView,UpdateAPIView
from rest_framework.views import APIView
from django.http import  JsonResponse,HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

def test(requests,emp_type):
    print("user"+"*"*10)
    print(requests.user)
    return HttpResponse(emp_type)

# Create your views here.
class empListAPIView(ListAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
'''
class empcreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
'''
class empcreateAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,requests):
        return JsonResponse("you are authenticated",safe=False)
    def post(self,requests):
        emp_code=requests.POST.get("emp_code")
        fullname=requests.POST.get("fullname")
        emp_type=requests.POST.get("emp_type")
        mobile=requests.POST.get("mobile")
        uname=requests.POST.get("uname")
        user=User.objects.get(username=uname)
        Employee(emp_code=emp_code,fullname=fullname,emp_type=emp_type,mobile=mobile,uname=user).save()
        token = Token.objects.get_or_create(user=user)
        print(token[0].key)
        return JsonResponse("your token is "+token[0].key,safe=False)

class empupdateAPIView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """This endpoint allows for updating a specific employee """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class empdeleteAPIView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class getAPIVIEW(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer