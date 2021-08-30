from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'Area', AreaViews)
router.register(r'AreasTree', AreasTreeView)
router.register(r'DataType', DataType)
router.register(r'Parameters', Parameters)
router.register(r'ExperimentRead', ExperimentRead)
router.register(r'PcPcConfiguration', PcPcConfiguration)
router.register(r'TypeOfPowerEquipment', TypeOfPowerEquipment)
router.register(r'PhysicalProcess', PhysicalProcess)
router.register(r'ExperimentClass', ExperimentClassViews)
router.register(r'String_values',String_valuesViewSet)
router.register(r'Phptpe',PhpTpe)
router.register(r'PhpTpeRead',PhpTpeRead)
router.register(r'ParametersValue',ParametersValuesViews)
router.register(r'ExperimentWrite', ExperimentWrite)
router.register(r'TypeOfParameters', TypeOfParametersViewSet)

urlpatterns = [

]
urlpatterns = [
    path('delete_expirements/', delete_expirements),
    path('update_Expirement/',update_Expirement),
    path('returnAreaTree/',ReturnAreaTree),
    path('ReturnExpirementClass/',ReturnExpirementClass),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
