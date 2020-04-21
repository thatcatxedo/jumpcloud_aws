from setuptools import setup

setup(
    name='jumpcloud_aws',
    version='0.1',
    packages=['jumpcloud_aws'],
    package_data={
        'jumpcloud_aws': ['config.yml']
    },
    install_requires=[
        'beautifulsoup4',
        'boto3',
        'bs4',
        'requests',
        'six',
        'click',
        'PyYAML'
    ],
    entry_points='''
        [console_scripts]
        jumpcloud_aws=jumpcloud_aws.app:cli
    ''',
    python_requires=">==3.6",
    include_package_data=True
)
