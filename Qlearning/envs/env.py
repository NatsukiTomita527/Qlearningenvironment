import gym
from gym import error, spaces, utils
from gym.utils import seeding

class FooEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self, env):
        self.env = env

        self.action_space = self.env.action_space

        self.observation_space = self.env.observation_space

        self.reward_range = self.env.reward_range

        self.metadata = self.env.metadata

  def step(self, action):           # actionを実行し、結果を返す
      return self.env.step(action)

  def reset(self):                  # 状態を初期化し、初期の観測値を返す
      return self.env.reset

  def render(self, close=False): # 環境を可視化する
      return self.env.render

  def close(self): # 環境を閉じて後処理をする
      return self.env.close()

  def seed(self, seed=None): # ランダムシードを固定する
      return self.env.seed(seed)

