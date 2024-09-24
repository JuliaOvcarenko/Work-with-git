import flask

sec_app = flask.Blueprint(
    name = 'second',
    import_name = 'second_app',
    template_folder = 'templates'
)