from rest_framework import serializers
from api.models import *


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id_area', 'name_area')


class AreasTreeSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True,read_only=True)

    class Meta:
        model = AreasTree
        list_serializer_class = FilterReviewListSerializer

        extra_kwargs = {
            'children': {'read_only': True},
            'parent': {'write_only': True},
            'id_subarea':{'read_only':True}
        }

        fields = ('id_subarea', 'parent', 'id_area', 'name_subarea', 'children')



class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = ['id_data', 'name_data']


class FcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fca
        fields = ['EXP', 'id_pc', 'grid_time', 'calc_time']


class LogTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogTable
        fields = ['user', 'action', 'date']


class PcConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PcConfiguration
        fields = ['id_pc', 'proc_name', 'proc_freq', 'proc_arch', 'num_cores', 'amount_ram', 'type_ram', 'sys_cap',
                  'gpu', 'price']


class ParametersValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametrsValues
        fields = ( 'value_number', 'value_range', 'value_string', 'value_image')


class PhysicalProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalProcess
        fields = ['id_ph_p_field', 'name']


class TypeOfParametrsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeOfParametrs
        fields = ['id_type', 'name']
        extra_kwargs = {
            'id_type': {'read_only': True},
            'name': {'read_only': True}
        }

class TypeOfPowerEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfPowerEquipment
        fields = ['id_type', 'name']


class Ph_p_T_p_e_Serializer(serializers.ModelSerializer):

    class Meta:
        model = PhPTPE
        fields ='__all__'


class Ph_p_T_p_e_ReadSerializer(serializers.ModelSerializer):
    id_t_p_e_field = TypeOfPowerEquipmentSerializer()
    class Meta:
        model = PhPTPE
        fields ='__all__'


class ExperimentClassSerializer(serializers.ModelSerializer):
    id_ph_p_t_p_e_field = Ph_p_T_p_e_Serializer()
    class Meta:
        model = ExperimentClass

        fields = ['id_field', 'id_ph_p_t_p_e_field', 'id_subarea', 'main_pict', 'geom_pict', 'reg_pict', 'tepl_pict']

    def create(self, validated_data):
        id_ph_p_t_p_e_field_data = validated_data.pop('id_ph_p_t_p_e_field')
        ph_p_t_p_e_field_id=PhPTPE.objects.create(**id_ph_p_t_p_e_field_data)
        expirement_class = ExperimentClass.objects.create(**validated_data,id_ph_p_t_p_e_field=ph_p_t_p_e_field_id)
        return expirement_class

class UnicExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnicExp
        fields = ['EXP', 'id_field', 'id_exp']




class StringValuesListSerializer(serializers.ListSerializer):
    class Meta:
        model = StringValues
        fields = ['id_param', 'value']

    def create(self, validated_data):
        strings = [StringValues(**item) for item in validated_data]
        return StringValues.objects.bulk_create(strings)

    def update(self, instance, validated_data):

        mapping = {emp.valuesid: emp for emp in instance}
        data_mapping = {item['valuesid']: item for item in validated_data}

        ret = []
        for _id, data in data_mapping.items():
            emp = mapping.get(_id, None)
            if emp is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(emp, data))

        for _id, data in mapping.items():
            if _id not in data_mapping:
                data.delete()

        return ret


class StringValuesSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = StringValuesListSerializer
        model = StringValues
        fields = ['id_param', 'value']



class StringValuesSerializer2(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = StringValuesListSerializer
        model = StringValues
        fields = ['value']


class StringValuesSerializer3(serializers.ModelSerializer):
    class Meta:
        model = StringValues
        fields = '__all__'
        list_serializer_class = StringValuesListSerializer


class StringValuesListSerializer3(serializers.ListSerializer):
    class Meta:
        model = StringValues
        fields = '__all__'

    def create(self, validated_data):
        strings = [StringValues(**item) for item in validated_data]
        return StringValues.objects.bulk_create(strings)

    def update(self, instance, validated_data):

        mapping = {emp.valuesid: emp for emp in instance}
        data_mapping = {item['valuesid']: item for item in validated_data}

        ret = []
        for _id, data in data_mapping.items():
            emp = mapping.get(_id, None)
            if emp is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(emp, data))

        for _id, data in mapping.items():
            if _id not in data_mapping:
                data.delete()

        return ret


class ParametersListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        parameters = [Parametrs(**item) for item in validated_data]
        return Parametrs.objects.bulk_create(parameters)
    class Meta:
        model = Parametrs
        fields = ['id_param', 'type_of_parameters', 'name_param', 'short_name_param', 'unit_param']




class ParametersSerializer(serializers.ModelSerializer):
    string_values = StringValuesSerializer2(many=True)

    class Meta:
        model = Parametrs
        extra_kwargs = {
            'id_param': {'read_only': True},
        }
        fields = ['id_param', 'name_param', 'short_name_param', 'unit_param','id_type','string_values']

    def create(self, validated_data):
        string_data = validated_data.pop('string_values')
        parameters = Parametrs.objects.create(**validated_data)
        for string in string_data:
            StringValues.objects.create(**string, id_param=parameters)
        return parameters



class ParametersSerializerForExpirement(serializers.ModelSerializer):

    class Meta:
        model = Parametrs
        extra_kwargs = {
            'id_param': {'read_only': True},
            'id_type':{'read_only': True},
        }
        fields = ['id_param','id_type']


class ExperimentReadSerializer(serializers.ModelSerializer):
    value = ParametersValuesSerializer()
    id_param = ParametersSerializerForExpirement(read_only=True)

    class Meta:
        extra_kwargs = {
            'id_value': {'read_only': True},
        }
        model = Experiment
        fields = ['id_value', 'id_field', 'id_exp', 'id_param', 'value', 'id_data']


class ExperimentWriteSerializer(serializers.ModelSerializer):
    value = ParametersValuesSerializer()
    class Meta:
        model = Experiment
        fields = ['id_value','id_field', 'id_exp', 'id_param', 'value', 'id_data']

    def create(self, validated_data):
        value = validated_data.pop('value')
        expirement = Experiment.objects.create(**validated_data)
        ParametrsValues.objects.create(**value, id_value=expirement)
        return expirement

    def update(self,instance, validated_data):
            value_data_d = validated_data.get('value')
            id_value_d = validated_data.get('id_value')
            parameters_value = ParametrsValues.objects.get(id_value=id_value_d)
            parameters_value.value_image =value_data_d.get('value_image')
            parameters_value.value_range =value_data_d.get('value_range')
            parameters_value.value_number =value_data_d.get('value_number')
            parameters_value.value_string =value_data_d.get('value_string')
            parameters_value.save()


class DeleteExpirementByrowAndColumnSerializer(serializers.Serializer):
    experiment_class =serializers.IntegerField()
    deleter_rows = serializers.ListField(child=serializers.IntegerField())
    delete_columns = serializers.ListField(child=serializers.IntegerField())

