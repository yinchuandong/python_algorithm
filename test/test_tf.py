import tensorflow as tf
import numpy as np


def test_gradient():
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


def test_numpy():

    Q_table = [
        [0, 1, 0, 0, 0, 5],
        [1, 1, 3, 1, 1, 1],
        [8, 1, 2, 3, 4, 5],
    ]
    Q_table = np.array(Q_table)
    Q_a = np.argmax(Q_table, 1)

    print Q_table
    print Q_a
    print Q_table[range(3), Q_a]
    return


def test_divide():
    x_data = np.asarray([4.5h, 4, 8])

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    state = tf.placeholder(tf.float32, [3])
    div = tf.div(state, 2)

    r = sess.run(div, feed_dict={state: x_data})
    print r


    return




if __name__ == '__main__':
    # test_gradient()
    # test_name_scope()
    # test_shape()
    # test_numpy()
    test_divide()
