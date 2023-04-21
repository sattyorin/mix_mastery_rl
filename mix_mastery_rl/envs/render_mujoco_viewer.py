import argparse
import os
import time

import mujoco
import mujoco_viewer

parser = argparse.ArgumentParser()
parser.add_argument(
    "--xml",
    type=str,
    default="samples/xmls/humanoid.xml",
)
parser.add_argument(
    "--meshdir",
    type=str,
    default="mixing/meshes",
)
args = parser.parse_args()

# load mesh
if os.path.exists(args.meshdir):
    mesh_files = os.listdir(args.meshdir)
    assets = dict()
    for file in mesh_files:
        with open(os.path.join(args.meshdir, file), "rb") as f:
            assets[file] = f.read()

    model = mujoco.MjModel.from_xml_path(args.xml, assets)

else:
    model = mujoco.MjModel.from_xml_path(args.xml)


data = mujoco.MjData(model)

# create the viewer object
viewer = mujoco_viewer.MujocoViewer(model, data)

# simulate and render
ctrl_t = time.time()
step_t = time.time()
for _ in range(10000000000):
    if time.time() - ctrl_t > 0.05:
        if data.ctrl.size > 2:
            data.ctrl[0] = 0.04
            data.ctrl[1] = 0.04
            data.ctrl[2] = 0.04
        # print(data.qpos)
        viewer.render()
        ctrl_t = time.time()
    if viewer.is_alive:
        if time.time() - step_t > 0.0025:
            mujoco.mj_step(model, data)
            # viewer.render()
            step_t = time.time()
    else:
        print("break")
        break

viewer.close()
