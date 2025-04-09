import tensorflow as tf
import numpy as np

def create_and_compile_model():
    # Define the model
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(1,)),
        tf.keras.layers.Dense(units=1)
    ])
    # Compile the model
    model.compile(optimizer='sgd', loss='mean_squared_error')
    return model

def define_data_two_times_x():
    # Define the data
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    y = np.array([2, 4, 6, 8, 10], dtype=float)

    return x, y

def define_data_x_plus_10():
    # Define the data
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    y = np.array([11, 12, 13, 14, 15], dtype=float)

    return x, y

def main():
    # Create and compile the model
    model1 = create_and_compile_model()

    # Define the data
    x1, y1 = define_data_two_times_x()

    # Train the model
    model1.fit(x1, y1, epochs=500, verbose=0)

    # Make a prediction
    result1 = []
    for i in range(6, 11):
        result1.append(model1.predict(np.array([i])))
    print(result1)  # Expected output: [12.0, 14.0, 16.0, 18.0, 20.0]

    # Create and compile the model
    model2 = create_and_compile_model()

    # Define the data
    x2, y2 = define_data_x_plus_10()

    # Train the model
    model2.fit(x2, y2, epochs=500, verbose=0)

    # Make a prediction
    result2 = []
    for i in range(6, 11):
        result2.append(model2.predict(np.array([i])))
    print(result2)  # Expected output: [16.0, 17.0, 18.0, 19.0, 20.0]

if __name__ == "__main__":
    main()