from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST: str | None = os.environ.get('DB_HOST')
DB_PORT: str | None = os.environ.get('DB_PORT')
DB_NAME: str | None = os.environ.get('DB_NAME')
DB_USER: str | None = os.environ.get('DB_USER')
DB_PASS: str | None = os.environ.get('DB_PASS')

DB_HOST_TEST: str | None = os.environ.get('DB_HOST_TEST')
DB_PORT_TEST: str | None = os.environ.get('DB_PORT_TEST')
DB_NAME_TEST: str | None = os.environ.get('DB_NAME_TEST')
DB_USER_TEST: str | None = os.environ.get('DB_USER_TEST')
DB_PASS_TEST: str | None = os.environ.get('DB_PASS_TEST')

SECRET: str | None = os.environ.get('SECRET')
