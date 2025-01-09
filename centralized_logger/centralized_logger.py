
import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime, timezone

class CentralizedJsonFormatter(jsonlogger.JsonFormatter):
    """Custom JSON formatter to structure logs."""

    def add_fields(self, log_record, record, message_dict):
        super(CentralizedJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['timestamp'] = log_record.get('timestamp') or datetime.now(timezone.utc).isoformat()
        log_record['severity'] = record.levelname

class CentralizedLogger:
    """Singleton logger class for centralized JSON logging."""
    _instance = None

    def __new__(cls, config=None):
        if not cls._instance:
            cls._instance = super(CentralizedLogger, cls).__new__(cls)
            cls._instance._configure(config)
        return cls._instance

    def _configure(self, config):
        """Configure the logger with handlers and formatters."""
        self.logger = logging.getLogger(config.get('name', 'centralized_logger'))
        self.logger.setLevel(config.get('level', logging.DEBUG))

        # Remove existing handlers
        for handler in list(self.logger.handlers):
            self.logger.removeHandler(handler)

        # Add a stream handler with JSON formatting
        json_handler = logging.StreamHandler()
        json_formatter = CentralizedJsonFormatter(config.get('format', '%(timestamp)s %(levelname)s %(message)s'))
        json_handler.setFormatter(json_formatter)
        self.logger.addHandler(json_handler)

        # Optional: Add file handler if specified
        if 'file' in config:
            file_handler = logging.FileHandler(config['file'])
            file_handler.setFormatter(json_formatter)
            self.logger.addHandler(file_handler)

    @staticmethod
    def get_logger():
        """Return the configured logger instance."""
        if CentralizedLogger._instance is None:
            raise Exception("Logger not configured. Instantiate CentralizedLogger first.")
        return CentralizedLogger._instance.logger
