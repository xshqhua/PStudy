import tensorflow as tf
with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    print(sess.list_devices())