
digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
lines = []
with open("input", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

calibration_nums = []
for line in lines:
    curr_num = 0
    min_word_dict = {}
    for num_word in digits.keys():
        num_word_i = line.find(num_word)
        if num_word_i > -1:
            min_word_dict[num_word_i] = digits[num_word]

    for num in digits.values():
        num_i = line.find(str(num))
        if num_i > -1:
            min_word_dict[num_i] = num

    max_word_dict = {}
    rev_line = line[::-1]
    for num_word in digits.keys():
        num_word_i = rev_line.find(num_word[::-1])
        if num_word_i > -1:
            max_word_dict[num_word_i] = digits[num_word]

    for num in digits.values():
        num_i = rev_line.find(str(num))
        if num_i > -1:
            max_word_dict[num_i] = num

    curr_num += 10 * min_word_dict[min(min_word_dict)]
    curr_num += max_word_dict[min(max_word_dict)]
    calibration_nums.append(curr_num)

print(calibration_nums)
print(sum(calibration_nums))

