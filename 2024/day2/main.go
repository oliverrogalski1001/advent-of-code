package main

import "fmt"

func main() {
	p1 := solve_1(parse_input_1("input.txt"))
	fmt.Printf("Day 2 Part 1 = %d\n", p1)
	p2 := solve_2(parse_input_1("input.txt"))
	fmt.Printf("Day 2 Part 2 = %d\n", p2)
}
