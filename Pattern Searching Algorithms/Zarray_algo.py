#Python program to understand Z- pattern searching algorithm
def compute_z_array(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0  

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z

def z_search(text, pattern):
    concat_str = pattern + "$" + text
    z_array = compute_z_array(concat_str)

    pattern_length = len(pattern)
    results = []

    for i in range(len(z_array)):
        if z_array[i] == pattern_length:
            results.append(i - pattern_length - 1)

    return results


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = z_search(text, pattern)

if matches:
    print(f"Pattern found at indices: {matches}")
else:
    print("Pattern not found.")
