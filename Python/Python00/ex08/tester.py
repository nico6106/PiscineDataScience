from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

size = 500
time = 0.005

for elem in ft_tqdm(range(size)):
    sleep(time)
print()

for elem in tqdm(range(size)):
    sleep(time)
print()
