from __main__ import jsonify, db, request, render_template, redirect, url_for, uuid
from models.studentModel import Student
from models.studentClassModel import StudentClass


class StudentController():

    @staticmethod
    def get_all_students():
        students = Student.query.all()
        students_dict = [student.to_dict() for student in students]
        return students_dict

    @staticmethod
    def show_student(id):
        student = Student.query.get(id)
        if not student:
            return jsonify({'message': 'Student not found'}), 404
        return jsonify({'student': student.to_dict()}), 200

    @staticmethod
    def create_student():
        name = request.json.get('name')
        email = request.json.get('email')
        student_number = request.json.get('student_number')

        existing_student = Student.query.filter((Student.studentNumber == student_number) | (Student.email == email)).first()
        if existing_student is not None:
            return jsonify({'message': 'Error: Dit studentnummer of email bestaat al.'})

        new_student = Student(name=name, email=email, studentNumber=student_number, role=1)
        db.session.add(new_student)
        db.session.commit()

        return jsonify({'message': 'success'})

    @staticmethod
    def update_student(id):
        student = Student.query.get(id)
        if not student:
            return jsonify({'message': 'Student not found'}), 404

        name = request.json.get('name')
        email = request.json.get('email')
        student_number = request.json.get('student_number')

        existing_student = Student.query.filter((Student.studentNumber == student_number) | (Student.email == email)).filter(Student.id != id).first()
        if existing_student is not None:
            return jsonify({'message': 'Error: Dit studentnummer of email bestaat al.'})

        # Get a list of the selected class IDs from the form data
        selected_classes = request.form.getlist('classes')

        # Update the student's name, email, and student number
        student.name = name
        student.email = email
        student.studentNumber = student_number

        # Remove any existing StudentClass objects for this student
        student.student_classes = []

        # Create StudentClass objects for the selected classes and add them to the pivot table
        for class_id in selected_classes:
            student_class = StudentClass(student_id=student.id, class_id=class_id)
            db.session.add(student_class)

        # Commit the changes to the database
        db.session.commit()

        return jsonify({'message': 'success'})
    
    @staticmethod
    def delete_student(id):
        student = Student.query.get(id)
        if not student:
            return jsonify({'message': 'Student not found'}), 404
        db.session.delete(student)
        db.session.commit()
        return '', 204

    @staticmethod
    def filter_student(input):
        if input != "null":
            search = "%{}%".format(input)

            results = Student.query.filter_by(role=1).filter(Student.name.like(search))
        else:
            results = Student.query.filter_by(role=1)

        if not results:
            return jsonify({'message': 'No results'}), 404
        results_dict = [result.to_dict() for result in results]
        return results_dict