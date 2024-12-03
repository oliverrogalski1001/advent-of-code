package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func parse_input_2(filename string) ([]int, map[int]int) {
	file, _ := os.Open(filename)
	defer file.Close()

	arr := make([]int, 0)
	count := make(map[int]int)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Split(line, "   ")
		num1, _ := strconv.Atoi(split[0])
		num2, _ := strconv.Atoi(split[1])
		arr = append(arr, num1)
		count[num2] += 1
	}

	return arr, count
}

func solve_2(arr []int, counts map[int]int) int {
	res := 0
	for _, num := range arr {
		res += num * counts[num]
	}
	return res
}
