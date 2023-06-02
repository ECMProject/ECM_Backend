from django.contrib import admin
from eseme_app.models import Levels, Course, Zones, Schedule, Periods, Season, Members, Students

from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

# Register your models here.
#-- ------------- ------------- ------------- ------------- -------------
#-- ------------- 
#-- ------------- ------------- ------------- ------------- -------------

@admin.register(Levels)
class CataLevelsadmin(admin.ModelAdmin):
    list_display = [f.name for f in Levels._meta.fields]
    search_fields = [f.name for f in Levels._meta.fields]
    list_per_page = 10

@admin.register(Zones)
class CataZonesadmin(admin.ModelAdmin):
    list_display = [f.name for f in Zones._meta.fields]
    search_fields = [f.name for f in Zones._meta.fields]
    list_per_page = 10

@admin.register(Periods)
class CataPeriodsadmin(admin.ModelAdmin):
    list_display = [f.name for f in Periods._meta.fields]
    search_fields = [f.name for f in Periods._meta.fields]
    list_per_page = 10

@admin.register(Schedule)
class CataScheduleadmin(admin.ModelAdmin):
    list_display = [f.name for f in Schedule._meta.fields]
    search_fields = [f.name for f in Schedule._meta.fields]
    list_per_page = 10



#-- ------------- ------------- ------------- ------------- -------------
#-- ------------- 
#-- ------------- ------------- ------------- ------------- -------------
@admin.register(Members)
class CataMembersadmin(admin.ModelAdmin):
    list_display = [f.name for f in Members._meta.fields]
    search_fields = [f.name for f in Members._meta.fields]
    list_per_page = 10
    
    #list_filter = (('memb_name',RelatedDropdownFilter),
    #               )
    
        
    
@admin.register(Course)
class CataCourseadmin(admin.ModelAdmin):
    list_display =  [f.name for f in Course._meta.fields]
    search_fields = [f.name for f in Course._meta.fields]
    list_per_page = 10
    
    list_filter = (('cour_level', RelatedDropdownFilter),
    )
    
@admin.register(Season)
class CataSeasonadmin(admin.ModelAdmin):
    list_display =  [f.name for f in Season._meta.fields]
    search_fields = [f.name for f in Season._meta.fields]
    list_per_page = 10
    
    list_filter = (('seas_period', RelatedDropdownFilter),
                   ('seas_course', RelatedDropdownFilter),
                   ('seas_schedule', RelatedDropdownFilter),
                   ('seas_mode', RelatedDropdownFilter),
                   ('seas_teacher', RelatedDropdownFilter),

    )
    

@admin.register(Students)
class CataSeasonadmin(admin.ModelAdmin):
    list_display =  [f.name for f in Students._meta.fields]
    search_fields = [f.name for f in Students._meta.fields]
    list_per_page = 10
    
    list_filter = (('stud_season', RelatedDropdownFilter),
                   ('stud_member', RelatedDropdownFilter),
    )