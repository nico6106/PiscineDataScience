from statistics import ft_statistics


ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
print("-----")

ft_statistics(1, toto="mean", tutu="median", tata="quartile", hello="std", world="var")
print("-----")

ft_statistics(0, toto="mean", tutu="median", tata="quartile", hello="std", world="var")
print("-----")

ft_statistics('1', toto="mean", tutu="median", tata="quartile", hello="std", world="var")
print("-----")

ft_statistics(-156, 145, toto="mean", tutu="median", tata="quartile", hello="std", world="var")
print("-----")

ft_statistics(-156, 145, 1, toto="mean", tutu="median", tata="quartile", hello="std", world="var")
print("-----")

ft_statistics(-2147483649, 2147483647, 2147483648, tito=15, toto="mean", tutu="median", tata="quartile", hello="std", world="var", fe="fee")
print("-----")

ft_statistics(-156, 1, 2, tutu="quartile")
print("-----")

ft_statistics(-156, 145, 1, 2, tutu="quartile")
print("-----")

ft_statistics(-156, 145, 1, 2, 5, tutu="quartile")
print("-----")
