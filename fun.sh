#!/bin/sh
CDATE=`date +%Y-%m-%d`
cat ~/dev_env/fun_desc_pattern.txt | sed -e 's/CURRENT_DATE/'$CDATE'/g'
