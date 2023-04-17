#!/bin/bash

cd $(dirname $0)/../..
pwd

path=mix_mastery_rl/envs/mixing/config/bowl_param.yaml

radius_top=$(yq e '.radius_top' $path)
radius_bottom=$(yq e '.radius_bottom' $path)
height=$(yq e '.height' $path)
num_geom=$(yq e '.num_geom' $path)

python3 bowl_sdf_generator/make_bowl.py --model_name cooking_bowl \
                    --num_division $num_geom \
                    --radius_bottom $radius_bottom \
                    --radius_top $radius_top \
                    --height $height \
                    --thickness 0.006 \
                    --out_mujoco_dir mix_mastery_rl/envs/mixing \
                    --out_gazebo_dir ros/stir_description/models
