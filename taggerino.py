
from consts import INITAL_VERSION
from determineo import check_if_tag_exist, check_if_previous_commit_is_tagged


def determine_if_tagging_is_needed():
    if check_if_tag_exist() is None and check_if_previous_commit_is_tagged() is None:
        print("tagging needed, no tags were found on last and previous commit ")
        tagging_needed = True
    else:
        print("tag was found, no tagging needed")
        tagging_needed = False
    return tagging_needed


tagging_needed = determine_if_tagging_is_needed()
