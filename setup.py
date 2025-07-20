from setuptools import setup, find_packages

setup(
    name="quan_cryptor",
    version="5.1.0-alpha.1",
    description="Simple client-server chat with post-quantum assymetric encryption.",
    author="SeniorShadifer",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests==2.32.3",
        "cryptography==44.0.2",
        "loguru==0.7.3",
        "platformdirs==4.3.8",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.0",
    entry_points={
        "console_scripts": ["server=server.main:main", "client=client.main:main"]
    },
)
