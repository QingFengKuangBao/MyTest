import os

import numpy as np
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 基本的例子
# def test01():
#     # create data
#     x_data = np.random.rand(100).astype(np.float32)
#     y_data = x_data*0.1 + 0.3

#     # 创建结构
#     Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
#     biases=tf.Variable(tf.zeros([1]))


#     y=Weights*x_data+biases
#     loss = tf.reduce_mean(tf.square(y-y_data))

#     optimizer = tf.train.GradientDescentOptimizer(0.5)
#     train = optimizer.minimize(loss)
#     init = tf.global_variables_initializer() 


#     sess = tf.Session()
#     sess.run(init)          # Very important
#     print(x_data)
#     for step in range(301):
#         sess.run(train)
#         if step % 20 == 0:
#             print(y)
#             print(step, sess.run(Weights), sess.run(biases))
#     sess.close()


# 会话控制
# def test02():
    # matrix1 = tf.constant([[3,3]])
    # matrix2 = tf.constant([[2],
    #                    [2]])
    # product = tf.matmul(matrix1,matrix2) #矩阵相乘 np.dot(n1,m2)

    
    # #开启会话
    # sess=tf.Session()
    # #运行
    # result=sess.run(product)
    # print(result)
    # sess.close()

    # with tf.Session() as sess:
    #     result2=sess.run(product)
    #     print(result2)


# 变量
# def test03():
#     #定义变量
#     state=tf.Variable(initial_value=1,name="counter")
#     # print(state.name)

#     #定义常量
#     one=tf.constant(1)

#     new_value=tf.add(state,one)

#     update=tf.assign(state,new_value)
    
#     init=tf.global_variables_initializer()#初始化全局变量

#     with tf.Session() as sess:
#         sess.run(init)
#         for i  in range(3):
#             # print(sess.run(update))
#             # sess.run(new_value)
#             sess.run(update)
#             print(sess.run(state))
            

# placeholder  传入值
def test04():
    input1=tf.placeholder(tf.float32)
    input2=tf.placeholder(tf.float32)
    output=tf.multiply(input1,input2)

    with tf.Session() as sess:
        print(sess.run(output,feed_dict={input1:[7.1], input2:[2.]}))
    pass


if __name__ == '__main__':
    # 会话
    # test02()
    # 变量
    # test03()

    test04()

    pass
