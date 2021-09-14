import logging.config
import os
import sys

__all__ = ['log']

entrypoint_path = os.path.dirname(sys.argv[0])
log_path = os.path.join(entrypoint_path, 'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)

conf_path = os.path.join(entrypoint_path, 'conf', 'logging.conf')
if os.path.exists(conf_path):
    logging.config.fileConfig(conf_path)
    log = logging.getLogger('root')
else:
    logging.basicConfig(level=logging.INFO)
    log = logging.root