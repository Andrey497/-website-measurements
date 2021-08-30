import json

from django.shortcuts import render
from rest_framework import viewsets, generics, status, response, views
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.views import APIView

from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class AreaViews(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreasTreeView(viewsets.ModelViewSet):
    queryset = AreasTree.objects.all()
    serializer_class = AreasTreeSerializer


class DataType(viewsets.ModelViewSet):
    queryset = DataType.objects.all()
    serializer_class = DataTypeSerializer


class TypeOfPowerEquipment(viewsets.ModelViewSet):
    queryset = TypeOfPowerEquipment.objects.all()
    serializer_class = TypeOfPowerEquipmentSerializer


class PhysicalProcess(viewsets.ModelViewSet):
    queryset = PhysicalProcess.objects.all()
    serializer_class = PhysicalProcessSerializer


class ExperimentClassViews(viewsets.ModelViewSet):
    queryset = ExperimentClass.objects.all()
    serializer_class = ExperimentClassSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id_subarea","id_ph_p_t_p_e_field","id_ph_p_t_p_e_field"]


class Parameters(viewsets.ModelViewSet):
    queryset = Parametrs.objects.all()
    serializer_class = ParametersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_type']


class ExperimentWrite(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentWriteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_field']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TypeOfParametersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TypeOfParametrs.objects.all()
    serializer_class = TypeOfParametrsSerializer


class ExperimentRead(viewsets.ReadOnlyModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentReadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_field']


class PcPcConfiguration(viewsets.ModelViewSet):
    queryset = PcConfiguration.objects.all()
    serializer_class = PcConfigurationSerializer


class String_valuesViewSet(viewsets.ModelViewSet):
    queryset = StringValues.objects.all()
    serializer_class = StringValuesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def get_serializer_class(self, *args, **kwargs):
    #     if "data" in kwargs:
    #         data = kwargs["data"]
    #
    #         if isinstance(data, list):
    #             kwargs["many"] = True
    #
    #     return super(String_valuesViewSet, self).get_serializer(*args, **kwargs)


class String_valuesApi(views.APIView):
    def get(self, request):
        data = StringValues.objects.all()
        data_serializers = StringValuesSerializer3(data, many=True, read_only=True)
        payload = {
            'codigo': status.HTTP_200_OK,
            'mensaje': 'Ok',
            'data': data_serializers.data
        }
        return response.Response(payload, status=status.HTTP_200_OK)

    def post(self, request):
        """ Ejemplo de manejo de listas en Serializer


          Para este ejemplo asumimos lo siguiente:
          Se tienen que enviar todos los datos existentes de los empleados en el JSON ya que
          se comparara con la base de datos y :
           1.- Si se encuentran se actualizan los datos,
           2.- Si no existen en la base de datos  se crean,
           3.- Si se encuentran en la base de datos, pero no fueron pasados en el JSON se elimnan.

         """

        # Obtener el  JSON.
        data = request.data

        # Obtener los datos de la base de datos
        emp = StringValues.objects.all()
        # Es necesario pasarlo a listas
        _arr_emp = [entry for entry in emp]

        # Serializar los datos
        se = StringValuesSerializer3(instance=_arr_emp, data=data, many=True)

        # validar y guardar
        if se.is_valid():
            se.save()
            payload = {
                'codigo': status.HTTP_200_OK,
                'mensaje': 'Ok',
                data: 'hello'

            }
        else:
            payload = {
                'codigo': status.HTTP_400_BAD_REQUEST,
                'mensaje': 'Fallo',
                'data': se.errors
            }

        return response.Response(payload, status=status.HTTP_200_OK);


class String_valuesApi(views.APIView):
    def get(self, request):
        data = StringValues.objects.all()
        data_serializers = StringValuesSerializer3(data, many=True, read_only=True)
        payload = {
            'codigo': status.HTTP_200_OK,
            'mensaje': 'Ok',
            'data': data_serializers.data
        }
        return response.Response(payload, status=status.HTTP_200_OK)

    def post(self, request):
        """ Ejemplo de manejo de listas en Serializer


          Para este ejemplo asumimos lo siguiente:
          Se tienen que enviar todos los datos existentes de los empleados en el JSON ya que
          se comparara con la base de datos y :
           1.- Si se encuentran se actualizan los datos,
           2.- Si no existen en la base de datos  se crean,
           3.- Si se encuentran en la base de datos, pero no fueron pasados en el JSON se elimnan.

         """

        # Obtener el  JSON.
        data = request.data

        # Obtener los datos de la base de datos
        emp = StringValues.objects.all()
        # Es necesario pasarlo a listas
        _arr_emp = [entry for entry in emp]

        # Serializar los datos

        se = StringValuesSerializer3(instance=_arr_emp, data=data, many=True)

        # validar y guardar
        if se.is_valid():
            se.save()
            payload = {
                'codigo': status.HTTP_200_OK,
                'mensaje': 'Ok',
                data: 'hello'

            }
        else:
            payload = {
                'codigo': status.HTTP_400_BAD_REQUEST,
                'mensaje': 'Fallo',
                'data': se.errors
            }

        return response.Response(payload, status=status.HTTP_200_OK);


class PhpTpe(viewsets.ModelViewSet):
    queryset = PhPTPE.objects.all()
    serializer_class = Ph_p_T_p_e_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_ph_p_field']

class PhpTpeRead(viewsets.ModelViewSet):
    queryset = PhPTPE.objects.all()
    serializer_class = Ph_p_T_p_e_ReadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_ph_p_field']


class ParametersValuesViews(viewsets.ModelViewSet):
    queryset = ParametrsValues.objects.all()
    serializer_class = ParametersValuesSerializer


# Метод #удаления не работает
class DeleteExpirementByrowAndColumnApiView(views.APIView):
    model = Experiment
    serializer_class = DeleteExpirementByrowAndColumnSerializer

    def post(self, request):
        data = request.data
        query = (Q(id_field=data.experiment_class), Q(id_exp=data.rows) | Q(id_param=data.columns))
        queryset = Experiment.objects.filter(query)
        print(queryset)
        queryset.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response("Deleted_objects", status=status.HTTP_200_OK)


# Метод удаления
@api_view(['GET', 'POST'])
def delete_expirements(request):
    if request.method == 'POST':
        data = request.data
        if((data.rows|data.columns)&data.experiment_class):
            query = (Q(id_field=data.experiment_class), (Q(id_exp=data.rows) | Q(id_param=data.columns)))
            queryset = Experiment.objects.filter(query)
            queryset.delete()
    return response.Response({"message": "Ok"})


# Обновление
@api_view(['GET', 'POST'])
def update_Expirement(request):
    if request.method == 'POST':
        data = request.data
        for item in data:
            value_data_d = item.get('value')
            id_value_d = item.get('id_value')
            parameters_value = ParametrsValues.objects.get(pk=id_value_d)
            parameters_value.value_image = value_data_d.get('value_image')
            parameters_value.value_range = value_data_d.get('value_range')
            parameters_value.value_number = value_data_d.get('value_number')
            parameters_value.value_string = value_data_d.get('value_string')
            parameters_value.save()
    return response.Response({"message": "OK"})


@api_view(['GET'])
def ReturnAreaTree(request):
    if request.method == 'GET':
        area_id = request.GET.get("area_id", 0)
        parent_subarea_id = request.GET.get("parent_subarea_id", 0)
        phys_proc_id = request.GET.get("phys_proc_id", 1)
        equpment_type_id = request.GET.get("equpment_type_id",1)
        subareas = AreasTree.objects.filter(id_area=area_id, parent=parent_subarea_id, experimentclass__id_ph_p_t_p_e_field__id_ph_p_field=phys_proc_id,experimentclass__id_ph_p_t_p_e_field__id_t_p_e_field=equpment_type_id)
        area = Area.objects.get(pk=area_id);
        subareas_list = []
        for item in subareas:
            subareas_list.append({
                'id':item.id_subarea,
                'name':item.name_subarea
            })
        if(len(subareas_list)!=0):
            return response.Response({'area_name':area.name_area,'subareas':subareas_list},status.HTTP_200_OK)
        return response.Response({'status': "failed"}, status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def ReturnExpirementClass(request):
    if request.method == 'GET':
        subarea_id = request.GET.get("subarea_id", 0)
        phys_proc_id = request.GET.get("phys_proc_id", 0)
        equpment_type_id = request.GET.get("equpment_type_id",0)
        subareas = ExperimentClass.objects.filter(id_subarea=subarea_id,id_ph_p_t_p_e_field__id_ph_p_field=phys_proc_id,id_ph_p_t_p_e_field__id_t_p_e_field=equpment_type_id)
        if(subareas):
            returnObject ={
            'id':subareas[0].id_field,
            'main_pict': subareas[0].main_pict,
            'geom_pict': subareas[0].geom_pict,
            'reg_pict':subareas[0].reg_pict,
            'tepl_pict':subareas[0].tepl_pict,
            }
            return response.Response({'message':returnObject},status.HTTP_200_OK)
        return response.Response({'message':"Такого класса нет"},status.HTTP_400_BAD_REQUEST)


