from django.utils.translation import ugettext_lazy
try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    name = 'pretix_ldap'
    verbose_name = 'pretix LDAP'

    class PretixPluginMeta:
        name = ugettext_lazy('pretix LDAP')
        author = 'sohalt'
        description = ugettext_lazy('LDAP authentication backend for pretix')
        visible = True
        version = '1.0.0'
        compatibility = "pretix>=3.3.0"

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_ldap.PluginApp'
