package main

import (
	"bufio"
	"os"
	"slices"
	"strconv"
	"strings"
)

func parse_input_1(filename string) ([]int, []int) {
	file, _ := os.Open(filename)
	defer file.Close()

	arr1 := make([]int, 0)
	arr2 := make([]int, 0)

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Split(line, "   ")
		num1, _ := strconv.Atoi(split[0])
		num2, _ := strconv.Atoi(split[1])
		arr1 = append(arr1, num1)
		arr2 = append(arr2, num2)
	}

	return arr1, arr2
}

func solve_1(arr1 []int, arr2 []int) int {
	res := 0
	slices.Sort(arr1)
	slices.Sort(arr2)
	for i := range len(arr1) {
		res += max(arr1[i], arr2[i]) - min(arr1[i], arr2[i])
	}
	return res
}
