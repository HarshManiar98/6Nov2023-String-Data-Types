# string interpolation Methods
#  1) the first method is is the format()

w1 = "Harsh"
w2 = "Python"

msg = "my name is {} i am learning {}"

print(msg.format(w1,w2))


# Philistine is my Country i love Philistine

h1 = "Philistine"
h2 = "love"
h3 = "Supporting"

msg2 = "{} is my Country i {} Philistine people and i am {} the Philistine "

print(msg2.format(h1,h2,h3))


# Ronaldo is the Football Player and Ronaldo love  and support Philistine

e1 = "Ronaldo"
e2 = "Philistine"

msg3 ="{} is the Football Player and Ronaldo love and support {}"


print(msg3.format(e1,e2))

# 2) the second method of f string method in variable subsituation method 
#  f String is the literal string interpolation  

y1 = "Anil Doller"
y2 = "Python"

print(f"I am learning {y2} from {y1} sir")

#  the Elon Musk is the Multibillnare and He is the Boss of Space X and Tesla
j1 = "Elone Musk"
j2 = "Space X and Tesla"

print(f'{j1} is the Multibillnare and He is the Boss of {j2}')


# 3)  method is is % formatting

# The Monkey like a Banana and Lion like A Meat Of any animal 

k1 = " Monkey"
K2 = " Lion"

print(" The %s like a Banana and %s like A Meat of any animal"%(k1,K2))


l1 = "Teacher"
l2 = "student"

print('The %s Teach the Student and %s is listning the Teacher'%(l1,l2))