import subprocess
import logging
import sys

from consts import INITAL_VERSION


def check_if_tag_exist():
    try:
        HEAD_TAG = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=7', 'HEAD'])
    except subprocess.CalledProcessError as no_tag_found:
        logging.error('It seems like the latest commit does not have any tags!')
        if no_tag_found:
            return None
    if HEAD_TAG is not None:
        return HEAD_TAG