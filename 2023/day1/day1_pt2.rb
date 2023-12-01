to_number = {
  'one' => 1,
  'two' => 2,
  'three' => 3,
  'four' => 4,
  'five' => 5,
  'six' => 6,
  'seven' => 7,
  'eight' => 8,
  'nine' => 9
}

input_file = File.open('input.txt')
output = 0
input_file.each_line do |line|
  regex = /(?=(\d|one|two|three|four|five|six|seven|eight|nine))/

  numbers = line.scan(regex).map do |number|
    if number[0].to_i != 0
      number[0].to_i
    else
      to_number[number[0]]
    end
  end

  output += (numbers[0].to_s + numbers[-1].to_s).to_i
end
puts output