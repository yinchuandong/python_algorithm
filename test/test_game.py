# import gym
# env = gym.make('CartPole-v0')
# env.reset()
# env1 = gym.make('CartPole-v0')
# env1.reset()
# for _ in range(1000):
#     env.render()
#     env.step(env.action_space.sample())  # take a random action
#     env1.render()
#     env1.step(env1.action_space.sample())  # take a random action

# from ple.games.pong import Pong
# from ple import PLE

# game = Pong()
# p = PLE(game, fps=30, display_screen=True, force_fps=False)
# p.init()
# 
from ple.games.flappybird import FlappyBird
from ple import PLE


game = FlappyBird()
p = PLE(game, fps=30, display_screen=True)

p.init()
reward = 0.0

for i in range(nb_frames):
   if p.game_over():
           p.reset_game()

   observation = p.getScreenRGB()
   action = agent.pickAction(reward, observation)
   reward = p.act(action)