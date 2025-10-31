#clase que me permite tener mensajes en la terminal dando detalles en tiempo real
# de lo que pas aen el sistema
# para utilziarlo tienes que mandarlo a llmar en las clases que los requieres
import logging
import logging.config
from datetime import datetime
import os

# Crear un directorio para guardar los logs si no existe
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Nombre dinámico del archivo de log basado en la fecha
LOG_FILE = os.path.join(LOG_DIR, f"app_{datetime.now().strftime('%Y-%m-%d')}.log")

# Configuración básica de logging
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detailed": {
            "format": "%(asctime)s [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
        },
        "simple": {
            "format": "%(asctime)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "detailed",
            "filename": LOG_FILE,
            "encoding": "utf-8",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    },
    "loggers": {
        "my_app": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False,
        },
    },
}

# Configurar logging
logging.config.dictConfig(LOGGING_CONFIG)

def get_logger(name: str):
    """
    Obtiene un logger configurado con el nombre especificado.
    """
    return logging.getLogger(name)
