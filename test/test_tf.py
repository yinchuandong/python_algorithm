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
    # a = np.zeros_like(Q_table)
    # print np.shape(a)
    # Q_table = np.array(Q_table)
    # Q_a = np.argmax(Q_table, 1)

    # print Q_tabl
    # print Q_a
    # print Q_table[range(3), Q_a]
    return


def test_divide():
    x_data = np.asarray([4.5, 4, 8])

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    state = tf.placeholder(tf.float32, [3])
    div = tf.div(state, 2)

    r = sess.run(div, feed_dict={state: x_data})
    print r
    return


def test_add():
    a = tf.constant([[1], [2], [3]])
    b = tf.constant([[1], [1]])
    c = tf.constant([[1], [2], [3]])

    d = a + c
    # d = tf.concat([a, c], axis=1)

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    # add = d
    add = tf.reduce_sum(d)
    r = sess.run(add)
    print r


def test_multiply():
    pred = tf.constant([[1, 1], [2, 2], [3, 3]])
    label = tf.constant([[0, 0], [1, 1], [0, 0]])

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    multiply = pred * label
    # multiply = tf.multiply(pred, label)
    r = sess.run(multiply)
    print r


def test_entropy():
    pred = tf.constant([[0.8, 0.2], [0.5, 0.5]])
    log_pi = tf.log(tf.clip_by_value(pred, 1e-20, 1.0))
    entropy = -tf.reduce_sum(pred * log_pi, axis=1)
    # entropy = pred * log_pi

    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    r = sess.run(entropy)
    print r

    return


def test_onehot():
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    action = tf.constant([[0, 1], [2, 3]])

    action_onehot = tf.one_hot(action, 4)
    r0, r1 = sess.run([action, action_onehot])
    print np.shape(r0)
    print np.shape(r1)

    # returns = tf.constant([[1, 2], [3, 4]])
    # loss = action * returns
    # print sess.run(loss)

    return


if __name__ == '__main__':
    # test_gradient()
    # test_name_scope()
    # test_shape()
    # test_numpy()
    # test_divide()
    # test_add()
    # test_multiply()
    # test_entropy()
    test_onehot()
