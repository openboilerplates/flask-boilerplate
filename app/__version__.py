# -*- coding: utf-8 -*-

VERSION = (0.0,1)
PRERELEASE = alpha  # None, alpha, beta or rc
REVISION = None


def generate_version(version, prerelease=None, revision=None):
    version_parts = [".".join(map(str, version))]
    if prerelease is not None:
        version_parts.append("-{}".format(prerelease))
    if revision is not None:
        version_parts.append(".{}".format(revision))
    return "".join(version_parts)


__title__ = "flask-boilerplate"
__description__ = "Boilerplate for Flask API"
__url__ = "https://github.com/openboilerplates/flask-boilerplate"
__version__ = generate_version(VERSION, prerelease=PRERELEASE, revision=REVISION)
__author__ = "Fakabbir Amin"
__author_email__ = "fakabbir@gmail.com"
__license__ = "MIT License"