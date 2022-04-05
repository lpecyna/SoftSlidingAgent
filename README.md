# Agent for SoftSlidingGym
This repository contains modified benchmarked reinforcement learning algorithms for deformable linear object (DLO) following environment from [SoftSlidingGym](https://github.com/lpecyna/SoftSlidingGym) ([paper](https://arxiv.org/abs/2204.00117)). They were adapted for this specific task based on the algorithms in [SoftAgent](https://github.com/Xingyu-Lin/softagent) repository.

The benchmarked algorithms currently include only Soft Actor-Critic algorithm:
* CURL/SAC [[source](./curl)] [[paper](https://proceedings.icml.cc/static/paper_files/icml/2020/5951-Paper.pdf)] 
    * This is based on the [original implementation](https://github.com/MishaLaskin/curl)

## Installation 

1. Install "SoftSlidingGym" by following the instructions in [SoftSlidingGym](https://github.com/lpecyna/SoftSlidingGym) repository. Then, copy the "SoftSlidingGym" code to softgym folder in the SoftSlidingAgent root directory so we have the following file structure:
    ```
    SoftSlidingAgent
    ├── curl
    ├── ...
    ├── softgym
        ├── PyFlex
        ├── ...
        ├── softgym
    ```
2. Update conda env with additional packages required by SoftAgent: `conda env update  --file environment.yml  --prune`
3. Activate the conda environment by running `. ./prepare_1.0.sh`.

## Running benchmarked experiments

1. Running CURL/SAC experiments: `python experiments/run_curl.py`. Refer to `run_curl.py` for different arguments.

**Note**: Default number of environment variations are set to 1000. Set them to a different number (e.g. 1) if you just want to test the algorithm.

## Main changes

Main changes to the algorithm (compared to the scripts in [SoftAgent](https://github.com/Xingyu-Lin/softagent)) were made to allow it to operate with the episodes of various length. They appear mainly in [train.py](./curl/train.py) file. There were some variations of SAC algorithm investigated ([curl_sac.py](./curl/curl_sac.py)) but the included file should be fairly the same as the original one in [SoftAgent](https://github.com/Xingyu-Lin/softagent). Some parameters in [default_config.py](./curl/default_config.py) have been adapted.

## The task

The agent behaviour is determined by the reward function and defined more in the environment repository: [SoftSlidingGym](https://github.com/lpecyna/SoftSlidingGym).

Generally, the agent is supposed to slide along the rope - using an appropriate grasping force - to its tail end. The beginning of the rope is firmly attached to a point in space in the simulator.

| Image                                    | Name                                                                                               | Description                             |
|------------------------------------------|:---------------------------------------------------------------------------------------------------|:----------------------------------------|
| ![Gif](./examples/Reach_end_hold.gif) | [Rope following](https://github.com/lpecyna/SoftSlidingGym/blob/master/softgym/envs/rope_follow.py) | Correctly perfromed rope following task |


## References
- CURL implementation is from the official release: https://github.com/MishaLaskin/curl
- SoftAgent repository: https://github.com/Xingyu-Lin/softagent
- SoftGym repository: https://github.com/Xingyu-Lin/softgym
- SoftSlidingGym - environment for soft object following: https://github.com/lpecyna/SoftSlidingGym
