import tensorflow as tf
import numpy as np


def main():
    x_data = np.asarray([2])
    t_data = np.asarray([3])

    W = tf.constant([3.0])
    y = W * x_data
    z = y * t_data

    # Before starting, initialize the variables.  We will 'run' this first.
    init = tf.initialize_all_variables()

    # Launch the graph.
    sess = tf.Session()
    sess.run(init)

    print sess.run(y)
    print sess.run(z)

    gd1 = tf.gradients(y, W)
    print sess.run(gd1)

    gd2 = tf.gradients(z, y, gd1)
    print sess.run(gd2)

    gd = tf.gradients(z, W)
    print sess.run(gd)

    return


def test_name_scope():
    with tf.name_scope('root') as scope:
        t = tf.constant(3.0, name='t')
        print t.op.name
        t0 = tf.constant(3.0, name='t0')
        print t0.op.name
        with tf.name_scope('sub'):
            t1 = tf.constant(3.0, name='t1')
            print t1.op.name

        with tf.name_scope(scope):
            t1 = tf.constant(3.0, name='t1')
            print t1.op.name
    return


def test_shape():
    t = tf.placeholder('float', [2, 4])
    print t.op.name
    print t.get_shape().as_list()
    return

if __name__ == '__main__':
    main()
    # test_name_scope()
    # test_shape()