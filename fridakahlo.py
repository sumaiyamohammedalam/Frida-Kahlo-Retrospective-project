# 1. Create a list of paintings
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

# 2. Create a list of dates
dates = [1939, 1933, 1946, 1940]

# 3. Zip paintings with dates and convert to a list
paintings = list(zip(paintings, dates))
print("Paintings with dates:", paintings)

# 4. Append additional paintings with their dates
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print("Updated paintings list:", paintings)

# 5. Find the total number of paintings
num_paintings = len(paintings)
print("Total number of paintings:", num_paintings)

# 6. Generate a list of audio tour numbers
audio_tour_number = list(range(1, num_paintings + 1))
print("Audio tour numbers:", audio_tour_number)

# 7. Create the master list by zipping audio tour numbers with paintings
master_list = list(zip(audio_tour_number, paintings))

# 8. Print the master list
print("Master list for the audio tour:", master_list)
