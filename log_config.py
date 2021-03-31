from gunicorn import glogging
import logging


class CustomLogger(glogging.Logger):
    """Custom logger for Gunicorn log messages."""

    def setup(self, cfg):
        """Configure Gunicorn application logging configuration."""
        super().setup(cfg)

        # Override Gunicorn's `error_log` configuration.
        self._set_handler(
            self.error_log, cfg.errorlog, logging.Formatter(
                fmt=('timestamp=%(asctime)s pid=%(process)d '
                     'loglevel=%(levelname)s code=%(filename)s-%(funcName)s-%(lineno)s '
                     'msg=%(message)s')))
