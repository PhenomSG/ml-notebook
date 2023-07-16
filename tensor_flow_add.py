import tensorflow as tf

# Create a TensorFlow constant
a = tf.constant(2)
b = tf.constant(3)

# Perform addition operation
result = tf.add(a, b)

# Print the result
print("The sum is:", result.numpy())
