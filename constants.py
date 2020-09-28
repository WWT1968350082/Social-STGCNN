import numpy as np
import torch
OBS_LEN = 8
PRED_LEN = 12
NUM_WORKERS = 0

MLP_DIM = 64
H_DIM = 64
EMBEDDING_DIM = 16
BOTTLENECK_DIM = 32
NOISE_DIM = 8

DATASET_NAME = 'eth'
NUM_ITERATIONS = 20000
NUM_EPOCHS = 500
G_LR = 1e-3
D_LR = 1e-3
G_STEPS = 1
D_STEPS = 2

MAX_PEDS = 64
BEST_K = 20
PRINT_EVERY = 250
NUM_SAMPLES = 20
NUM_SAMPLES_CHECK = 5000


ATTN_L = 196
ATTN_D = 512
ATTN_D_DOWN = 16


g_l2_losses_abs, g_l2_losses_rel = ([],) * 2
print(g_l2_losses_abs)
print(g_l2_losses_rel)
