from setuptools import setup, find_packages

setup(
    name='GravityAIInferenceSDK',
    version='0.1',
    author='Priyanka Marathe',
    author_email='priyanka.marathe@gravity-ai.com',
    description='SDK for interacting with the Gravity AI Inference API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/GravityAiInferenceSDK',
    packages=find_packages(),
    install_requires=[
        'requests>=2.26.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
