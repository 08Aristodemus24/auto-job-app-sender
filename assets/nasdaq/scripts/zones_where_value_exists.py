nums = [1, 1, 8, 11, -3, 0, 10, 8, 9, 9, 10, 2]

# 8 is found in odd index but also in even index
# 8 is also found in left half but also in right half
val = 1

# if value is found in even index flag zones[0] as 1
# if value is found in odd index flag zones[1] as 1
# if value is found in left half of array flag zones[2] as 1
# if value is found in right half of array flag zones[3] as 1 
zones = [0, 0, 0, 0]
mid = int(len(nums) / 2)
print(mid)

for i, num in enumerate(nums):
    if num == val:
        # if index of value when it matches value
        # is even then this zone is set to 1
        zones[0] = 1 if (i % 2) == 0 or zones[0] == 1 else 0 
        zones[1] = 1 if (i % 2) != 0 or zones[1] == 1 else 0
        zones[2] = 1 if i < mid or zones[2] == 1 else 0
        zones[3] = 1 if i >= mid or zones[3] == 1 else 0

print(zones)
