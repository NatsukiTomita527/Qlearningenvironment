from gym.envs.registration import register

register(
  id='foo-v0',
  entry_point='Qlearning.envs.Env'
)