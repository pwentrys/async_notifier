from win10toast import ToastNotifier
from config.utils import from_args_fallback as ff, from_args_fallback_int as ffi
from config.strings import Strings as s
import os
import asyncio


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
            self.socketio.start_background_task(self.t.show_toast, {'title': Toaster.DEFAULT_TITLE, 'msg': 'Online.'})
        # self.t.show_toast(title=Toaster.DEFAULT_TITLE, msg='Online.')

    def close(self):
        if self.socketio:
            self.socketio.start_background_task(self.t.show_toast, {'title': Toaster.DEFAULT_TITLE, 'msg': 'Offline.'})
        # self.t.show_toast(title=Toaster.DEFAULT_TITLE, msg='Offline.')

    def show_default_toast(self):
        self.t.show_toast("Hello World!!!",
                           "Python is awsm by default!")

    def toast_custom(self, args):
        self.t.show_toast(f'Custom Toast',
                          f'{args.get("message", "ERROR")}'
                          )

    def toast_args(self, args):
        if self.socketio:
            print(f'Toast Args - Start')
            title = ff(args, 'title', Toaster.DEFAULT_TITLE)
            msg = ff(args, 'msg', Toaster.DEFAULT_MSG)
            duration = ffi(args, 'duration', Toaster.DEFAULT_DURATION)
            self.t.show_toast(title=title, msg=msg, duration=duration)
            print(f'Toast Args - End')
        # self.t.show_toast(title=title,
        #                   msg=msg,
        #                   duration=duration
        #                   )

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
