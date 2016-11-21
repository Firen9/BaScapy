from distutils.core import setup
from distutils import archive_util
from distutils import sysconfig
from distutils.command.sdist import sdist
import os

SCRIPTS = ['scapy/bin/scapy','scapy/bin/UTscapy']
# On Windows we also need additional batch files to run the above scripts
if os.name == "nt":
  SCRIPTS += ['bin/scapy.bat','bin/UTscapy.bat']

setup(
    name='BaScapy',
    version='0.2',
    packages=['scapy/scapy/','scapy/scapy/arch', 'scapy/scapy/arch/windows', 'scapy/scapy/layers','scapy/scapy/asn1','scapy/scapy/tools','scapy/scapy/modules', 'scapy/scapy/crypto', 'scapy/scapy/contrib','python-tk'],
    data_files = [('share/man/man1', ["scapy/doc/scapy.1.gz"])],
    scripts = SCRIPTS,
    url='',
    license='',
    author='Sascha Böhm',
    author_email='',
    description=''
)
