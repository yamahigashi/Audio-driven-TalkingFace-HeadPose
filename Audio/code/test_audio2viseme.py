# encoding:utf-8
# test different audio
import os
import argparse

import glob
# import pdb
# from PIL import Image
# import numpy as np
import sys


def getsingle(srcdir, name, varybg=0, multi=0):
    srcroot = os.getcwd()
    if not varybg:
        imgs = glob.glob(os.path.join(srcroot, srcdir, "*_blend.png"))
        print("srcdir", os.path.join(srcroot, srcdir, "*_blend.png"))
    else:
        imgs = glob.glob(os.path.join(srcroot, srcdir, "*_blend2.png"))
        print("srcdir", os.path.join(srcroot, srcdir, "*_blend2.png"))
    if not os.path.exists("../../render-to-video/datasets/list/testSingle"):
        os.makedirs("../../render-to-video/datasets/list/testSingle")
    f1 = open("../../render-to-video/datasets/list/testSingle/%s.txt" % name, "w")
    imgs = sorted(imgs)
    if multi:
        imgs = imgs[2:]
    for im in imgs:
        print(im, file=f1)
    f1.close()


def parse_arg():
    parser = argparse.ArgumentParser(description='Voice operated character animation')

    parser.add_argument('--device_ids', type=int, default=0, help='gpu id')
    parser.add_argument('--audio_epoch', type=int, default=99, help='audio epoch')
    parser.add_argument('--audio_file', type=str, default="", help='Path to audio file')
    parser.add_argument('--model_file', type=str, default="../audio/model/atcnet_lstm_general.pth", help='Path to audio model')
    parser.add_argument('--person_id', type=str, default="0", help='Person id')

    args = parser.parse_args()

    return args


def main():
    args = parse_arg()
    sample_dir = f"../results/{args.person_id}_{args.audio_epoch}"

    # 1.audio to 3dmm
    add = f"--model_name {args.model_file} --pose 1 --relativeframe 0"
    cmd = f"python atcnet_test1.py --device_ids {args.device_ids} {add} --sample_dir {sample_dir} --in_file {args.audio_file}"
    print(cmd)
    os.system(cmd)  # nosec


if __name__ == "__main__":
    main()
