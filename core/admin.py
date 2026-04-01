from django.contrib import admin
from .models import TimeTable, Holiday

# Admin pour TimeTable
@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('department', 'day_of_week', 'start_time', 'end_time', 'teacher', 'subject')
    list_filter = ('department', 'day_of_week', 'teacher')
    search_fields = ('department__name', 'teacher__user__username', 'subject__name')
    ordering = ('department', 'day_of_week', 'start_time')

# Admin pour Holiday
@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'description')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'description')
    ordering = ('start_date',)