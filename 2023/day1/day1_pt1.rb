# frozen_string_literal: true

input_file = File.open('input.txt')
output = 0
input_file.each_line do |line|
  line_numbers = line.scan(/\d/).map(&:to_i)
  output += (line_numbers[0].to_s + line_numbers[-1].to_s).to_i
end
puts output