# Task 3 - Tuples for Fixed Data

# Part A - Unpacking Fixed Data
image_size = (224, 224)
model_result = ("baseline_cnn", 0.91)

width, height = image_size
model_name, accuracy = model_result

print(f"Image size: {width} x {height}")
print(f"Model: {model_name} | Accuracy: {accuracy}")

# Part B - Returning a Tuple
def summarize_scores(scores):
    if len(scores) == 0:
        return None
    return min(scores), max(scores), sum(scores) / len(scores)

result = summarize_scores([72, 88, 91, 67])
if result is not None:
    minimum, maximum, average = result
    print(f"Minimum: {minimum} | Maximum: {maximum} | Average: {average}")

empty_result = summarize_scores([])
print(f"Empty: {empty_result}")

# Part C - Tuples as Dictionary Keys
input_models = {
    (224, 224): "resnet50",
    (299, 299): "inception_v3",
    (384, 384): "vit_base"
}

print(f"Model for 299x299: {input_models[(299, 299)]}")

try:
    invalid = {[224, 224]: "resnet50"}
except TypeError as e:
    print(f"TypeError: {e}")