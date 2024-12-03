package main

import (
	"io"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func parse_input_1(filename string) string {
	file, _ := os.Open(filename)
	buf, _ := io.ReadAll(file)
	return string(buf)
}

// mul(1,2)
func solve_1(input string) int {
	r, _ := regexp.Compile(`mul\([0-9]{1,3},[0-9]{1,3}\)`)
	matches := r.FindAllString(input, -1)
	res := 0
	for _, match := range matches {
		match = match[4 : len(match)-1]
		nums_str := strings.Split(match, ",")
		num1, _ := strconv.Atoi(nums_str[0])
		num2, _ := strconv.Atoi(nums_str[1])
		res += num1 * num2
	}
	return res
}
