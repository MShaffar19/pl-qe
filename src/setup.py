from setuptools import setup, find_packages

requirements = [
    "pip",
    "pennylane @ git+https://github.com/XanaduAI/pennylane#egg=pennylane",
]


info = {
    "name": "pl_qe",
    "packages": find_packages(where="python"),
    "package_dir": {"": "python"},
    "install_require": requirements,
}


classifiers = [
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]


setup(classifiers=classifiers, **(info))
