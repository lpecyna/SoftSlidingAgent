# SoftAgent for DLO following
This repository contains modification for the benchmarked algorithms for difformable linear object (DLO) following environment from [SoftGym DLO following](https://github.com/lpecyna/Softgym_rope_following) ([paper - TBD]()). They were adapted for this specific task based on the algorithms in [SoftAgent](https://github.com/Xingyu-Lin/softagent) repository.

The benchmarked algorithms currently include only Soft Actor-Critic algorithm:
* CURL/SAC [[source](./curl)] [[paper](https://proceedings.icml.cc/static/paper_files/icml/2020/5951-Paper.pdf)] 
    * This is based on the [original implementation](https://github.com/MishaLaskin/curl)

## Installation 

1. Install "SoftGym DLO following" by following the instructions in [SoftGym DLO following](https://github.com/lpecyna/Softgym_rope_following) repository. Then, copy the "SoftGym DLO following" code to softgym folder in the SoftAgent root directory so we have the following file structure:
    ```
    Softagent_rope_followig
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

**Note**: Default number of environment variations are set to 1000. Set them to a different number (e.g. 1) if you want to just test the algorithm.

## Main changes

Main changes to the algorithm were made to allow it to operate with the episodes of not constant length. They appear mainly in [train.py](./curl/train.py) file. There were some variations of SAC algorithm investigated [curl_sac.py](./curl/curl_sac.py) but the included file should be fairly the same as the orighinal one in SoftAgent. Some parameters in [default_config.py](./curl/default_config.py) have been adapted.

## The task

The task is determined by the reward function and defined more in the environment repository: [SoftGym DLO following](https://github.com/lpecyna/Softgym_rope_following).

Generally, the agent is supposed to slide along the rope - using an appropriate grasping force - to its tail end. The beginning of the rope is firmly attached to a point in space in the simulator.

| Image                                    | Name                                                                                               | Description                             |
|------------------------------------------|:---------------------------------------------------------------------------------------------------|:----------------------------------------|
| ![Gif](./examples/Reach_end_hold.gif) | [Rope following](https://github.com/lpecyna/Softgym_rope_following/softgym/envs/rope_following.py) | Correctly perfromed rope following task |

## Cite
If you find this codebase useful in your research, please consider citing:
```
TBD
```

## References
- CURL implementation is from the official release: https://github.com/MishaLaskin/curl
- SoftAgent repository: https://github.com/Xingyu-Lin/softagent
- SoftGym repository: https://github.com/Xingyu-Lin/softgym
- SoftGym DLO following repository: https://github.com/lpecyna/Softgym_rope_following
