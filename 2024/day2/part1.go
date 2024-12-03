package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func parse_input_1(filename string) [][]int {
	file, _ := os.Open(filename)
	defer file.Close()

	arr := make([][]int, 0)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Split(line, " ")
		level := make([]int, 0)
		for _, string_num := range split {
			num, _ := strconv.Atoi(string_num)
			level = append(level, num)
		}
		arr = append(arr, level)
	}
	return arr
}

func solve_1(arr [][]int) int {
	res := 0
	for _, level := range arr {
		start := level[0]
		end := level[len(level)-1]
		op := 1
		if start > end {
			op = -1
		} else if start < end {
			op = 1
		} else {
			continue
		}
		last := level[0]
		safe := 1
		for j, num := range level {
			if j == 0 {
				continue
			}
			if num*op <= last*op || num-last > 3 || last-num > 3 {
				safe = 0
				break
			}
			last = num
		}
		res += safe
	}
	return res
}
