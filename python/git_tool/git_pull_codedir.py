#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : git_pull_codedir.py
## Author : Denny <contact@dennyzhang.com>
## Description :
## Sample:
##          python git_pull_codedir.py --code_dirs "/data/code_dir/repo1,/data/code_dir/repo2"
## Dependency:
##        pip install GitPython
## --
## Created : <2017-03-24>
## Updated: Time-stamp: <2017-09-04 18:55:31>
##-------------------------------------------------------------------
import os, sys
import sys
import logging
import argparse
# Notice: Need to run: pip install GitPython
import git

log_folder = "%s/log" % (os.path.expanduser('~'))
if os.path.exists(log_folder) is False:
    os.makedirs(log_folder)
log_file = "%s/%s.log" % (log_folder, os.path.basename(__file__).rstrip('\.py'))
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.getLogger().addHandler(logging.StreamHandler())

def git_pull(code_dir):
    logging.info("Run git pull in %s" %(code_dir))
    if os.path.exists(code_dir) is False:
        logging.error("Code directory(%s): doesn't exist" % (code_dir))
        sys.exit(1)
    os.chdir(code_dir)
    g = git.cmd.Git(code_dir)
    output = g.pull()
    return output

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--code_dirs', required=True, \
                        help="Code directories to pull. If multiple, separated by comma", type=str)
    l = parser.parse_args()
    code_dirs = l.code_dirs

    separator = ","
    for code_dir in code_dirs.split(separator):
        git_output = git_pull(code_dir)
        # print(git_output)
        if git_output == 'Already up-to-date.':
            has_changed = False
        else:
            has_changed = True
            logging.info("Code has changed in %s. Detail: %s" % (code_dir, git_output))

    if has_changed is True:
        sys.exit(1)
    else:
        sys.exit(0)
## File : git_pull_codedir.py ends
