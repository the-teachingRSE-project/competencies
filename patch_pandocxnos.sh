#!/usr/bin/env bash

# Patches the suboptimal definition of valid versions in pandocxnos
# See 3 identical! and unmerged PRs in https://github.com/tomduck/pandoc-xnos/pulls. The repo doesn't seem to be maintained anymore.
# Here we fix the same thing, just better ;-).

sed -i s/'pattern = re.compile(r'\''^\[1-2\]\\\.\[0-9\]+(?:\\\.\[0-9\]+)?(?:\\\.\[0-9\]+)?\$'\'')'/'pattern = re.compile(r'\''^\[1-9\]+\\\.\[0-9\]+(?:\\\.\[0-9\]+)?(?:\\\.\[0-9\]+)?\$'\'')'/ \
 $(find . -ipath  */pandocxnos/core.py)
