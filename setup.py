from setuptools import setup, find_packages
setup(
    name = 'bucle',
    packages = ['bucle'],
    package_dir = {'bucle': './bucle/'},
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'bucle=bucle.scripts.run:process',
            ]
        },
)
