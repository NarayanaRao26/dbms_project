from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

GENDER = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('others', 'OTHERS')
)

DELIVERY = (
    ('not applicable', 'NOT APPLICABLE'),
    ('Normal', 'NORMAL'),
    ('c-section', 'C-SECTION')
)

SMOKING = (
    ('never', 'NEVER'),
    ('former', 'FORMER'),
    ('ever', 'EVER')
)

PLACE = (
    ('urban', 'URBAN'),
    ('rural', 'RURAL')
)

HOUSING = (
    ('individual', 'INDIVIDUAL'),
    ('apartment', 'APARTMENT'),
    ('hostel', 'HOSTEL'),
    ('others', 'OTHERS')
)

PHYSICAL_EXERCISES = (
    ('sedentary', 'SEDENTARY'),
    ('moderate', 'MODERATE'),
    ('high', 'HIGH')
)

SLEEP = (
    ('good', 'GOOD'),
    ('insomnia', 'INSOMNIA'),
    ('day time sleepiness', 'DAY TIME SLEEPINESS')
)


CHEWING = (
    ('no', 'NO'),
    ('betel nut', 'BETEL NUT'),
    ('tobocco', 'TOBOCCO'),
    ('others', 'OTHERS')
)

ALCOHOL = (
    ('no','NO'),
    ('daily', 'DAILY'),
    ('weekly', 'WEEKLY'),
    ('monthly', 'MONTHLY'),
    ('others', 'OTHERS')
)

FOOD = (
    ('veg', 'VEG'),
    ('non-veg', 'NON-VEG')
)

FAMILY_TYPE = (
    ('nuclear', 'NUCLEAR'),
    ('combined', 'COMBINED'),
    ('others','OTHERS')
)

FOOD_PLACE = (
    ('home', 'HOME'),
    ('outside', 'OUTSIDE')
)

MARITAL_STATUS = (
    ('unmarried', 'UNMARRIED'),
    ('married', 'MARRIED'),
    ('divorced', 'DIVORCED'),
    ('widowed', 'WIDOWED'),
    ('others', 'OTHERS')
)

SEROLOGY = (
    ('neg RF and neg ACPA', 'NEG RF AND NEG ACPA'),
    ('low-pos RF or ACPA','LOW-POS RF OR ACPA'),
    ('high-pos RF or ACPA', 'HIGH-POS RF OR ACPA'),
    ('none', 'NONE')
)

APR = (
    ('normal CRP and ESR', 'NORMAL CRP AND ESR'),
    ('abnormal CRP or ESR', 'ABNORMAL CRP AND ESR'),
    ('none', 'NONE')
)

SYMPTOM_DURATION = (
    ('< 6 weeks', '< 6 WEEKS'),
    ('> 6 weeks', '> 6 WEEKS')
)


class Patient_personal_info(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=10, default="")
    yob = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=6, choices=GENDER)
    delivary = models.CharField(max_length=15, choices=DELIVERY)
    childhood_trauma = models.BooleanField()
    smoking = models.CharField(max_length=15, choices=SMOKING)
    pack_years = models.IntegerField()
    chewing = models.CharField(max_length=15, choices=CHEWING)
    drinking = models.CharField(max_length=15, choices=ALCOHOL)
    place = models.CharField(max_length=20, choices=PLACE)
    housing = models.CharField(max_length=10, choices=HOUSING)
    occupation = models.CharField(max_length=20)
    family_type = models.CharField(max_length=10, choices=FAMILY_TYPE)
    meditation = models.BooleanField()
    pets = models.BooleanField()
    garden = models.BooleanField()
    exercises = models.CharField(max_length=15, choices=PHYSICAL_EXERCISES)
    food_place = models.CharField(max_length=15, choices=FOOD_PLACE)
    food = models.CharField(max_length=10, choices=FOOD)
    marital_status = models.CharField(max_length=15, choices=MARITAL_STATUS)
    sleep = models.CharField(max_length=20, choices=SLEEP)
    work_stress = models.BooleanField()
    family_stress = models.BooleanField()
    weekend_habits = models.TextField(default="")
    other_mentions = models.TextField(default="")


class Visit(models.Model):
	patient_id = models.CharField(max_length=10, default="")
	visit_number = models.IntegerField()
	hospital_code = models.IntegerField()
	employee_id = models.CharField(max_length=10)
	date = models.DateTimeField(default=timezone.now)

	class Meta:
		unique_together = (("patient_id", "visit_number"),)


class Patient(models.Model):
    patient_id = models.CharField(max_length=10, default="", primary_key=True)
    yob = models.DateTimeField(default=timezone.now)
    phone = models.IntegerField()
    place = models.CharField(max_length=20)
    gender = models.CharField(max_length=8, choices=GENDER)


class Employee(models.Model):
    employee_id = models.CharField(max_length=10,primary_key=True,default='')
    name = models.CharField(max_length=40)
    job_profile = models.CharField(max_length=20)
    qualification = models.CharField(max_length=10)
    phone = models.IntegerField()
    department = models.CharField(max_length=20)
    gender = models.CharField(max_length=8, choices=GENDER)


class Doctor(models.Model):
    employee_id = models.CharField(max_length=10,default='')
    mentor = models.CharField(max_length=50,default='')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)


class Hospital(models.Model):
    hospital_code = models.IntegerField(primary_key=True)
    hospital_name = models.CharField(max_length=100)
    place = models.CharField(max_length=30)


class Normal_values(models.Model):
    parameter_name = models.CharField(max_length=50)
    least_value = models.FloatField()
    highest_value = models.FloatField()
    units = models.CharField(max_length=10)


class Prescription(models.Model):
    medicine = models.TextField(default="")
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)


class ACR_Scoring(models.Model):
    small_joints = models.IntegerField()
    large_joints = models.IntegerField()
    serology = models.CharField(max_length=20, choices=SEROLOGY)
    apr = models.CharField(max_length=20, choices=APR)
    symptom_duration = models.CharField(max_length=15, choices=SYMPTOM_DURATION)
    bone_test_score = models.IntegerField()
    serology_test_score = models.IntegerField()
    syptom_duration_score = models.IntegerField()
    final_acr_score = models.IntegerField()
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)



class Basic_Tests(models.Model):
    RA_Factor = models.BooleanField()
    CRP = models.BooleanField()
    ESR = models.FloatField()
    WBC = models.FloatField()
    Neutrophils = models.FloatField()
    Lymphocytes = models.FloatField()
    Monocytes = models.FloatField()
    Eosinophils = models.FloatField()
    Basophils = models.FloatField()
    Neu = models.FloatField()
    Lym  = models.FloatField()
    Mon  = models.FloatField()
    Eos  = models.FloatField()
    Bas  = models.FloatField()
    RBC = models.FloatField()
    SGOT = models.FloatField()
    SGPT = models.FloatField()
    CRP_Highly_Sensitive = models.FloatField()
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)


class Advanced_Tests(models.Model):
    HGB = models.FloatField()
    HCT = models.FloatField()
    MCV = models.FloatField()             
    MCH = models.FloatField()
    MCHC = models.FloatField()
    RDW_CV = models.FloatField()
    RDW_SD = models.FloatField()
    PLT = models.FloatField()
    MPV = models.FloatField()
    PDW = models.FloatField()
    PCT = models.FloatField()
    P_LCC = models.FloatField()
    P_LCR = models.FloatField()
    Albumin = models.FloatField()
    Alkaline_Phosphatase = models.FloatField()
    Blood_Urea = models.FloatField()
    Direct_Bilirubin = models.FloatField()
    Glucose_Fasting = models.FloatField()
    Glucose_Post_Prandial = models.FloatField()
    HBA1C = models.FloatField()
    HDL_Cholesterol = models.FloatField()
    LDH = models.FloatField()
    LDL = models.FloatField()
    Cholesterol = models.FloatField()
    Rheumatoid_Factor_Latex = models.FloatField()
    Total_Bilirubin = models.FloatField()
    Total_Cholesterol = models.FloatField()
    Total_Protein = models.FloatField()
    Uric_Acid = models.FloatField()
    visit = models.ForeignKey(Visit,on_delete=models.CASCADE)


class BMP(models.Model):
    glucose_random = models.FloatField()
    calcium = models.FloatField()
    sodium = models.FloatField()
    magnesium = models.FloatField()
    potassium = models.FloatField()
    chloride = models.FloatField()
    serum_cretinine = models.FloatField()
    visit = models.ForeignKey(Visit,on_delete=models.CASCADE)


class Confirmation_Tests(models.Model):
    IL6 = models.FloatField()
    IL10 = models.FloatField()
    IFNG = models.FloatField()
    TNF = models.FloatField()
    TGFB = models.FloatField()
    sRANKL = models.FloatField()
    IL1B = models.FloatField()
    IL17 = models.FloatField()
    visit = models.ForeignKey(Visit,on_delete=models.CASCADE)
