from distutils.core import setup
import os
from phonenumber_field import __version__


packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('phonenumber_field'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[11:] # Strip "currencies/" or "currencies\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))
            

setup(
    name="django-phonenumber-field",
    version = __version__,
    url='http://github.com/stefanfoulis/django-phonenumber-field',
    license='BSD',
    platforms=['OS Independent'],
    description="An international phone number field for django models.",
    setup_requires = [
        'versiontools >= 1.4',
    ],
    install_requires = [
        'phonenumbers',
    ],
    long_description=open('README.rst').read(),
    author='Stefan Foulis',
    author_email='stefan.foulis@gmail.com',
    maintainer='Stefan Foulis',
    maintainer_email='stefan.foulis@gmail.com',
    package_dir={'phonenumber_field': 'phonenumber_field'},
    packages=packages,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
