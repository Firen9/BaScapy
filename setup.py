from distutils.core import setup

setup(
    name='BaScapy',
    version='',
    packages=['scapy/scapy/','scapy/scapy/arch', 'scapy/scapy/arch/windows', 'scapy/scapy/layers','scapy/scapy/asn1','scapy/scapy/tools','scapy/scapy/modules', 'scapy/scapy/crypto', 'scapy/scapy/contrib','python-tk'],
    data_files = [('share/man/man1', ["scapy/doc/scapy.1.gz"])],
    url='',
    license='',
    author='',
    author_email='',
    description=''
)
