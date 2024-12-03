package main

func solve_2(arr [][]int) int {
	res := 0
	for _, level := range arr {
		safe, i := is_safe(level)
		if !safe {
			level1 := append(append([]int{}, level[:i]...), level[i+1:]...)
			level2 := append(append([]int{}, level[:i-1]...), level[i:]...)
			safe1, _ := is_safe(level1)
			safe2, _ := is_safe(level2)
			if safe1 || safe2 {
				res += 1
			}
		} else {
			res += 1
		}
	}
	return res
}

func is_safe(level []int) (bool, int) {
	start := level[0]
	end := level[len(level)-1]
	op := 1
	if start > end {
		op = -1
	} else if start < end {
		op = 1
	}
	last := level[0]
	for j, num := range level {
		if j == 0 {
			continue
		}
		if num*op <= last*op || num-last > 3 || last-num > 3 {
			return false, j
		}
		last = num
	}
	return true, 0
}
