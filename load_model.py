import tensorflow as tf

def load_trained_model(model_path):
    # Load the model without optimizer configuration
    model = tf.keras.models.load_model(model_path, compile=False)

    # Re-compile with a new optimizer if needed
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model
