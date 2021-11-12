import tensorflow as tf

#  Brain initializes a random fully connected neural net and offer a method to run forward propagation through it


class Brain (tf.keras.Model):
    def __init__(self,
                 sizes,
                 activation='tanh',
                 output_activation=None):
        super().__init__()

        self._geometry = sizes

        self.denses = [tf.keras.layers.Dense(
            size, activation=activation) for size in sizes[:-1]]
        self.out = tf.keras.layers.Dense(
            sizes[-1], activation=output_activation)

    @tf.function
    def call(self, x):
        for dense in self.denses:
            x = dense(x)

        return self.out(x)
