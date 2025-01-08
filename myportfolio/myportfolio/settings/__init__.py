import os.path
from pathlib import Path

from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

APP_DIR = BASE_DIR / "core_apps"

ENVVAR_SETTINGS_PREFIX = "PORTFOLIO_SETTINGS_"
LOCAL_SETTINGS_PATH = os.getenv(f"{ENVVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH")

if not LOCAL_SETTINGS_PATH:
    # We dedicate local/settings.unittests.py to have reproducible unittest runs
    LOCAL_SETTINGS_PATH = "local/settings.dev.py"

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)

include(
    "base.py",
    "logging.py",
    "aws.py",
    "custom.py",
    optional(LOCAL_SETTINGS_PATH),
    "envvars.py",
    "docker.py",
)