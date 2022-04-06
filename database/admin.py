from django.contrib import admin
from .models import (
Patient_personal_info,
Visit,
Patient,
Employee,
Doctor,
Hospital,
Normal_values,
Prescription,
ACR_Scoring,
Basic_Tests,
Advanced_Tests,
BMP,
Confirmation_Tests
)

# Register your models here.
admin.site.register(Patient_personal_info),
admin.site.register(Patient),
admin.site.register(Employee),
admin.site.register(Visit),
admin.site.register(Doctor),
admin.site.register(Hospital),
admin.site.register(Normal_values),
admin.site.register(Prescription),
admin.site.register(ACR_Scoring),
admin.site.register(Basic_Tests),
admin.site.register(Advanced_Tests),
admin.site.register(BMP),
admin.site.register(Confirmation_Tests)
