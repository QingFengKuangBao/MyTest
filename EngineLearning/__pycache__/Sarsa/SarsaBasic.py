import pandas as pd
import numpy as np
import time

np.random.seed(200)  # 随机数的seed值
N_STATES = 10   # 1维世界的宽度
ACTIONS = ['left', 'right']     # 探索者的可用动作
EPSILON = 1   # 贪婪度 greedy
ALPHA = 0.1     # 学习率
GAMMA = 0.9    # 奖励递减值
MAX_EPISODES = 20   # 最大回合数
FRESH_TIME = 0.1    # 移动间隔时间

from numpy import dtype

def build_q_table(n_states,actions):
    # 初始化
    table = pd.DataFrame(np.zeros(
        shape=(n_states, len(actions))),  # 数组的结构
        columns=ACTIONS , # 列的索引名称
        dtype=np.float16
        )
    # print(table)
    return table


def choose_action(state, q_table):
    # 如何选择 action
    state_actions = q_table.iloc[state, :]  # 选出这个 state 的所有 action 值
    if(np.random.uniform() > EPSILON or state_actions.all() == 0):  # 非贪婪 or 或者这个 state 还没有探索过
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.idxmax()  # 贪婪模式
    return action_name

# 获取环境反馈
def get_env_feedback(S, A):
    if A == 'right':#向右走
        if S == N_STATES - 2:   # terminate
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else: #向左走
        R=0
        if S==0:
            S_=S
        else:
            S_=S-1
    return S_,R #S_:移动后的状态   R行为所反馈的奖惩值

def update_env(S, episode, step_counter):
    # This is how environment be updated  环境是如何更新的
    env_list = ['-']*(N_STATES-1) + ['T']   # '---------T' our environment  初始化的环境
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


def rl():
    q_table = build_q_table(N_STATES, ACTIONS)  # 初始 q table
    for episode in range(MAX_EPISODES):     # 回合
        step_counter = 0
        S = 0   # 回合初始位置
        A = choose_action(S, q_table)   # 选行为
        is_terminated = False   # 是否回合结束
        update_env(S, episode, step_counter)    # 环境更新
        while not is_terminated:
            S_, R = get_env_feedback(S, A)  # 实施行为并得到环境的反馈
            q_predict = q_table.loc[S, A]    # 估算的(状态-行为)值
            if S_ != 'terminal':
                A_=choose_action(S_, q_table) 
                q_target = R + GAMMA * q_table.loc[S_,A_] #  
            else:
                q_target = R     #  实际的(状态-行为)值 (回合结束)
                is_terminated = True    # terminate this episode

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  #  q_table 更新   Qlearing的核心算法
            S = S_  # 探索者移动到下一个 state
            A=A_
            update_env(S, episode, step_counter+1)  # 环境更新

            step_counter += 1
    return q_table


if __name__ == "__main__":
    
    q_table = rl()
    print('\r\nQ-table:\n')
    
    print(q_table)
    # q_table.to_json('e://桌面/1.json')
    # print(pd.read_json("e://桌面/1.json",typ='frame').dtypes)
    pass
