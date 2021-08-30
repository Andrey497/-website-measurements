# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import time
import datetime
from django.db import models
from django.contrib.postgres.fields import DecimalRangeField

class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    name_area = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Area'


class AreasTree(models.Model):
    id_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='id_area',)
    id_subarea = models.AutoField(primary_key=True)
    name_subarea = models.CharField(max_length=100)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='id_parent_area', blank=True, null=True, related_name='children')

    class Meta:
        managed = False
        db_table = 'Areas_tree'



class DataType(models.Model):
    id_data = models.AutoField(primary_key=True)
    name_data = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Data_type'

    def __str__(self):
        return self.name_data


class Experiment(models.Model):
    id_field = models.ForeignKey('ExperimentClass', models.DO_NOTHING,
                                 db_column='ID*')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    id_exp = models.IntegerField()
    id_param = models.ForeignKey('Parametrs', models.DO_NOTHING, db_column='id_param')
    id_value = models.AutoField(primary_key=True)
    id_data = models.ForeignKey(DataType, models.DO_NOTHING, db_column='id_data')

    class Meta:
        managed = False
        db_table = 'Experiment'


class ExperimentClass(models.Model):
    id_ph_p_t_p_e_field = models.ForeignKey('PhPTPE', models.DO_NOTHING,
                                            db_column='id_Ph.p._T.p.e.',related_name='expirement_class')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    id_subarea = models.ForeignKey(AreasTree, models.DO_NOTHING, db_column='id_subarea')
    id_field = models.AutoField(db_column='ID*',
                                primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    main_pict = models.CharField(db_column='Main_pict', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    geom_pict = models.CharField(db_column='Geom_pict', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    reg_pict = models.CharField(db_column='Reg_pict', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    tepl_pict = models.CharField(db_column='Tepl_pict', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Experiment_class'


class Fca(models.Model):
    exp = models.OneToOneField('UnicExp', models.DO_NOTHING, db_column='EXP',
                               primary_key=True)  # Field name made lowercase.
    id_pc = models.ForeignKey('PcConfiguration', models.DO_NOTHING, db_column='id_PC')  # Field name made lowercase.
    grid_time = models.CharField(max_length=100)
    calc_time = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'FCA'
        unique_together = (('exp', 'id_pc'),)


class LogTable(models.Model):
    user = models.CharField(max_length=100)
    action = models.CharField(primary_key=True, max_length=100)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Log_table'


class PcConfiguration(models.Model):
    id_pc = models.AutoField(db_column='id_PC', primary_key=True)  # Field name made lowercase.
    proc_name = models.CharField(max_length=100)
    proc_freq = models.DecimalField(max_digits=65535, decimal_places=65535)
    proc_arch = models.CharField(max_length=100)
    num_cores = models.IntegerField()
    amount_ram = models.DecimalField(db_column='amount_RAM', max_digits=65535,
                                     decimal_places=65535)  # Field name made lowercase.
    type_ram = models.CharField(db_column='type_RAM', max_length=100)  # Field name made lowercase.
    sys_cap = models.IntegerField()
    gpu = models.CharField(db_column='GPU', max_length=100)  # Field name made lowercase.
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'PC Configuration'


class Parametrs(models.Model):
    id_type = models.ForeignKey('TypeOfParametrs', models.DO_NOTHING, db_column='id_type', related_name='parameter')
    id_param = models.AutoField(primary_key=True)
    name_param = models.CharField(max_length=100)
    short_name_param = models.CharField(max_length=100, blank=True, null=True)
    unit_param = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Parametrs'


class ParametrsValues(models.Model):
    id_value = models.OneToOneField(Experiment, models.DO_NOTHING, db_column='id_value', primary_key=True,related_name='value')
    value_number = models.DecimalField(max_digits=14, decimal_places=7, blank=True, null=True)
    value_range = DecimalRangeField(blank=True, null=True)  # This field type is a guess.
    value_string = models.CharField(max_length=100, blank=True, null=True)
    value_image = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True,default=datetime.datetime.now())

    class Meta:
        managed = False
        db_table = 'Parametrs_values'


class PhPTPE(models.Model):
    id_ph_p_field = models.ForeignKey('PhysicalProcess', models.DO_NOTHING,
                                      db_column='id_Ph.p.')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    id_t_p_e_field = models.ForeignKey('TypeOfPowerEquipment', models.DO_NOTHING,
                                       db_column='id_T.p.e.')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    id_ph_p_t_p_e_field = models.AutoField(db_column='id_Ph.p._T.p.e.',
                                           primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'Ph.p._T.p.e.'


class PhysicalProcess(models.Model):
    id_ph_p_field = models.AutoField(db_column='id_Ph.p.',
                                     primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Physical_process'


class SoftwareConfiguration(models.Model):
    id_soft = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    grid_gen = models.CharField(max_length=100)
    calc_module = models.CharField(max_length=100)
    type_license = models.CharField(max_length=100)
    license_term = models.CharField(max_length=100)
    workplaces = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Software configuration'


class StringValues(models.Model):
    id = models.AutoField(primary_key=True)
    id_param = models.ForeignKey(Parametrs, models.DO_NOTHING, db_column='id_param',related_name="string_values")
    value = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'String_values'
        unique_together = (('id_param', 'value'),)
        ordering = ['id_param']
    def __str__(self):
        return self.value



class TypeOfParametrs(models.Model):
    id_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Type_of_parametrs'


class TypeOfPowerEquipment(models.Model):
    id_type = models.AutoField(db_column='id_T.p.e.',
                                      primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Type_of_power_equipment'


class UnicExp(models.Model):
    id_field = models.ForeignKey(ExperimentClass, models.DO_NOTHING,
                                 db_column='ID*')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    id_exp = models.IntegerField()
    exp = models.AutoField(db_column='EXP', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Unic_EXP'


class Users(models.Model):
    login = models.CharField(db_column='Login', primary_key=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    level = models.TextField(db_column='Level')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Users'




