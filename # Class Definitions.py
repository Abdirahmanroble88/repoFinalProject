#class for the Doctor
class Doctor:
    def __init__(self, doctor_id=None, name=None,                          #Method 6 variable
                 specialization=None, working_time=None, 
                 qualification=None, room_number=None):
        self.doctor_id = doctor_id                                        
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def __str__(self):
        return (f"{self.doctor_id:<4}{self.name:<20}"                    # a String Method and string format 
                f"{self.specialization:<15}{self.working_time:<10}"      #that indicated Number of character it whole
                f"{self.qualification:<20}{self.room_number}")


#A class that whole Doctors for managing a list of doctors
class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    def format_dr_info(self, doctor):
        return (f"{doctor.doctor_id:<4}{doctor.name:<20}"
                f"{doctor.specialization:<15}{doctor.working_time:<10}"
                 f"{doctor.qualification:<20} {doctor.room_number}")

    def enter_dr_info(self):
        doctor_id = input("Enter the doctor's ID: ")
        name = input("Enter the doctor's name: ")
        specialization = input("Enter the doctor's specialization: ")
        working_time = input("Enter the doctor's working time: ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")

        return Doctor(doctor_id, name, specialization, working_time, qualification, room_number)

    def read_doctors_file(self):                   #exception condition in case the file no Error or not found
        try:                                       #a For loop iterates over each line "_" and  removes any leading "_"
            with open(r"C:\Users\arobl\OneDrive\Desktop\Python\ProjectFinal\doctors.txt", "r") as file:
                for line in file:
                    doctor_info = line.strip().split("_")
                    doctor_id, name, specialization, working_time, qualification, room_number = doctor_info
                    doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
                    self.doctors.append(doctor)
        except FileNotFoundError:
            print("Doctors file not found. Creating a new one...")

    def search_doctor_by_id(self):                           # A Method to search for a doctor by their ID
        doctor_id = input("Enter the doctor's ID: ")         
        found = False
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                self.display_doctor_info(doctor)
                found = True
                break

        if not found:                                             # display if the Doctor ID no found  
            print("Can't find the doctor with the same ID on the system")

    def search_doctor_by_name(self):                            # A Method to search for a Doctors by their name
        doctor_name = input("Enter the doctor's name: ")
        found = False
        for doctor in self.doctors:
            if doctor.name.lower() == doctor_name.lower():
                self.display_doctor_info(doctor)
                found = True
                break

        if not found:
            print("Can't find the doctor with the same name on the system")

    def display_doctor_info(self, doctor):                                      #Method that display the output base the search input
        print("{:<4} {:<20} {:<15} {:<10} {:<20} {:<10}".format(
            "Id", "Name", "Specialization", "Timing", "Qualification", "Room Number"))
        print("{:<4} {:<20} {:<15} {:<10} {:<20} {:<10}".format(
                doctor.doctor_id, doctor.name, doctor.specialization,
                doctor.working_time, doctor.qualification, doctor.room_number))

    def edit_doctor_info(self):                                                 #Method that allow you to input Doctors ID
        doctor_id = input("Please enter the ID of the doctor you want to edit: ") #display their names,ID,Specialty...
        found = False
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                name = input("Enter new Name: ")
                specialization = input("Enter new Specialist in: ")
                working_time = input("Enter new Timing: ")
                qualification = input("Enter new Qualification: ")
                room_number = input("Enter new Room number: ")

                doctor.name = name
                doctor.specialization = specialization
                doctor.working_time = working_time
                doctor.qualification = qualification
                doctor.room_number = room_number

                self.write_list_of_doctors_to_file()
                print("Doctor whose ID is", doctor_id, "has been edited.") #statement helps unnecessary iteration
                found = True
                break
                                                            
        if not found:
            print("Cannot find the doctor with the ID", doctor_id)
                                                                      # Method that list of Doctors organized
    def display_doctors_list(self):                                   #format display as grid display as a list 
        print("{:<4} {:<20} {:<15} {:<10} {:<20} {:<10}".format(          
            "Id", "Name", "Specialization", "Timing", "Qualification", "Room Number"))
        for doctor in self.doctors:
            print("{:<4} {:<20} {:<15} {:<10} {:<20} {:<10}".format(
                doctor.doctor_id, doctor.name, doctor.specialization,
                doctor.working_time, doctor.qualification, doctor.room_number))

    def write_list_of_doctors_to_file(self):
        with open(r"C:\Users\arobl\OneDrive\Desktop\Python\ProjectFinal\doctors.txt", "w") as file:
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor) + "\n")

    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        self.write_list_of_doctors_to_file()
        print("Doctor whose ID is", new_doctor.doctor_id, "has been added.")


class Patient:
    def __init__(self, pid=None, name=None, disease=None, gender=None, age=None):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"{self.pid:<5} {self.name:<20} {self.disease:<15} {self.gender:<10} {self.age}"


class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def format_patient_info(self, patient):
        return f"{patient.pid:<5} {patient.name:<20} {patient.disease:<15} {patient.gender:<10} {patient.age}"

    def enter_patient_info(self):
        pid = input("Enter the patient's ID: ")
        name = input("Enter the patient's name: ")
        disease = input("Enter the patient's disease: ")
        gender = input("Enter the patient's gender: ")
        age = input("Enter the patient's age: ")

        return Patient(pid, name, disease, gender, age)

    def read_patients_file(self):
        try:
            with open(r"C:\Users\arobl\OneDrive\Desktop\Python\ProjectFinal\patients.txt", "r") as file:
                for line in file:
                    patient_info = line.strip().split("_")
                    pid, name, disease, gender, age = patient_info
                    patient = Patient(pid, name, disease, gender, age)
                    self.patients.append(patient)
        except FileNotFoundError:
            print("Patients file not found. Creating a new one...")

    def search_patient_by_id(self):
        pid = input("Enter the patient's ID: ")
        found = False
        for patient in self.patients:
            if patient.pid == pid:
                self.display_patient_info(patient)
                found = True
                break

        if not found:
            print("Can't find the patient with the same ID on the system")

    def display_patient_info(self, patient):                                       #only when searching patient
        print("ID    Name                 Disease         Gender     Age")
        print(patient)

    def edit_patient_info(self):
        pid = input("Please enter the ID of the patient you want to edit: ")
        found = False
        for patient in self.patients:
            if patient.pid == pid:
                name = input("Enter new Name: ")
                disease = input("Enter new Disease: ")
                gender = input("Enter new Gender: ")
                age = input("Enter new Age: ")

                patient.name = name
                patient.disease = disease
                patient.gender = gender
                patient.age = age

                self.write_list_of_patients_to_file()
                print("Patient whose ID is", pid, "has been edited.")
                found = True
                break

        if not found:
            print("Cannot find the patient with the ID", pid)

    def display_patients_list(self):
        print("ID    Name                 Disease         Gender     Age")        #display when listing patients Id,name...
        for patient in self.patients:
            print(patient)

    def write_list_of_patients_to_file(self):
        with open(r"C:\Users\arobl\OneDrive\Desktop\Python\ProjectFinal\patients.txt", "w") as file:
            for patient in self.patients:
                file.write(self.format_patient_info(patient) + "\n")

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        self.write_list_of_patients_to_file()
        print("Patient whose ID is", new_patient.pid, "has been added.")





class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            print("\nWelcome to Alberta Hospital (AH) Management system")
            print("Select from the following options, or select 3 to stop:")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit Program")

            choice = input(">>> ")

            if choice == "1":
                self.display_doctors_menu()
            elif choice == "2":
                self.display_patients_menu()
            elif choice == "3":
                print("Thanks for using the program. Bye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def display_doctors_menu(self):
        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")

            choice = input(">>> ")

            if choice == "1":
                self.doctor_manager.display_doctors_list()
            elif choice == "2":
                self.doctor_manager.search_doctor_by_id()
            elif choice == "3":
                self.doctor_manager.search_doctor_by_name()
            elif choice == "4":
                self.doctor_manager.add_dr_to_file()
            elif choice == "5":
                self.doctor_manager.edit_doctor_info()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def display_patients_menu(self):
        while True:
            print("\nPatients Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")

            choice = input(">>> ")

            if choice == "1":
                self.patient_manager.display_patients_list()
            elif choice == "2":
                self.patient_manager.search_patient_by_id()
            elif choice == "3":
                self.patient_manager.add_patient_to_file()
            elif choice == "4":
                self.patient_manager.edit_patient_info()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    management_system = Management()
    management_system.display_menu()

