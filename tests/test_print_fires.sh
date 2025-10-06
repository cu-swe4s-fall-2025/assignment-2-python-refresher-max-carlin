#!/bin/bash
test -e ssshtest || curl -s -O https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

SCRIPT=src/print_fires.py
DATA=tests/test.csv

run print_fires_success python $SCRIPT --country 'United States of America' --country_column 0 --fires_column 'Forest fires' --file_name $DATA
assert_stdout
assert_exit_code 0

run print_fires_wrong_csv python $SCRIPT --country 'United States of America' --country_column 0 --fires_column 'Forest fires' --file_name 'nonexistent.csv'
assert_no_stderr
assert_exit_code 1

run print_fires_wrong_column python $SCRIPT --country 'United States of America' --country_column 0 --fires_column 'NotACOlumn' --file_name 'nonexistent.csv'
assert_no_stderr
assert_exit_code 1

run print_fires_mean_success python $SCRIPT --country 'United States of America' --country_column 0 --fires_column 'Forest fires' --file_name $DATA --operation 'mean'
assert_in_stdout 1925.8666666666666
assert_exit_code 0

run print_fires_mean_success python $SCRIPT --country 'United States of America' --country_column 0 --fires_column 'Forest fires' --file_name $DATA --operation 'median'
assert_in_stdout 1555.5
assert_exit_code 0

run print_fires_mean_success python $SCRIPT --country 'United States of America' --country_column 0 --fires_column 'Forest fires' --file_name $DATA --operation 'std'
assert_in_stdout 1024.276516484793
assert_exit_code 0



