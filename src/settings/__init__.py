"""Config of application"""

from .database import TortoiseSettings

tortoise_config = TortoiseSettings.generate()

TORTOISE_ORM = dict(tortoise_config)

TORTOISE_ORM['apps'] = {
    'models': {
        'models': tortoise_config.modules['models'],
        'default_connection': 'default',
    }
}
TORTOISE_ORM['connections'] = dict(
    default=tortoise_config.db_url,
)
