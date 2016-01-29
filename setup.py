from setuptools import setup


def readme():
    with open('README.rst') as reader:
        return reader.read()

setup(
    name='pswingw2',
    version='0.1',
    url='https://github.com/ZettaIO/pswingw2py',
    description="A package for sending SMS messages using the PSWinCom SMS V2 Gateway.",
    author='Einar Forselv',
    author_email='eforselv@gmail.com',
    packages=['pswingw2'],
    license='MIT',
    keywords="sms, pswin, linkmobility",
    long_description=readme(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        # "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Telephony",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['pswinsms = pswingw2.shell:main'],
    }
)
