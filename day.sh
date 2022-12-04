#!/usr/bin/env bash

day="$@"
dayString="day${day}"
if [[ -e "$dayString" ]]; then
	echo "file already exists"
else
	if [[ day -ge 1 && day -le 25 ]]; then
		mkdir "$dayString"
		cd "$dayString"
		touch input input_test
		touch "${dayString}-1.py" "${dayString}-2.py"
		echo "${dayString} succesfully created"
	else
		echo "invalid day number"
	fi
fi
