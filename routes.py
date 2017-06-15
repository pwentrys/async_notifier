from flask import Flask
from flask_cors import cross_origin

from config.strings import Strings as s
from config.templates import Templates
from utils.flask_extensions import add_url_vars


def app_routes(app, appname):
    assert isinstance(app, Flask)
    app.t = Templates(__file__)

    # ---------------------------------------------------------------------------- #
    #                                                                              #
    #                           Landing Page                                       #
    #                                                                              #
    # ---------------------------------------------------------------------------- #
    def _run_toast(title, msg, duration):
        duration = int(duration)
        app.sql.execute(f'INSERT INTO `{s.appname}`.`messages` (`title`, `message`, `icon_id`, `duration`) VALUES (\'{title}\', \'{msg}\', 0, {duration});')
        app.sql.commit()
        app.toaster.show_toast(title=title, msg=msg, duration=duration)

    def run_toast(title=s.appname, msg='EMPTY', duration='1'):
        print(f'Title: {title}')
        print(f'Message: {msg}')
        print(f'Duration: {duration}')
        # app.socketio.start_background_task(app.toaster.show_toast, **{'title': title, 'msg': msg, 'duration': duration})
        app.socketio.start_background_task(_run_toast, **{'title': title, 'msg': msg, 'duration': f'{duration}'})

    @app.route(s.slash)
    @cross_origin()
    def index():
        return """
            Testy test
        """
    add_url_vars(app, s.index, index)

    @cross_origin()
    def toast():
        #  app.socketio.start_background_task(app.toaster.show_toast, **{'msg': f'Test'})
        app.sched.enter(0.01, 0.01, run_toast, [s.appname, 'EMPTY', f'{1}'])
        app.sched.run(True)
        #  app.socketio.start_background_task(app.toaster.toast_args, {'msg': 'Test'})
        return """
            Testy test
        """
    add_url_vars(app, 'toast', toast)

    @cross_origin()
    def toast_message(message):
        app.sched.enter(0.01, 0.01, run_toast, [s.appname, message, f'{1}'])
        app.sched.run(True)
        #  app.socketio.start_background_task(app.toaster.show_toast, **{'msg': message})
        return """
            Testy test
        """
    add_url_vars(app, 'toast/<string:message>', toast_message)

    @cross_origin()
    def toast_title_message(title, message):
        app.sched.enter(0.01, 0.01, run_toast, [title, message, f'{1}'])
        app.sched.run(True)
        #  app.socketio.start_background_task(app.toaster.show_toast, **{'title': title, 'msg': message})
        return """
            Testy test
        """
    add_url_vars(app, 'toast/<string:title>/<string:message>', toast_title_message)

    @cross_origin()
    def toast_title_message_duration(title, message, duration):
        app.sched.enter(0.01, 0.01, run_toast, [title, message, f'{duration}'])
        app.sched.run(True)
        #  app.socketio.start_background_task(app.toaster.show_toast, **{'title': title, 'msg': message, 'duration': duration})
        return """
            Testy test
        """
    add_url_vars(app, 'toast/<string:title>/<string:message>/<int:duration>', toast_title_message_duration)
