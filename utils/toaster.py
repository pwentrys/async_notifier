from win10toast import ToastNotifier
from config.utils import from_args_fallback as ff, from_args_fallback_int as ffi
import os
import asyncio


class Toaster:
    DEFAULT_DURATION = 1
    DEFAULT_MSG = ''
    DEFAULT_TITLE = 'Andromeda'
    DEFAULT_ICON = 'static\\icon.png'

    def __init__(self):
        self.t = ToastNotifier()
        self.loop = asyncio.get_event_loop()
        self.nextend = self.loop.time
        self.loop.run_forever()

    def close(self):
        self.t.show_toast(title=Toaster.DEFAULT_TITLE, msg='Offline.')
        if not self.loop.is_closed():
            self.loop.close()

    def show_default_toast(self):
        self.t.show_toast("Hello World!!!",
                           "Python is awsm by default!")

    def toast_custom(self, args):
        self.t.show_toast(f'Custom Toast',
                          f'{args.get("message", "ERROR")}'
                          )

    @staticmethod
    def _toast_args(args, loop):
        t = args['t']
        title = ff(args, 'title', Toaster.DEFAULT_TITLE)
        msg = ff(args, 'msg', Toaster.DEFAULT_MSG)
        duration = ffi(args, 'duration', Toaster.DEFAULT_DURATION)
        lt = loop.time()
        if lt > t.nextend:
            t.nextend = lt + duration
            t.show_toast(title=title,
                         msg=msg,
                         duration=duration
                         )
        else:
            loop.call_later(t.nextend - lt, Toaster._toast_args, args, loop)

    def toast_args(self, args):
        args['t'] = self
        self.loop.call_soon(Toaster._toast_args, args, self.loop)

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
