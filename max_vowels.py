vowels = ('a', 'e', 'i', 'o', 'u')

def max_number_of_vowels(s, k):
    subs = s[:k]
    total = 0
    for c in subs:
        if c in vowels:
            total += 1
    maxtotal = total
    for i in range(len(s) - k):
        if s[i] in vowels:
            total -= 1
        if s[i+k] in vowels:
            total += 1
        if maxtotal < total:
            maxtotal = total
            subs = s[i+1:i+k+1]
    return subs, maxtotal

s = 'bacacbefaobeacfe'
k = 5

print(max_number_of_vowels(s, k))