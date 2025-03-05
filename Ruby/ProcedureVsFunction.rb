def Get_user_name(x)
  puts x
  name = gets 
  return name
end 

def Result(x,y)
  puts x + y 
end 


def main
 # What is Procedure vs Function ?
  prompt = "Enter your name :"
  result = "So, You're:"
  name = Get_user_name(prompt)
   Result(result,name) 
end

main
# Here the Result seems like a function but it has no return still it is working so it is called procedure and in the first function which is returing the name is refered to the usual function :) 
