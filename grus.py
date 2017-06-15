# --------------------------------------------------------------------------- #
#                                                                             #
#                             Args Parse                                      #
#                                                                             #
# --------------------------------------------------------------------------- #
from argparse import ArgumentParser

from app import _app
from config.strings import Strings as s

parser = ArgumentParser(__file__, description=s.appname)

parser.add_argument(
    f'--development',
    '-dev',
    help=f'Dev Mode.',
    action=f'store_true'
)

parser.add_argument(
    f'--production',
    f'-prod',
    help=f'Prod Mode.',
    action=f'store_true'
)

args = parser.parse_args()

# --------------------------------------------------------------------------- #
#                                                                             #
#                               Launch                                        #
#                                                                             #
# --------------------------------------------------------------------------- #

if __name__ == s.main:
    # _app.toaster.toast_args({'msg': 'Online.'})
    # _app.sched.enter(1, 1, _app.toaster.show_toast, {'title': 'App Started', 'msg': 'Online.', 'duration': 1})
    # _app.sched.run(False)
    _app.socketio.run(_app,
                      host=_app._config.web.active.address,
                      port=_app._config.web.active.port,
                      debug=_app.debug
                      )
    # _app.run(
    #     host=_app._config.web.active.address,
    #     port=_app._config.web.active.port,
    #     debug=_app.debug,
    #     threaded=True
    # )
    # _app.toaster.close()
