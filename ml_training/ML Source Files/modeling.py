from __future__ import annotations

import tensorflow as tf


def build_binary_classifier(config: dict, input_dim: int) -> tf.keras.Model:
    hidden_units = list(config["model"]["hidden_units"])
    dropout = float(config["model"]["dropout"])

    inputs = tf.keras.Input(shape=(input_dim,), name="normalized_features")
    x = inputs

    for units in hidden_units:
        x = tf.keras.layers.Dense(units, activation="relu")(x)
        x = tf.keras.layers.Dropout(dropout)(x)

    outputs = tf.keras.layers.Dense(1, activation="sigmoid", name="leak_probability")(x)
    return tf.keras.Model(inputs=inputs, outputs=outputs, name="binary_leak_classifier")


def compile_binary_classifier(model: tf.keras.Model, config: dict) -> None:
    learning_rate = float(config["training"]["learning_rate"])
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss="binary_crossentropy",
        metrics=[
            tf.keras.metrics.BinaryAccuracy(name="accuracy"),
            tf.keras.metrics.Precision(name="precision"),
            tf.keras.metrics.Recall(name="recall"),
            tf.keras.metrics.AUC(name="auc"),
        ],
    )
