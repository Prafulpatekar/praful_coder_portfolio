from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myportfolio.core_apps.portfolio'
    verbose_name = _('Portfolio')
    verbose_name_plural = _('Portfolios')
