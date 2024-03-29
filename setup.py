from pathlib import Path

from setuptools import find_packages, setup

readme = Path(__file__).parent / 'README.md'

setup(
    name='hyp3_ci',
    use_scm_version=True,
    description='HyP3 plugin for ci processing',
    long_description=readme.read_text(),
    long_description_content_type='text/markdown',

    url='https://github.com/ASFHyP3/hyp3-ci',
    project_urls={
        'Documentation': 'https://hyp3-docs.asf.alaska.edu',
    },

    author='ASF APD/Tools Team',
    author_email='uaf-asf-apd@alaska.edu',

    license='BSD',
    include_package_data=True,

    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],

    python_requires='~=3.8',

    install_requires=[
        'hyp3lib>=3,<4',
    ],

    extras_require={
        'develop': [
            'flake8',
            'flake8-import-order',
            'flake8-blind-except',
            'flake8-builtins',
            'pytest',
            'pytest-cov',
            'pytest-console-scripts',
        ]
    },

    packages=find_packages(),

    entry_points={'console_scripts': [
            'hyp3_ci = hyp3_ci.__main__:main',
            'proc_ci = hyp3_ci.process:main',
        ]
    },

    zip_safe=False,
)
