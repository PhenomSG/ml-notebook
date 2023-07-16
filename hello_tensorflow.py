'''import tensorflow as tf
hello = tf.constant('Hello,Tensorflow!')
session = tf.Session()
print(hello)'''

# n TensorFlow 2.x, the usage of tf.Session() has been replaced with eager execution, 
# and we no longer need to explicitly create a session. 

# updated code
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
print(hello)
