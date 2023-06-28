#!/bin/bash

total_rows=0
total_time=0

for year in {2018..2021}
do
  for month in {1..12}
  do
	echo "Loading flights_data/raw/Flights_${year}_${month}.csv"
	start=`date +%s`
	python3 ILP_csv.py $1 9009 flights_data/raw/Flights_${year}_${month}.csv
	end=`date +%s`
	rows=`wc -l flights_data/raw/Flights_${year}_${month}.csv | cut -d" " -f1`
	rows=$((${rows}-1))
	total_rows=$((${total_rows}+${rows}))
	total_time=$((${total_time}+${end}-${start}))
	rows_per_sec=$((${rows}/(${end}-${start})))
	echo "Loaded ${rows} rows at ${rows_per_sec} rows per second."
  done
done

total_rows_per_sec=$((${total_rows}/${total_time}))
echo "All together, loaded ${total_rows} rows at ${total_rows_per_sec} rows per second."
