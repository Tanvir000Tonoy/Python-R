class Demo
	def first_procedure(arg)
		@shared_variable = arg
		second_procedure()
	end

	# note this procedure accesses shared_variable even though it is not passed 
	# as a parameter/argument:
	def second_procedure()
		puts("The shared variable has the value: #{@shared_variable}")
	end
end

def main()
	demo = Demo.new().first_procedure(42)
end

main()