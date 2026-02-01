import os
import polib


def compile_po_to_mo(po_file, mo_file):
    """
    Compile .po file to .mo file using polib
    """
    try:
        po = polib.pofile(po_file, encoding='utf-8')
        po.save_as_mofile(mo_file)
        print(f"✅ Compiled: {mo_file}")
    except Exception as e:
        print(f"❌ Failed to compile {po_file}: {e}")


try:
    import polib
except ImportError:
    print("Installing polib...")
    import subprocess

    subprocess.check_call(['pip', 'install', 'polib'])
    import polib

locales_to_compile = ['ru', 'uz', 'en']

for locale in locales_to_compile:
    po_file = f'locales/{locale}/LC_MESSAGES/messages.po'
    mo_file = f'locales/{locale}/LC_MESSAGES/messages.mo'

    if os.path.exists(po_file):
        compile_po_to_mo(po_file, mo_file)
    else:
        print(f"⚠️ File not found: {po_file}")

print("All translations compiled!")