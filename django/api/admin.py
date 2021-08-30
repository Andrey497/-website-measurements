from django.contrib import admin
from .models import Area, AreasTree, DataType, Experiment, ExperimentClass, Fca, LogTable, \
    PcConfiguration, Parametrs, ParametrsValues, PhPTPE, PhysicalProcess, TypeOfParametrs, \
    TypeOfPowerEquipment, UnicExp, Users, StringValues

# Register your models here
admin.site.register(Area)
admin.site.register(AreasTree)
admin.site.register(DataType)
admin.site.register(Experiment)
admin.site.register(ExperimentClass)
admin.site.register(Fca)
admin.site.register(LogTable)
admin.site.register(PcConfiguration)
admin.site.register(Parametrs)
admin.site.register(ParametrsValues)
admin.site.register(PhPTPE)
admin.site.register(PhysicalProcess)
admin.site.register(TypeOfParametrs)
admin.site.register(TypeOfPowerEquipment)
admin.site.register(UnicExp)
admin.site.register(Users)
admin.site.register(StringValues)
