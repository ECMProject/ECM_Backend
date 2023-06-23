from django_filters import rest_framework as filters
from eseme_app import models
from django_filters import DateFilter

class CustomInFilter(filters.Filter):
    def filter(self, qs, value):
        if not value:
            return qs
        values = value.split(',')
        if len(values) > 1:
            self.lookup_expr = 'in'
        else:
            self.lookup_expr = 'exact'
            values = values[0]

        return super(CustomInFilter, self).filter(qs, values)

class StudentByIdFilter(filters.FilterSet):
    dni = filters.NumberFilter(field_name='stud_member__memb_dni')

    class Meta:
        model = models.Students
        fields = ['dni']
        
        