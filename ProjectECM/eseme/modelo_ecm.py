from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Course(models.Model):
    cour_id = models.SmallAutoField(primary_key=True)
    cour_description = models.TextField(blank=True, null=True)
    cour_level = models.ForeignKey('Levels', models.DO_NOTHING, db_column='cour_level', blank=True, null=True)
    cour_material = models.TextField(blank=True, null=True)
    alterno = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Cursillo(models.Model):
    curso = models.TextField(blank=True, null=True)
    code = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cursillo'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dnis(models.Model):
    identificador = models.TextField(blank=True, null=True)
    nombre = models.TextField(blank=True, null=True)
    mobil = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    zona = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dnis'


class EsemeAppSchedule(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=150)
    day = models.IntegerField()
    startime = models.TimeField()
    endime = models.TimeField()

    class Meta:
        managed = False
        db_table = 'eseme_app_schedule'


class EsemeAppZones(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'eseme_app_zones'


class Levels(models.Model):
    leve_id = models.SmallAutoField(primary_key=True)
    leve_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'levels'


class Members(models.Model):
    memb_id = models.SmallAutoField(primary_key=True)
    memb_dni = models.TextField()
    memb_typedni = models.CharField(max_length=3, blank=True, null=True)
    memb_name = models.TextField()
    memb_surname = models.TextField()
    memb_mobil = models.TextField()
    birthdate = models.DateField(blank=True, null=True)
    memb_zone = models.ForeignKey('Zones', models.DO_NOTHING, db_column='memb_zone', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'members'


class Migra(models.Model):
    nombre = models.TextField(blank=True, null=True)
    identificador = models.TextField(blank=True, null=True)
    celular = models.TextField(blank=True, null=True)
    curso = models.TextField(blank=True, null=True)
    zona = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migra'


class Migra01(models.Model):
    nombre = models.TextField(blank=True, null=True)
    identificador = models.TextField(blank=True, null=True)
    celular = models.TextField(blank=True, null=True)
    curso = models.TextField(blank=True, null=True)
    zona = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    vez = models.BigIntegerField(blank=True, null=True)
    cod_curso = models.SmallIntegerField(blank=True, null=True)
    cod_zone = models.SmallIntegerField(blank=True, null=True)
    cod_member = models.SmallIntegerField(blank=True, null=True)
    cod_season = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migra01'


class Modes(models.Model):
    mode_id = models.SmallAutoField(primary_key=True)
    mode_description = models.TextField(blank=True, null=True)
    mode_status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modes'


class Periods(models.Model):
    peri_id = models.SmallAutoField(primary_key=True)
    peri_description = models.TextField(blank=True, null=True)
    peri_start = models.DateField(blank=True, null=True)
    peri_end = models.DateField(blank=True, null=True)
    peri_status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periods'


class Schedule(models.Model):
    sche_id = models.SmallAutoField(primary_key=True)
    sche_description = models.TextField(blank=True, null=True)
    sche_day = models.SmallIntegerField(blank=True, null=True)
    sche_starttime = models.TimeField(blank=True, null=True)
    sche_endtime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule'


class Season(models.Model):
    seas_id = models.SmallAutoField(primary_key=True)
    seas_period = models.ForeignKey(Periods, models.DO_NOTHING, db_column='seas_period', blank=True, null=True)
    seas_course = models.ForeignKey(Course, models.DO_NOTHING, db_column='seas_course', blank=True, null=True)
    seas_schedule = models.ForeignKey(Schedule, models.DO_NOTHING, db_column='seas_schedule', blank=True, null=True)
    seas_mode = models.ForeignKey(Modes, models.DO_NOTHING, db_column='seas_mode', blank=True, null=True)
    seas_teacher = models.ForeignKey(Members, models.DO_NOTHING, db_column='seas_teacher', blank=True, null=True)
    seas_status = models.BooleanField(blank=True, null=True)
    seas_glosa = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'season'


class Students(models.Model):
    stud_season = models.ForeignKey(Season, models.DO_NOTHING, db_column='stud_season', blank=True, null=True)
    stud_member = models.ForeignKey(Members, models.DO_NOTHING, db_column='stud_member', blank=True, null=True)
    seas_final = models.SmallIntegerField(blank=True, null=True)
    seas_ses01 = models.BooleanField(blank=True, null=True)
    seas_ses02 = models.BooleanField(blank=True, null=True)
    seas_ses03 = models.BooleanField(blank=True, null=True)
    seas_ses04 = models.BooleanField(blank=True, null=True)
    seas_ses05 = models.BooleanField(blank=True, null=True)
    seas_ses06 = models.BooleanField(blank=True, null=True)
    seas_ses07 = models.BooleanField(blank=True, null=True)
    seas_ses08 = models.BooleanField(blank=True, null=True)
    seas_ses09 = models.BooleanField(blank=True, null=True)
    seas_ses10 = models.BooleanField(blank=True, null=True)
    seas_ses11 = models.BooleanField(blank=True, null=True)
    seas_ses12 = models.BooleanField(blank=True, null=True)
    stud_id = models.AutoField()
    stud_glosa = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class Zones(models.Model):
    zone_id = models.SmallAutoField(primary_key=True)
    zone_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zones'
