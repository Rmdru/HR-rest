from __main__ import render_template
from controllers.lessonController import LessonController
from controllers.classController import ClassController
def setup_lesson_routes(app):
    # This route will redirect to the lessons index route
    @app.route("/lessen_overzicht")
    def lessons_index():
        classes = ClassController.get_all_classes()
        lessons = LessonController.get_all_lessons()
        return render_template(
            "lessons/index.html", lessons=lessons, classes=classes
        )

    @app.route('/lessons/', methods=['POST'])
    def create_lesson():
        return LessonController.create_lesson()

    @app.route('/lessons/<id>', methods=['GET'])
    def show_lesson(id):
        return LessonController.show_lesson(id)

    @app.route('/lessons/<id>', methods=['POST'])
    def update_lesson(id):
        return LessonController.update_lesson(id)

    @app.route('/lessons/<id>', methods=['DELETE'])
    def delete_lesson(id):
        return LessonController.delete_lesson(id)
        
    # Route to filter lessons
    @app.route('/lessons/filter/<name>/<startDate>/<endDate>', methods=['GET'])
    def filter_lessons(name, startDate, endDate):
        return LessonController.filter_lessons(name, startDate, endDate)



