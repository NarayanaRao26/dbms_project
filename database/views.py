from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import (
	Patient_personal_infoForm,
	VisitForm,
	PatientForm,
	EmployeeForm,
	PrescriptionForm,
	DoctorForm,
	HospitalForm,
	Normal_valuesForm,
	ACR_ScoringForm,
	Basic_TestsForm,
	Advanced_TestsForm,
	BMPForm,
	Confirmation_TestsForm
	)

# Create your views here.


def home(request):
	return render(request, 'database/home.html')

@login_required
def patient_info(request):
	if request.method == 'POST':
		p_form = Patient_personal_infoForm(request.POST)
		a_form = ACR_ScoringForm(request.POST)
		
		if p_form.is_valid() and a_form.is_valid():
			p_form.save()
			a_form.save()
			return redirect('database-home')
	else:
		p_form = Patient_personal_infoForm()
		a_form = ACR_ScoringForm()

	context = {
		'p_form': p_form,
		'a_form': a_form
	}

	return render(request, 'database/patient_info.html',context)


@login_required
def employee(request):
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('doctor_info')
	else:
		form = EmployeeForm()

	context = {
		'form': form
	}
	return render(request, 'database/employee.html',{ 'form': form })

@login_required
def doctor_info(request):
	if request.method == 'POST':
		form = DoctorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('hospital_info')
	else:
		form = DoctorForm()

	context = {
		'form': form
	}
	return render(request, 'database/doctor_info.html',{ 'form': form })

@login_required
def hospital_info(request):
	if request.method == 'POST':
		form = HospitalForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('database-home')
	else:
		form = HospitalForm()

	context = {
		'form': form
	}
	return render(request, 'database/hospital_info.html',{ 'form': form })

@login_required
def patient(request):
	if request.method == 'POST':
		form = PatientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('visit_info')
	else:
		form = PatientForm()

	context = {
		'form': form
	}
	return render(request, 'database/patient.html',{ 'form': form })


@login_required
def visit_info(request):
	if request.method == 'POST':
		form = VisitForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('database-home')
	else:
		form = VisitForm()

	context = {
		'form': form
	}
	return render(request, 'database/visit_info.html',{ 'form': form })


@login_required
def prescriptions(request):
	if request.method == 'POST':
		form = PrescriptionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('database-home')
	else:
		form = PrescriptionForm()

	context = {
		'form': form
	}
	return render(request, 'database/prescriptions.html',{ 'form': form })



@login_required
def normalvalues(request):
	if request.method == 'POST':
		form = Normal_valuesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('database-home')
	else:
		form = Normal_valuesForm()

	context = {
		'form': form
	}
	return render(request, 'database/normalvalues.html',{ 'form': form })



@login_required
def basic_tests(request):
	if request.method == 'POST':
		form = Basic_TestsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('database-home')
	else:
		form = Basic_TestsForm()

	context = {
		'form': form
	}
	return render(request, 'database/basic_tests.html',{ 'form': form })

@login_required
def advanced_tests(request):
	if request.method == 'POST':
		form = Advanced_TestsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('bmp-info')
	else:
		form = Advanced_TestsForm()

	context = {
		'form': form
	}
	return render(request, 'database/advanced_tests.html',{ 'form': form })

@login_required
def bmp_info(request):
	if request.method == 'POST':
		form = BMPForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('database-home')
	else:
		form = BMPForm()

	context = {
		'form': form
	}
	return render(request, 'database/bmp_info.html',{ 'form': form })

@login_required
def confirmation_tests(request):
	if request.method == 'POST':
		form = Confirmation_TestsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('database-home')
	else:
		form = Confirmation_TestsForm()

	context = {
		'form': form
	}
	return render(request, 'database/confirmation_tests.html',{ 'form': form })


def about(request):
	return render(request, 'database/about.html')

	