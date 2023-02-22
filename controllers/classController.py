from __main__ import jsonify, db, request, render_template, redirect, url_for
from models.classModel import Class


class classController():

    @staticmethod
    def get_all_classes():
        classes = Class.query.all()
        class_dict = [class_.to_dict() for class_ in classes]
        return class_dict

    @staticmethod
    def show_class(id):
        class_ = Class.query.get(id)
        if not class_:
            return jsonify({'message': 'Class not found'}), 404
        return jsonify({'class': class_.to_dict()}), 200

    @staticmethod
    def create_class():
        name = request.form.get('name')

        new_class = Class(name=name)

        db.session.add(new_class)
        db.session.commit()

        return redirect(url_for('classes_index'))

    @staticmethod
    def update_class(id):
        class_ = Class.query.get(id)
        if not class_:
            return jsonify({'message': 'Class not found'}), 404

        name = request.form.get('name')

        class_.name = name

        db.session.commit()

        return redirect(url_for('classes_index'))

    @staticmethod
    def delete_class(id):
        class_ = Class.query.get(id)
        if not class_:
            return jsonify({'message': 'Class not found'}), 404
        db.session.delete(class_)
        db.session.commit()
        return '', 204


