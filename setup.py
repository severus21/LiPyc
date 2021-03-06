from distutils.core import setup
import os

setup(name="lipyc",
        version="1.0.6.dev1",
        description="A light picture manager",
        author="Laurent Prosperi",
        author_email="laurent.prosperi@ens-cachan.fr",
        url="https://github.com/severus21/LiPyc",
        platforms=["linux", "win32", "cygwin"],
        license="Apache 2.0",
        download_url="https://pypi.python.org/pypi/LiPyc",
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',  #https://pypi.python.org/pypi?%3Aaction=list_classifiers

            'Intended Audience :: End Users/Desktop',
            'Topic :: Multimedia :: Graphics :: Viewers',

            'License :: OSI Approved :: Apache Software License',

            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6'
        ],
        packages=["lipyc", "lipyc.panels", "lipyc.data", "lipyc.fs"],
        scripts = ['launcher.py'],#todo launcher to lipyc
        keywords= ["picture", "managment"],
        package_dir = {"lipyc": "src", "lipyc.data":"data"},
        requires=["PIL", "tkinter", "pycrypto", "cv2"],
        package_data={
            "lipyc.data": ["album_default.png", "file_default.png", "default-pgs.json"],
        },
    )
