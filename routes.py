from flask import Flask
from flask_cors import cross_origin

from config.templates import Templates
from utils.flask_extensions import add_url_vars
from utils.strings import Strings as s


def app_routes(app, appname):
    assert isinstance(app, Flask)
    app.t = Templates(__file__)

    # ---------------------------------------------------------------------------- #
    #                                                                              #
    #                           Landing Page                                       #
    #                                                                              #
    # ---------------------------------------------------------------------------- #
    def _run_toast(title='TITLE', msg='MESSAGE', duration=3):
        if msg != app.last_msg and title != app.last_title:
            app.last_title = title
            app.last_msg = msg
            if type(duration) == type(''):
                duration = int(duration)
            app.toaster.show_toast(title=title, msg=msg, duration=duration)
            app.sql.execute(f'INSERT INTO `{s.appname}`.`messages` (`title`, `message`, `icon_id`, `duration`) VALUES (\'{title}\', \'{msg}\', 0, {duration});')
            app.sql.commit()

    @app.route(s.slash)
    @cross_origin()
    def index():
        return """
            Testy test
        """
    add_url_vars(app, s.index, index)

    @cross_origin()
    def toast():
        _run_toast(s.appname, 'EMPTY', 1)
        return """
            Testy test
        """
    add_url_vars(app, 'toast', toast)

    @cross_origin()
    def toast_message(message):
        _run_toast(s.appname, message, 1)
        return """
            Testy test
        """
    add_url_vars(app, 'toast/<string:message>', toast_message)

    @cross_origin()
    def toast_title_message(title, message):
        _run_toast(f'{title}', f'{message}', 1)
        return """
            Testy test
        """
    add_url_vars(app, 'toast/<string:title>/<string:message>', toast_title_message)

    @cross_origin()
    def toast_title_message_duration(title, message, duration):
        _run_toast(f'{title}', f'{message}', duration)
        return """
            Testy test
        """
    add_url_vars(app, 'toast/<string:title>/<string:message>/<int:duration>', toast_title_message_duration)
