from rest_framework.response import Response #Para mostrar data de los serializers
from rest_framework.decorators import api_view #Vistas de prueba que trae rest framework
from assets.serializers import * #import de todos los serializers,
from callcenterdata.models import * #import de todos los callcenterdata, proximamente se mueve a assets

#Cambiar las variables que tengan computers por el serializer que esten haciendo en el momento,
#luego de hacer las pruebas necesarias devolver a computers

@api_view(['GET'])
#Vista de prueba para visualizar datos de la BD en formato JSON
#en http://127.0.0.1:8000/
#Insertar datos desde phpmyadmin y visualizarlos en el formato JSON, luego probar insertar datos desde JSON
def getData(request):
    computers = Computers.objects.all()
    serializer = ComputerSerializer(computers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
#Vista de prueba para insertar datos en la BD via JSON
#en http://127.0.0.1:8000/add/
#copiar el formato de un dato ya ingresado desde phpmyadmin y hacer pruebas

def addItem(request):
    serializer = ComputerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)