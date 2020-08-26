from setuptools import setup, find_namespace_packages

setup(
    name="qcetlapi",
    version="0.1.0",
    description="Provide Swagger API for GSIQCETL",
    author="Savo Lazic",
    author_email="savo.lazic@oicr.on.ca",
    python_requires=">=3.8.0",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    package_data={"": ["swagger/api.yaml", "templates/index.html"]},
    entry_points={"console_scripts": ["qcetlapi = qcetlapi:start_server"]},
    install_requires=[
        "connexion[swagger-ui]>=2.6.0",
        "gsiqcetl@git+ssh://git@bitbucket.oicr.on.ca/gsi/gsi-qc-etl.git@v0.38.0",
    ],
    # setup_requires=["pytest-runner"],
    # tests_require=["pytest"],
    # test_suite="test",
    # extras_require={
    #    "develop": ["pre-commit>=1.18.3", "pytest>=5.2.2", "pytest-runner>=5.2"]
    # },
)
