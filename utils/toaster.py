from win10toast import ToastNotifier

from config.utils import from_args_fallback as ff, from_args_fallback_int as ffi
from utils.strings import Strings as s


class Toaster:
    DEFAULT_DURATION = 1
    DEFAULT_MSG = ''
    DEFAULT_TITLE = s.appname
    DEFAULT_ICON = 'static\\icon.png'

    def __init__(self):
        self.t = ToastNotifier()
        self.socketio = ''
        self.open()

    def open(self):
        if self.socketio:
            self.socketio.start_background_task(
                self.t.show_toast,
                {'title': Toaster.DEFAULT_TITLE, 'msg': 'Online.'})

    def close(self):
        if self.socketio:
            self.socketio.start_background_task(
                self.t.show_toast,
                {'title': Toaster.DEFAULT_TITLE, 'msg': 'Offline.'})

    def toast_args(self, args):
        title = ff(args, 'title', Toaster.DEFAULT_TITLE)
        msg = ff(args, 'msg', Toaster.DEFAULT_MSG)
        duration = ffi(args, 'duration', Toaster.DEFAULT_DURATION)
        try:
            if self.socketio:
                self.socketio.start_background_task(
                    self.t.show_toast,
                    {'title': Toaster.DEFAULT_TITLE, 'msg': 'Online.'})
            else:
                self.t.show_toast(title=title, msg=msg, duration=duration)
        except Exception as error:
            print(error)

    def toast_title(self, title):
        self.t.show_toast(
            title=title,
            msg=''
        )

    def toast_body(self, msg):
        self.t.show_toast(
            title='',
            msg=msg
        )

    def toast_titlebody(self, title, msg):
        self.t.show_toast(
            title=title,
            msg=msg
        )

    def toast_titlebodyicon(self, title, msg, icon_path):
        self.t.show_toast(
            title=title,
            msg=msg,
            icon_path=icon_path
        )

    def toast_titlebodyicondur(self, title, msg, icon_path, duration):
        self.t.show_toast(
            title=title,
            msg=msg,
            icon_path=icon_path,
            duration=int(duration)
        )
