import numpy as np
from smac.env import StarCraft2Env

class StarCraft2FullActionSpaceEnv(StarCraft2Env):
    def __init__(
        self,
        map_name="8m",
        step_mul=8,
        move_amount=2,
        difficulty="7",
        game_version=None,
        seed=None,
        continuing_episode=False,
        obs_all_health=True,
        obs_own_health=True,
        obs_last_action=False,
        obs_pathing_grid=False,
        obs_terrain_height=False,
        obs_instead_of_state=False,
        obs_timestep_number=False,
        state_last_action=True,
        state_timestep_number=False,
        reward_sparse=False,
        reward_only_positive=True,
        reward_death_value=10,
        reward_win=200,
        reward_defeat=0,
        reward_negative_scale=0.5,
        reward_scale=True,
        reward_scale_rate=20,
        replay_dir="",
        replay_prefix="",
        window_size_x=1920,
        window_size_y=1200,
        heuristic_ai=False,
        heuristic_rest=False,
        debug=False,
    ):
        super(StarCraft2FullActionSpaceEnv, self).__init__(map_name, step_mul, move_amount, difficulty, game_version, seed,
        continuing_episode, obs_all_health, obs_own_health, obs_last_action, obs_pathing_grid, 
        obs_terrain_height, obs_instead_of_state, obs_timestep_number, state_last_action, state_timestep_number, 
        reward_sparse, reward_only_positive, reward_death_value, reward_win,reward_defeat, reward_negative_scale, reward_scale, reward_scale_rate, replay_dir, replay_prefix, window_size_x,window_size_y,heuristic_ai,heuristic_rest,debug)

    def get_avail_agent_actions(self, agent_id):
        avail_actions = super.get_avail_agent_actions(agent_id)
        
        unit = self.get_unit_by_id(agent_id)
        if unit.health > 0:
            return np.ones_like(avail_actions)
        else:
            return [1] + [0] * (self.n_actions - 1)

    def get_agent_action(self, a_id, action):
        avail_actions = super.get_avail_agent_actions(a_id)

        if avail_actions[action] != 1:
            return None

        return super().get_agent_action(a_id, action)
