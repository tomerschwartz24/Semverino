import subprocess
import logging

from consts import INITAL_VERSION

logging.basicConfig(level=logging.DEBUG)


def check_if_tag_exist():
    try:
        HEAD_TAG = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=7', 'HEAD'], text=True)
    except subprocess.CalledProcessError as no_tag_found:
        logging.error(' It seems like the latest commit does not have any tags!')
        if no_tag_found:
            return None
    if HEAD_TAG is not None:
        logging.error(' Latest commit is tagged as: {}'.format(HEAD_TAG))
        return HEAD_TAG
    
def check_if_previous_commit_is_tagged():
    try:
        PREVIOUS_TAG = subprocess.check_output(['git', 'describe', '--tags', 'HEAD~1'], text=True)
    except subprocess.CalledProcessError as no_previous_tag_found:
        logging.error(' It seems like the previous commit does not have any tags!')
        if no_previous_tag_found:
            return None
    if PREVIOUS_TAG is not None:
        logging.info(' Previous commit seems to be tagged as {}'.format(PREVIOUS_TAG))
        return PREVIOUS_TAG


check_if_previous_commit_is_tagged()
# def determine_if_tagging_is_needed():
