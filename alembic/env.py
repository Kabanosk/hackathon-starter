import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from alembic import context
from src.model.tables import metadata

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
CONFIG = load_dotenv()

# Interpret the config file for Python logging.
# This line sets up loggers basically.
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = "postgresql+pg8000://"
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(get_url())

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


def get_url():
    dbuser = os.getenv("DB_USER")
    dbpass = os.getenv("DB_PASS")
    dbhost = os.getenv("DB_HOST")
    dbport = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")

    return f"postgresql://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}"


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
