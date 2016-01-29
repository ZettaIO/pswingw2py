from setuptools import setup

setup(
    name='pswingw2',
    version='0.2',
    url='https://github.com/ZettaIO/pswingw2py',
    download_url='https://github.com/ZettaIO/pswingw2py/archive/0.1.tar.gz',
    description="A package for sending SMS messages using the PSWinCom LINK SMS Gateway.",
    author='Einar Forselv',
    author_email='eforselv@gmail.com',
    packages=['pswingw2'],
    license='MIT',
    keywords="sms, pswin, linkmobility",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Telephony",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['pswinsms = pswingw2.shell:main'],
    },
    install_requires=['requests', 'six']
)
