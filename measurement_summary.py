measurements = [18, 21, 24, 19]
review_threshold_text = "20"

# Replace this scaffold output with your calculation, loop, decision, and summary.
# print("TODO: complete the measurement summary")
review_threshold = int(review_threshold_text)
total = 0
review_count = 0
for measurement in measurements:
    print("Measurement:", measurement, end="")
    total = total + measurement
    if measurement > review_threshold:
        print(" review")
        review_count += 1
    else:
        print(" within range")
print("Count:", len(measurements))
print("Total:", total)
print("Mean:", sum(measurements)/len(measurements))
print("Review count:", review_count)
