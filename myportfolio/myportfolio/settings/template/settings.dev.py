DEBUG = True
SECRET_KEY = (
    "django-insecure-whdh!d&9b!)+a9r@-pgksjy$syx#)jx_vi)dl+onr7en=plv&^"  # noqa: Q000
)

MIDDLEWARE += ("myportfolio.utils.middleware.LoggingMiddleware",)  # type: ignore
LOGGING["formatters"]["colored"] = {  # type: ignore
    "()": "colorlog.ColoredFormatter",
    "format": "%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s",
}
LOGGING["loggers"]["myportfolio"]["level"] = "DEBUG"  # type: ignore
LOGGING["handlers"]["console"]["level"] = "DEBUG"  # type: ignore
LOGGING["handlers"]["console"]["formatter"] = "colored"  # type: ignore
