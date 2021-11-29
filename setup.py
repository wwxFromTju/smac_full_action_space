from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup

description = """SMAC with full action space"""

extras_deps = {
    "dev": [
        "pre-commit>=2.0.1",
        "black>=19.10b0",
        "flake8>=3.7",
        "flake8-bugbear>=20.1",
    ],
}


setup(
    name="SMAC_FULL_ACTION_SPACE",
    version="1.0.0",
    description="SMAC - StarCraft Multi-Agent Challenge.",
    long_description=description,
    author="wwx",
    author_email="wxwang@tju.edu.cn",
    license="MIT License",
    keywords="StarCraft, Multi-Agent Reinforcement Learning with full action space",
    # url="https://github.com/oxwhirl/smac",
    packages=[
        "smac_full_action_space"
    ],
    extras_require=extras_deps,
    install_requires=[
        "pysc2>=3.0.0",
        "s2clientprotocol>=4.10.1.75800.0",
        "absl-py>=0.1.0",
        "numpy>=1.10",
    ],
)
