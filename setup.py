from setuptools import setup, find_packages

setup(
    name="colored_slack_log_handler",
    version="0.0.1",
    packages=find_packages(),
    description=("Python color-coding Slack log handler"),
    author="shibataka000",
    author_email="chise.alter.pasta@gmail.com",
    url="https://github.com/shibataka000/colored_slack_log_handler",
    license="",
    keyword="slack",
    install_requires=["requests"],
    setup_requires=["pytest-runner", "flake8"],
    tests_requires=["pytest", "mock"],
)
