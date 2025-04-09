import tensorflow as tf

print("✅ TensorFlow is installed!")
print("TensorFlow version:", tf.__version__)

gpus = tf.config.list_physical_devices('GPU')
print("Available GPUs:", gpus if gpus else "❌ No GPU detected")