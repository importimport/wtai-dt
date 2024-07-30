from setuptools import setup, find_packages

with open('readme.rst') as f:
    readme = f.read()

setup(
    name="wtai-dt",
    packages=find_packages(),
    version='0.0.2',
    description="turbine ai and digital twin",
    long_description=readme,
    author="hnust",
    author_email='2538134102@qq.com',
    url="https://github.com/coco369/aliyun-api-gateway-python",
    download_url='https://github.com/coco369/aliyun-api-gateway-python',
    keywords=['command', 'line', 'tool'],
    classifiers=["Programming Language :: Python :: 3"],
    include_package_data=True,
    entry_points={
        'console_scripts': [
			"fastspider=fastspider.start:main"
        ]
    },
    install_requires=[
        'python3.7.6',
    ]
)