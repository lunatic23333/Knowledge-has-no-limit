# ex1 第一个程序
print("ex1 第一个程序")
print("Hello World")
print("Hello Again")
print("I like typing this")
print("Yay Printing")
print("I'd much rather you 'not'.")
print("I'd said do not touch this\n\n\n")


# ex2 注释和#号
print("ex2 注释和#号")
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.
print("I could have code like this.")   # and the comment after 13
# You can also use a comment to "disable" or comment out code
# print("this won't run,")
print("This will run.\n\n\n")


# ex3 数字和数学
print("ex3 数字和数学")
print("I will now count my chickens:")  # chicken
print("Hens", 25 + 30 / 6)              # hen
print("Roosters", 100 - 25 * 3 % 4)     # rooster

print("Now I will count the eggs:")     # egg
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 - 7?")    # boolean
print(3 + 2 < 5 - 7)
print("what is 3 + 2？", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("How about some more.")
print("Is it greater?", 5 > -2)            # boolean
print("Is it greater or equal?", 5 > -2)
print("Is it less or equal?", 5 < -2, "\n\n\n")


# ex4 变量和名字
print("变量和名字 ")
cars = 100
space_in_a_car = 4.0  # 赋予了4.0，而不是4，因为想要得到浮点数
drivers = 30
passengers = 90
cars_not_driven = cars - drivers        # "="表示赋值,"==“表示判断
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.\n\n\n")


# 更多变量和打印
print("更多变量和打印")
my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounfs heavy.")
print("Actually that's not too heacy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tiricky, try to get it excatly right.
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.\n\n\n")
# 变量名不允许用数字开头，允许用下划线，允许用大小写字母
# 可以用round()函数对数字进行四舍五入


# ex6 字符串和文本
print("ex6 字符串和文本")
types_of_people = 10
x = f"There are {types_of_people} types of people."     # 第一处

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"   # 第二处

print(x)
print(y)

print(f"I said: {x}")                                   # 第三处
print(f"I also said: '{y}'")                            # 第四处

hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarious))                # 第五处

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e, "\n\n\n")


# ex7 更多打印
print("ex7 更多打印")
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))         # 格式化字符串,实现字符串的替换
print("And everywhere that Mary went")
print("." * 10)                             # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"                                # 定义变量

# watch that comma at the end. try removing it to see what h
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')      # 字符串拼接
print(end7 + end8 + end9 + end10 + end11 + end12)
print("\n\n\n")


# ex8 打印打印
print("ex8 打印打印")
formatter = "{} {} {} {}"                                 # 定义变量

print(formatter.format(1, 2, 3, 4))                 # 格式化字符串
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here\n",
    "Maybe a poem\n",
    "Or a song about fear\n\n\n"
))

# ex9 打印 打印 打印
print("ex9 打印 打印 打印")
# Here's some new strage stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:", days)               # 字符串拼接
print("Here are the months:", months)           # 字符串拼接

print("""
There's something going on here.
With the three double- quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""", "\n\n\n")                                   # 多行字符串


# ex10 哪是什么？
print("ex10 哪是什么？")
tabby_cat = "\tI'm tabbed in."              # \t
persion_cat = "I'm split\non a line."       # \n
backslash_cat = ("I'm \\ a \\ cat.")        # \

fat_cat = """                               # 多行字符串
I'll do a list
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persion_cat)
print(backslash_cat)
print(fat_cat)
