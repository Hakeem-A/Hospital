from datetime import datetime

class Patient:
    def __init__(self, patient_id, name, age, gender, contact, address):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.address = address
        self.date_registered = datetime.now()
        self.consultations = []  # Many consultations
        self.bills = []  # Many bills

    def register(self):
        print(f"Patient {self.name} registered successfully on {self.date_registered}")

    def add_consultation(self, consultation):
        self.consultations.append(consultation)

    def add_bill(self, bill):
        self.bills.append(bill)

    def __str__(self):
        return f"Patient({self.name}, Age: {self.age}, Contact: {self.contact})"


class Staff:
    def __init__(self, staff_id, name, role, department, contact, email):
        self.staff_id = staff_id
        self.name = name
        self.role = role  # Doctor, Nurse, Admin
        self.department = department
        self.contact = contact
        self.email = email

    def __str__(self):
        return f"Staff({self.name}, Role: {self.role}, Department: {self.department})"


class Consultation:
    def __init__(self, consultation_id, patient, doctor, notes, diagnosis):
        self.consultation_id = consultation_id
        self.patient = patient  # One Patient
        self.doctor = doctor  # One Doctor
        self.date = datetime.now()
        self.notes = notes
        self.diagnosis = diagnosis
        self.prescriptions = []  # Many prescriptions

        # Link consultation to the patient
        patient.add_consultation(self)

    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)

    def __str__(self):
        return f"Consultation({self.consultation_id}, {self.patient.name}, {self.diagnosis}, Doctor: {self.doctor.name})"


class Prescription:
    def __init__(self, prescription_id, consultation, medication_name, dosage, instructions):
        self.prescription_id = prescription_id
        self.consultation = consultation  # One Consultation
        self.medication_name = medication_name
        self.dosage = dosage
        self.instructions = instructions

        # Link prescription to the consultation
        consultation.add_prescription(self)

    def __str__(self):
        return f"Prescription({self.medication_name}, {self.dosage}, {self.instructions})"


class Bill:
    def __init__(self, bill_id, patient, amount, due_date):
        self.bill_id = bill_id
        self.patient = patient  # One Patient
        self.amount = amount
        self.status = "Unpaid"
        self.date_issued = datetime.now()
        self.due_date = due_date

        # Link bill to the patient
        patient.add_bill(self)

    def pay(self):
        self.status = "Paid"
        print(f"Bill {self.bill_id} for {self.patient.name} has been paid.")

    def __str__(self):
        return f"Bill({self.bill_id}, Amount: ${self.amount}, Status: {self.status})"
# this is a test commit