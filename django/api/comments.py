





# class ParametersSerializer(WritableNestedModelSerializer):
#     type_of_parameters = TypeOfParametrsSerializer()
#
#     class Meta:
#         model = Parametrs
#         fields = ['id_param', 'type_of_parameters', 'name_param', 'short_name_param', 'unit_param']
#     # list_serializer_class = ParametersListSerializer

 # def update(self,instance,validated_data):
    #     string_data = validated_data.pop('string_values')
    #     string_values = instance.string_values
    #
    #     instance.name_param = validated_data.get('name_param', instance.name_param)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #
    #
    #     param.save()
    #
    #     return instance


#
#
#
#


# class User(models.Model):
#     username = models.CharField(max_length=100)
#
#
# class AccessKey(models.Model):
#     key = models.CharField(max_length=100)
#
#
# class Profile(models.Model):
#     sites = models.ManyToManyField(Site)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     access_key = models.ForeignKey(AccessKey, null=True, on_delete=models.CASCADE)
#
#
# class Avatar(models.Model):
#     image = models.CharField(max_length=100)
#     profile = models.ForeignKey(Profile, related_name='avatars', on_delete=models.CASCADE)
#
#
#
# class AvatarSerializer(serializers.ModelSerializer):
#     image = serializers.CharField()
#
#     class Meta:
#         model = Avatar
#         fields = ('pk', 'image',)
#
#
# class SiteSerializer(serializers.ModelSerializer):
#     url = serializers.CharField()
#
#     class Meta:
#         model = Site
#         fields = ('pk', 'url',)
#
#
# class AccessKeySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = AccessKey
#         fields = ('pk', 'key',)
#
#
# class ProfileSerializer(WritableNestedModelSerializer):
#     # Direct ManyToMany relation
#     sites = SiteSerializer(many=True)
#
#     # Reverse FK relation
#     avatars = AvatarSerializer(many=True)
#
#     # Direct FK relation
#     access_key = AccessKeySerializer(allow_null=True)
#
#     class Meta:
#         model = Profile
#         fields = ('pk', 'sites', 'avatars', 'access_key',)
#
#
# class UserSerializer(WritableNestedModelSerializer):
#     # Reverse OneToOne relation
#     profile = ProfileSerializer()
#
#     class Meta:
#         model = User
#         fields = ('pk', 'profile', 'username',)


# class StringValuesListSerializer(serializers.ListSerializer):
#     class Meta:
#         model = StringValues
#         fields = ['id_type', 'name']
#
#     def create(self, validated_data):
#         strings = [StringValues(**item) for item in validated_data]
#         return StringValues.objects.bulk_create(strings)
#
#     def update(self, instance, validated_data):
#
#         mapping = {emp.valuesid: emp for emp in instance}
#         data_mapping = {item['valuesid']: item for item in validated_data}
#
#         ret = []
#         for _id, data in data_mapping.items():
#             emp = mapping.get(_id, None)
#             if emp is None:
#                 ret.append(self.child.create(data))
#             else:
#                 ret.append(self.child.update(emp, data))
#
#         for _id, data in mapping.items():
#             if _id not in data_mapping:
#                 data.delete()
#
#         return ret
#
#     def update(self, instance, validated_data):
#
#         mapping = {emp.valuesid: emp for emp in instance}
#         data_mapping = {item['valuesid']: item for item in validated_data}
#
#         ret = []
#         for _id, data in data_mapping.items():
#             emp = mapping.get(_id, None)
#             if emp is None:
#                 ret.append(self.child.create(data))
#             else:
#                 ret.append(self.child.update(emp, data))
#
#         for _id, data in mapping.items():
#             if _id not in data_mapping:
#                 data.delete()
#
#         return ret


# class StringValuesListSerializer3(serializers.ListSerializer):
#     class Meta:
#         model = StringValues
#         fields = '__all__'
#
#     def create(self, validated_data):
#         strings = [StringValues(**item) for item in validated_data]
#         return StringValues.objects.bulk_create(strings)
#
#     def update(self, instance, validated_data):
#
#         mapping = {emp.valuesid: emp for emp in instance}
#         data_mapping = {item['valuesid']: item for item in validated_data}
#
#         ret = []
#         for _id, data in data_mapping.items():
#             emp = mapping.get(_id, None)
#             if emp is None:
#                 ret.append(self.child.create(data))
#             else:
#                 ret.append(self.child.update(emp, data))
#
#         for _id, data in mapping.items():
#             if _id not in data_mapping:
#                 data.delete()
#
#         return ret
# """Поле для создания или добовления внешнего ключа"""
# class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
#     def __init__(self, **kwargs):
#         self.serializer = kwargs.pop('serializer', None)
#         if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
#             raise TypeError('"serializer" is not a valid serializer class')
#
#         super().__init__(**kwargs)
#
#     def use_pk_only_optimization(self):
#         return False if self.serializer else True
#
#     def to_representation(self, instance):
#         if self.serializer:
#             return self.serializer(instance, context=self.context).data
#         return super().to_representation(instance)


# def __init__(self, *args, **kwargs):
#     many = kwargs.pop('many', True)
#     super(StringValuesSerializer, self).__init__(many=many, *args, **kwargs)
