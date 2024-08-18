from setuptools import setup, find_packages

setup(
    name="matilde",  # Name of your package
    version="0.1.0",  # Initial version of your package
    description="A website audit tool to ensure quality and consistency in site architecture and SEO",  # Short description
    long_description=open("README.md").read(),  # This will pull the content of your README file
    long_description_content_type="text/markdown",  # This specifies that your long description is in markdown
    author="Alex Ruco",  # Your name
    author_email="alex@ruco.pt",  # Your email
    url="https://github.com/alexruco/matilde",  # URL of your project repository
    packages=find_packages(),  # Automatically find all packages and sub-packages
    install_requires=[
        "requests>=2.25.1",  # List of dependencies your package needs
        "beautifulsoup4>=4.9.3",
        "lxml>=4.6.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # MIT License
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",  # Adjust this as your project matures
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
    ],
    python_requires=">=3.6",  # Specify the minimum Python version required
    include_package_data=True,  # Include package data as specified in MANIFEST.in or through the package_data argument
    entry_points={
        "console_scripts": [
            "matilde=matilde.main:run_audits",  # Example of how to make a script executable from the command line
        ],
    },
)
