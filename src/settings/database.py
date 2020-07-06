"""Config of DB"""

from pydantic import Field
from src.settings.base import BaseSettings

DB_MODELS = ['src.models.user', ]
POSTGRES_DB_URL = (
    "postgres://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
)


class PostgresSettings(BaseSettings):
    """Postgres env values"""

    postgres_user: str = Field("shelter", env="POSTGRES_USER")
    postgres_password: str = Field("shelter", env="POSTGRES_PASSWORD")
    postgres_db: str = Field("shelter", env="POSTGRES_DB")
    postgres_port: str = Field("5432", env="POSTGRES_PORT")
    postgres_host: str = Field("localhost", env="POSTGRES_HOST")


class TortoiseSettings(BaseSettings):
    """Tortoise-ORM settings"""

    db_url: str
    modules: dict
    generate_schemas: bool

    @classmethod
    def generate(cls):
        """Generate Tortoise-ORM settings"""

        postgres = PostgresSettings()
        db_url = POSTGRES_DB_URL.format(**postgres.dict())
        modules = {"models": DB_MODELS}
        return TortoiseSettings(
            db_url=db_url,
            modules=modules,
            generate_schemas=True,
        )
