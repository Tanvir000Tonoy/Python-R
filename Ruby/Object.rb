class Student
  def initialize(name, id)
    @name = name
    @id = id
  end

  def show_info
    puts "The student name is #{@name} and his ID is #{@id}"
  end
end

tanvir = Student.new("Tanvir Rahman Tonoy", "105699937")
tanvir.show_info
