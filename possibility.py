with open('twitter-out.txt') as f:
    x = [l.strip() for l in f]

pos = x.count('pos')
neg = x.count('neg')
total = pos+neg
print("total sample : " + str(total))
print("positive sample : " + str(pos))
print("negative sample : " + str(neg))
print("Possibility of Tax Evasion : " + str(pos*100/total) + str('%'))
