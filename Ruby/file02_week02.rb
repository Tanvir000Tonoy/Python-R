def willItChange(a,b)
	a = 100
	b = 101
  puts(a,b)
end

def main()
	a = 10
	b = 111
	puts('a ='+a.to_s(), 'b ='+b.to_s())
	willItChange(a,b)
	puts('now a =' + a.to_s()+ ' b='+b.to_s())

  # actually it did not changed the value of willItChange functions local variable value :0s
end
main()