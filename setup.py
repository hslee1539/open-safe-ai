from setuptools import setup, find_packages

setup(
    name="open-safe-ai",
    version="0.0.1",
    description="",
    author="hslee1539",
    author_email="hslee1539@gmail.com",
    url="https://github.com/hslee1539/open-safe-ai",
    py_modules=["open_safe_ai"],
    install_requires=[
        "fastapi",
        "typer",
        "mlx",
        "mlx_lm"
    ],
    entry_points={
        'console_scripts': [
            'open-safe-ai=open_safe_ai:main',
        ],
    }
)