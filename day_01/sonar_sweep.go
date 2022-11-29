package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func read_input(path string) ([]int16, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []int16
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		val, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return lines, err
		}
		lines = append(lines, int16(val))
	}

	return lines, scanner.Err()
}

func calc(data []int16) int {
	prev := data[0]
	inc := 0
	for _, e := range data[1:] {
		if e > prev {
			inc++
		}
		prev = e
	}
	return inc
}

func main() {
	input_fp := "day_01/input.txt"
	data, err := read_input(input_fp)
	if err != nil {
		panic(err)
	}

	sol := calc(data)
	fmt.Println("\nSolution:\t", sol)
}
