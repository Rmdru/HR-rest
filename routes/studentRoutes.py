from flask import render_template, jsonify
from controllers.studentController import StudentController


def setup_student_routes(app):
    # This route will redirect to the students index route
    @app.route("/student_overzicht")
    def students_index():
        students = StudentController.get_all_students()
        return render_template(
            "students/index.html", students=students
        )

    @app.route('/students/', methods=['POST'])
    def create_student():
        return StudentController.create_student()

    @app.route('/students/<id>', methods=['GET'])
    def show_student(id):
        return StudentController.show_student(id)

    @app.route('/students/<id>', methods=['POST'])
    def update_student(id):
        return StudentController.update_student(id)

    @app.route('/students/<id>', methods=['DELETE'])
    def delete_student(id):
        return StudentController.delete_student(id)
