import subprocess

from determineo import check_if_tag_exist, check_if_previous_commit_is_tagged
from helpers.logger import setup_logger
from consts import INITAL_VERSION

logger = setup_logger('taggerino-logger')

def determine_if_tagging_is_needed():
    if check_if_tag_exist() is None and check_if_previous_commit_is_tagged() is None:
        logger.info("tagging needed, no tags were found on last and previous commit ")
        tagging_needed = True
    else:
        logger.warning("tag was found, no tagging needed")
        tagging_needed = False
    return tagging_needed

def tag_if_needed(tagging_needed=False):
    if tagging_needed:
        tagger()

def tagger():
    subprocess.run(['git', 'tag', '{}'.format(INITAL_VERSION)])
    logger.info("Tagged HEAD with inital version {}".format(INITAL_VERSION))

    
def main():
    tagging_needed = determine_if_tagging_is_needed()
    tag_if_needed(tagging_needed)
    
main()