from .settings import project
from second_app import sec_app, render_sec

sec_app.add_url_rule(
    rule = '/',
    view_func = render_sec
)
project.register_blueprint(blueprint = sec_app)