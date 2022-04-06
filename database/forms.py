from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class Patient_personal_infoForm(forms.ModelForm):
	class Meta:
		model = Patient_personal_info
		fields = ['patient_id', 'yob', 'gender', 'delivary', 'childhood_trauma', 'smoking', 'pack_years', 'chewing', 'drinking', 'place', 'housing', 'occupation', 'family_type', 'meditation', 'pets', 'garden', 'exercises', 'food_place', 'food', 'marital_status', 'sleep', 'work_stress', 'family_stress', 'weekend_habits', 'other_mentions']


class VisitForm(forms.ModelForm):
	class Meta:
		model = Visit
		fields = ['patient_id', 'visit_number', 'hospital_code', 'employee_id', 'date' ]


class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ['patient_id', 'yob', 'phone', 'place', 'gender']

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ['employee_id', 'name', 'job_profile', 'qualification', 'phone', 'department', 'gender']


class PrescriptionForm(forms.ModelForm):
	class Meta:
		model = Prescription
		fields = ['visit', 'medicine']


class DoctorForm(forms.ModelForm):
	class Meta:
		model = Doctor
		fields = ['employee_id', 'mentor', 'doctor']


class HospitalForm(forms.ModelForm):
	class Meta:
		model = Hospital
		fields = ['hospital_code', 'hospital_name', 'place' ]


class Normal_valuesForm(forms.ModelForm):
	class Meta:
		model = Normal_values
		fields = ['parameter_name', 'least_value', 'highest_value', 'units']



class ACR_ScoringForm(forms.ModelForm):
	class Meta:
		model = ACR_Scoring
		fields = ['visit', 'small_joints', 'large_joints', 'serology', 'apr','symptom_duration', 'bone_test_score', 'serology_test_score', 'syptom_duration_score', 'final_acr_score']


class Basic_TestsForm(forms.ModelForm):
	class Meta:
		model = Basic_Tests
		fields = ['visit', 'RA_Factor', 'CRP', 'ESR', 'WBC', 'Neutrophils','Lymphocytes', 'Monocytes', 'Eosinophils', 'Basophils','Neu', 'Lym', 'Mon','Eos', 'Bas', 'RBC', 'SGOT', 'SGPT', 'CRP_Highly_Sensitive']


class Advanced_TestsForm(forms.ModelForm):
	class Meta:
		model = Advanced_Tests
		fields = ['visit', 'HGB', 'HCT', 'MCV', 'MCH', 'MCHC', 'RDW_CV', 'RDW_SD', 'PLT', 'MPV', 'PDW', 'PCT', 'P_LCC', 'P_LCR', 'Albumin', 'Alkaline_Phosphatase', 'Blood_Urea', 'Direct_Bilirubin', 'Glucose_Fasting', 'Glucose_Post_Prandial', 'HBA1C', 'HDL_Cholesterol', 'LDH', 'LDL', 'Cholesterol', 'Rheumatoid_Factor_Latex', 'Total_Bilirubin', 'Total_Cholesterol', 'Total_Protein', 'Uric_Acid']


class BMPForm(forms.ModelForm):
	class Meta:
		model = BMP
		fields = ['visit', 'glucose_random', 'calcium', 'sodium', 'magnesium', 'potassium', 'chloride', 'serum_cretinine']


class Confirmation_TestsForm(forms.ModelForm):
	class Meta:
		model = Confirmation_Tests
		fields = ['visit', 'IL6', 'IL10', 'IFNG', 'TNF', 'TGFB', 'sRANKL', 'IL1B', 'IL17']
