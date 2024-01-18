import os
from ..common.importThread import ImportThread
from ..view.studentView import StudentView
from ..model.studentModel import StudentModel
from ..model.entity.student import Student
from ..common.functions import Functions

class StudentPresenter:
    def __init__(self, view: StudentView, model: StudentModel):
        self.view = view
        self.model = model
        self.view.add_file_button.clicked.connect(self.view.openFile)
        #self.view.import_button.clicked.connect(self.fetchData)
        #self.func = 
        self.view.start_import_signal.connect(self.start_import)

    def start_import(self):
        self.view.reset_progress_bar()
        
        data = self.importData()
        self.model.set_data(data)
        self.import_thread = ImportThread(self.model)
        self.import_thread.update_progress.connect(self.view.update_progress_bar)
        self.import_thread.start()

    def fetchData(self):
        data = self.importData()
        print(data)

    def importData(self):
        #Example line : 3850;ZAFINDRABINY ELIAS.;M;385352949;Fitovinany;AMBOROMALANDY S.4;;
        filename = self.view.name_edit.text()
        myFile = open(filename, "r")
        lines = myFile.readlines()
        students = []
        students.clear()
        count = 0
        for line in lines:
            valLine = line.strip()
            count += 1
            student = valLine.split(";")
            matricule = student[0]
            level = ""
            company = matricule[0:1]
            section = matricule[1:2]
            number = matricule[2:]
            name = student[1].split(" ")
            lastname = name[0]
            firstname = name[1]
            gender = student[2]
            objStudent = Student(lastname, firstname, gender, level, company, section, number, matricule)
            students.append(objStudent)
        return students

