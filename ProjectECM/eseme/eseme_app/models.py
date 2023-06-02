from django.db import models


# Create your models here.
class Zones(models.Model):
    zone_id = models.SmallAutoField(primary_key=True)
    zone_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.zone_description
    
    class Meta:
        managed = False
        db_table = 'zones'
        
class Schedule(models.Model):
    sche_id = models.SmallAutoField(primary_key=True)
    sche_description = models.TextField(blank=True, null=True)
    sche_day = models.SmallIntegerField(blank=True, null=True)
    sche_starttime = models.TimeField(blank=True, null=True)
    sche_endtime = models.TimeField(blank=True, null=True)
    
    def __str__(self):
        return self.sche_description

    class Meta:
        managed = False
        db_table = 'schedule'
        
class Periods(models.Model):
    peri_id = models.SmallAutoField(primary_key=True)
    peri_description = models.TextField(blank=True, null=True)
    peri_start = models.DateField(blank=True, null=True)
    peri_end = models.DateField(blank=True, null=True)
    peri_status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.peri_description

    class Meta:
        managed = False
        db_table = 'periods'

class Modes(models.Model):
    mode_id = models.SmallAutoField(primary_key=True)
    mode_description = models.TextField(blank=True, null=True)
    mode_status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.mode_description
    
    class Meta:
        managed = False
        db_table = 'modes'        

class Levels(models.Model):
    leve_id = models.SmallAutoField(primary_key=True)
    leve_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.leve_description
    
    class Meta:
        managed = False
        db_table = 'levels'
#-- ---------------- ---------------- ---------------- ----------------
#-- ------ Dependientes
#-- ---------------- ---------------- ---------------- ----------------
class Course(models.Model):
    cour_id = models.SmallAutoField(primary_key=True)
    cour_description = models.TextField(blank=True, null=True)
    cour_level = models.ForeignKey('Levels', models.DO_NOTHING, db_column='cour_level', blank=True, null=True)
    cour_material = models.TextField(blank=True, null=True)
    alterno = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cour_description
    
    class Meta:
        managed = False
        db_table = 'course'
        
class Members(models.Model):
    memb_id = models.SmallAutoField(primary_key=True)
    memb_dni = models.TextField()
    memb_typedni = models.CharField(max_length=3, blank=True, null=True)
    memb_name = models.TextField()
    memb_surname = models.TextField()
    memb_mobil = models.TextField()
    birthdate = models.DateField(blank=True, null=True)
    memb_zone = models.ForeignKey('Zones', models.DO_NOTHING, db_column='memb_zone', blank=True, null=True)

    def __str__(self):
        return self.memb_name
    
    class Meta:
        managed = False
        db_table = 'members'
        
class Season(models.Model):
    seas_id = models.SmallAutoField(primary_key=True)
    seas_period = models.ForeignKey(Periods, models.DO_NOTHING, db_column='seas_period', blank=True, null=True)
    seas_course = models.ForeignKey(Course, models.DO_NOTHING, db_column='seas_course', blank=True, null=True)
    seas_schedule = models.ForeignKey(Schedule, models.DO_NOTHING, db_column='seas_schedule', blank=True, null=True)
    seas_mode = models.ForeignKey(Modes, models.DO_NOTHING, db_column='seas_mode', blank=True, null=True)
    seas_teacher = models.ForeignKey(Members, models.DO_NOTHING, db_column='seas_teacher', blank=True, null=True)
    seas_status = models.BooleanField(blank=True, null=True)
    seas_glosa = models.TextField()    
    
    def __str__(self):
        return self.seas_glosa

    class Meta:
        managed = False
        db_table = 'season'


class Students(models.Model):
    stud_id = models.SmallAutoField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 'students'