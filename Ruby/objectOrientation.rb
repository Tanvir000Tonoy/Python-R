class Date
  attr_accessor :day, :month, :year
end 

def main
  date = Date.new 
  date.day = gets.chomp
  date.month = gets.chomp
  date.year = gets.chomp
  puts "The date is #{date.day}/#{date.month}/#{date.year}"
end 

main
# Output: The date is 10/12/2012