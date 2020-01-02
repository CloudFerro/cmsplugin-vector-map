from setuptools import setup, find_packages

setup(
    name="cmsplugin-vector-map",
    version='1.0.3',
    url='https://gitlab.mtechnology.pl/packages/django/cmsplugin-vector-map',
    packages=find_packages(where='src'),
    include_package_data=True,
    package_dir={'': 'src'},
    license='BSD',
    description="vector maps for django CMS using jqvmap.js",
    long_description=open('README.md').read(),
    author='Radosław Stępień',
    author_email='rstepien@protonmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "Django >= 1.11",
        "django-cms >= 3.4",
    ],
    zip_safe=False,
)
