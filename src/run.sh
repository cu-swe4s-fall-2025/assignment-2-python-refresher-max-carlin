#!/bin/bash

echo "Running print fires the correct way:"
python print_fires.py --country 'United States of America' --country_column 0 --fires_column 'Forest fires' --file_name 'Agrofood_co2_emission.csv'

echo "Running print fires with a fake filename (will fail):"
python print_fires.py --country 'United States of America' --country_column 0 --fires_column 'Forest fires' --file_name 'nonexistentdata.csv'

echo "Running print fires with a column that doesn't exist (will fail):"
python print_fires.py --country 'United States of America' --country_column 0 --fires_column 'Fake Fires Column' --file_name 'Agrofood_co2_emission.csv'
