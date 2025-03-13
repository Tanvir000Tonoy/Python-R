# Global variables
$a
$b

# Effects of global scoping (Note : no parameters!)

def change()
	$a = 10
	$b = 5
end

def main()
	$a = 2
	$b = 3
	puts('a = ' + $a.to_s() + ' b = ' + $b.to_s())
	change()
	puts('a = ' + $a.to_s() + ' b = ' + $b.to_s())
end

main()