package main

import (
	"regexp"
	"strconv"
	"strings"
)

func solve_2(input string) int {
	do := "do()"
	dont := "don't()"
	r, _ := regexp.Compile(`(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))`)
	matches := r.FindAllString(input, -1)
	res := 0
	enable := true
	for _, match := range matches {
		switch match {
		case do:
			enable = true
			continue
		case dont:
			enable = false
			continue
		}
		if !enable {
			continue
		}
		match = match[4 : len(match)-1]
		nums_str := strings.Split(match, ",")
		num1, _ := strconv.Atoi(nums_str[0])
		num2, _ := strconv.Atoi(nums_str[1])
		res += num1 * num2
	}
	return res
}
