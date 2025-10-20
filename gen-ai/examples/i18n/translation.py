"""An example of using a translation catalog.

Authors:
    Dimitrij Ray (dimitrij.ray@gdplabs.id)

References:
    [1] https://gdplabs.gitbook.io/sdk/how-to-guides/get-started-with-translations
"""

from gllm_intl import _, configure_i18n, set_locale
from gllm_intl.translation.providers import FileSystemLocaleProvider

def main():
    """Configure i18n and set locale to Indonesian."""
    configure_i18n(FileSystemLocaleProvider(locales_dir="./locales"))
    set_locale("id_ID")
    print(_("greeting"))

if __name__ == "__main__":
    main()
