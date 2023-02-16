from flask import render_template, jsonify
from controllers.classController import classController


def setup_class_routes(app):
    # This route will redirect to the classes index route
    @app.route("/klassen_overzicht")
    def classes_index():
        classes = classController.get_all_classes()
        return render_template(
            "classes/index.html", classes=classes
        )

    @app.route('/classes/', methods=['POST'])
    def create_class():
        return classController.create_class()

    @app.route('/classes/<id>', methods=['GET'])
    def show_class(id):
        return classController.show_class(id)

    @app.route('/classes/<id>', methods=['POST'])
    def update_class(id):
        return classController.update_class(id)

    @app.route('/classes/<id>', methods=['DELETE'])
    def delete_class(id):
        return classController.delete_class(id)
