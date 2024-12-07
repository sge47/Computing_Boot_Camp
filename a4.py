'''
1. Given an integer variable `x`, write a conditional statement that will assign
to a variable `s` the string value `"POSITIVE"`, `"NEGATIVE"`, or `"ZERO"`
(depending on whether `x` is positive, negative, or zero, respectively). Assume
`x` has the value 2 for the purposes of this prompt (but also try plugging
in the values 0 and -1 for x, to ensure that your conditional statements are
written correctly).
'''

x = 2
if x > 0:
    s = "POSITIVE"
elif x < 0:
    s = 'NEGATIVE'
else:
    s = 'ZERO'
s

'''
2. Given integer variables `lb`, `ub`, `p`, and `q`, write a loop that will
count how many numbers between `lb` and `ub` (inclusive) are divisible by both
`p` and `q`. For the purposes of this prompt, assume that `p` is 2 and `q` is 3.
Also assume that `lb` is 1 and `ub` is 20. Thus, your result should be 3
(because only 6, 12, and 18 are divisible by both 2 and 3).
'''
p = 2
q = 3
lb = 1
ub = 20

count = 0
for i in range(lb, ub + 1):
    if ((i % p == 0) and (i % q == 0)):
        count += 1
    print(count)


'''
3. Given a list of integers `lst`, write a loop to count the number of negative
numbers in the list. Assume `lst` has the value `[-1, 2, -3, 4, 0]` for the
purposes of this prompt. Thus, your result should be 2 (because only -1 and -3
are negative numbers).
'''
lst = [-1, 2, -3, 4, 0]

count = 0
for i in lst: 
    if i < 0:
        count += 1
print(count)


'''
4. Write a loop to compute a variable `all_pos` that has the value `True` if
all of the elements in a list of integers `lst` are positive and `False`
otherwise. Again, assume `lst` has the value `[-1, 2, -3, 4, 0]` for the
purposes of this prompt.
'''
lst = [-1, 2, -3, 4, 0]
all_pos = True

for i in lst:
    if i < 0:
        all_pos = False
print(all_pos)


'''
5. Given a list of keys and a list of values, use a loop to construct a
dictionary that maps the ith key in the list of keys to the ith value in the
list of values. For the purposes of this prompt, assume that the list of keys
is `["x", "y", "z"]` and the list of values is `[10, 20, 30]`.
'''
k = ["x", "y", "z"]
v = [10, 20, 30]

dictionary = {}

for i in range(len(k)):
    dictionary[k[i]] = v[i]
print(dictionary)


'''
6. Compute the most frequently occuring categorical label for the region
depicted in the satellite images provided (see description in prompt on Canvas).
'''

band_red = [[1, 10, 255],
            [200, 155, 20],
            [30, 20, 10]]
band_nir = [[1, 20, 255],
            [10, 20, 30],
            [200, 155, 20]]

labels = {}
highest = None
count = 0

for i in range(len(band_red)):
    for j in range(len(band_nir)):
        ndvi = band_nir[i][j] - band_red[i][j]/ band_nir[i][j] + band_red[i][j]
        if -0.25 < ndvi <= 0.25:
            label = "barren"
        elif 0.25 < ndvi <= 1.0:
            label = "vegetation-rich"
        elif -1.0 <= ndvi <= -0.25:
            label = "flooded"
        labels[label] = labels.get(label, 0) + 1
        if labels[label] > count:
            highest = label
            count = labels[label]
print(highest)


'''
7. Read in any files named `band_nir.csv` and `band_red.csv` as lists of lists
and print out the highest frequency label for the corresponding region.
'''
import csv
band_red = []
band_nir = []
with open('band_red.csv') as f:
    reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
    for row in reader:
        band_red.append(row)

with open('band_nir.csv') as f:
    reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
    for row in reader:
        band_nir.append(row)

print(band_red)

labels = {}
highest = None
count = 0

for i in range(len(band_red)):
    for j in range(len(band_nir)):
        ndvi = band_nir[i][j] - band_red[i][j]/ band_nir[i][j] + band_red[i][j]
        if -0.25 < ndvi <= 0.25:
            label = "barren"
        elif 0.25 < ndvi <= 1.0:
            label = "vegetation-rich"
        elif -1.0 <= ndvi <= -0.25:
            label = "flooded"
        labels[label] = labels.get(label, 0) + 1
        if labels[label] > count:
            highest = label
            count = labels[label]
print(highest)
