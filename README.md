
# Python Centralized Logger

A Python library for centralized JSON logging. 

## Installation

Install directly from the repository:

```bash
pip install git+https://github.com/useralreadyinuse/python-centralized-logger.git
```

## Usage

```python
from centralized_logger import CentralizedLogger

config = {
    'name': 'example_logger',
    'level': 'INFO',
    'format': '%(timestamp)s %(levelname)s %(message)s',
}
CentralizedLogger(config)
logger = CentralizedLogger.get_logger()

logger.info("This is a log message")
```

## License

This project is licensed under the MIT License.
