# rendering results of RGB-Scenes dataset
Dataset Scenes:
- RGB
    - Building
    - DailyStuff
    - Dimsum
    - Ebike
    - IronIngot
    - LandScape
    - Parterre
    - RoadBlock
    - RotaryKiln
    - Truck
- Thermal
    - Building
    - DailyStuff
    - Dimsum
    - Ebike
    - IronIngot
    - LandScape
    - Parterre
    - RoadBlock
    - RotaryKiln
    - Truck


## RGB
### rgb execution
GPU: one NVIDIA A100

time usage: 123.92 min

### rendering results
copy rendering results:
```bash
cd $(git rev-parse --show-toplevel)
python tools/copy_videos_RGB_Scenes.py --image_type rgb
```
### Scenes Visualization
#### Building

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.93 GB** | **199.51 s** | 516,512 | 19.24 | 0.739 | 0.332 |
| **30k** | 1.34 GB | 715.12 s | **884,545** | **20.45** | **0.783** | **0.253** |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/rgb/Building/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/rgb/Building/traj_29999.mp4)

#### DailyStuff

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.82 GB** | **159.26 s** | 519,511 | **21.10** | **0.794** | **0.223** |
| **30k** | 1.02 GB | 714.00 s | **664,040** | 20.27 | 0.745 | 0.250 |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/rgb/DailyStuff/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/rgb/DailyStuff/traj_29999.mp4)

#### Dimsum

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.88 GB** | **160.28 s** | 537,091 | **24.21** | **0.856** | 0.172 |
| **30k** | 1.09 GB | 715.19 s | **716,547** | 23.49 | 0.840 | **0.152** |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/rgb/Dimsum/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/rgb/Dimsum/traj_29999.mp4)

#### Ebike

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.50 GB** | **151.76 s** | 292,940 | **27.42** | **0.919** | **0.121** |
| **30k** | 0.51 GB | 652.19 s | **319,048** | 27.10 | 0.905 | 0.131 |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/rgb/Ebike/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/rgb/Ebike/traj_29999.mp4)

#### IronIngot

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **1.23 GB** | **170.26 s** | 749,340 | **24.11** | **0.877** | **0.165** |
| **30k** | 1.47 GB | 773.39 s | **983,211** | 24.10 | 0.860 | 0.167 |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/rgb/IronIngot/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/rgb/IronIngot/traj_29999.mp4)

#### LandScape

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **1.12 GB** | **166.69 s** | 681,860 | **20.61** | **0.710** | **0.231** |
| **30k** | 1.48 GB | 751.91 s | **985,861** | 20.25 | 0.684 | 0.237 |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/rgb/Landscape/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/rgb/Landscape/traj_29999.mp4)

#### Parterre

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.63 GB** | **152.35 s** | 380,637 | 23.74 | **0.847** | 0.166 |
| **30k** | 0.68 GB | 656.90 s | **436,007** | **23.97** | 0.841 | **0.148** |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/rgb/Parterre/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/rgb/Parterre/traj_29999.mp4)

#### RoadBlock

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.35 GB** | **144.94 s** | 197,474 | **27.59** | **0.914** | 0.194 |
| **30k** | 0.36 GB | 616.23 s | **220,088** | 26.89 | 0.904 | **0.187** |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/rgb/RoadBlock/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/rgb/RoadBlock/traj_29999.mp4)

#### RotaryKiln

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **1.21 GB** | **160.99 s** | 732,846 | **21.49** | **0.801** | **0.163** |
| **30k** | 1.77 GB | 721.50 s | **1,185,367** | 21.21 | 0.767 | 0.197 |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/rgb/RotaryKiln/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/rgb/RotaryKiln/traj_29999.mp4)

#### Truck

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.66 GB** | **148.61 s** | 383,837 | 22.24 | **0.816** | 0.212 |
| **30k** | 0.77 GB | 646.20 s | **497,067** | 22.24 | 0.802 | 0.212 |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/rgb/Truck/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/rgb/Truck/traj_29999.mp4)

## Thermal

### thermal execution
GPU: one NVIDIA A100

time usage: 106.64 min

### rendering results
copy rendering results:
```bash
cd $(git rev-parse --show-toplevel)
python tools/copy_videos_RGB_Scenes.py --image_type thermal
```
### Scenes Visualization
#### Building

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.53 GB** | **131.54 s** | 322,841 | 24.37 | 0.867 | 0.169 |
| **30k** | 0.81 GB | 572.21 s | **519,569** | **25.37** | **0.872** | **0.146** |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/thermal/Building/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/thermal/Building/traj_29999.mp4)

#### DailyStuff

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.22 GB** | **127.05 s** | 129,738 | **20.24** | **0.829** | **0.162** |
| **30k** | 0.34 GB | 549.03 s | **209,350** | 19.07 | 0.795 | 0.203 |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/thermal/DailyStuff/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/thermal/DailyStuff/traj_29999.mp4)

#### Dimsum

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.26 GB** | **129.20 s** | 149,638 | 25.70 | 0.888 | 0.098 |
| **30k** | 0.31 GB | 557.82 s | **186,421** | **26.27** | **0.890** | **0.089** |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/thermal/Dimsum/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/thermal/Dimsum/traj_29999.mp4)

#### Ebike

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.45 GB** | **130.31 s** | 282,278 | **22.42** | **0.852** | **0.158** |
| **30k** | 0.83 GB | 578.34 s | **541,974** | 21.26 | 0.813 | 0.209 |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/thermal/Ebike/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/thermal/Ebike/traj_29999.mp4)

#### IronIngot

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.44 GB** | **135.27 s** | 256,275 | **29.80** | **0.908** | **0.054** |
| **30k** | 0.51 GB | 591.17 s | **318,863** | 29.73 | 0.897 | 0.058 |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/thermal/IronIngot/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/thermal/IronIngot/traj_29999.mp4)

#### LandScape

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.38 GB** | **184.72 s** | 236,726 | **19.94** | **0.807** | **0.285** |
| **30k** | 1.05 GB | 928.04 s | **695,418** | 19.47 | 0.773 | 0.322 |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/thermal/Landscape/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/thermal/Landscape/traj_29999.mp4)

#### Parterre

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.26 GB** | **130.03 s** | 147,046 | **22.50** | **0.862** | **0.146** |
| **30k** | 0.34 GB | 562.54 s | **208,891** | 22.08 | 0.835 | 0.173 |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/thermal/Parterre/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/thermal/Parterre/traj_29999.mp4)

#### RoadBlock

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.20 GB** | **126.11 s** | 106,391 | 26.28 | **0.918** | 0.109 |
| **30k** | 0.23 GB | 536.06 s | **133,826** | **26.37** | 0.905 | **0.101** |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/thermal/RoadBlock/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/thermal/RoadBlock/traj_29999.mp4)

#### RotaryKiln

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.26 GB** | **125.56 s** | 151,457 | 26.42 | **0.926** | 0.083 |
| **30k** | 0.32 GB | 537.36 s | **193,783** | **26.78** | 0.925 | **0.076** |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/thermal/RotaryKiln/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/thermal/RotaryKiln/traj_29999.mp4)

#### Truck

| Iteration | Memory Usage | Elapsed Time | Num. Gaussians | PSNR (↑) | SSIM (↑) | LPIPS (↓) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **7k** | **0.31 GB** | **128.40 s** | 173,696 | 23.96 | 0.844 | 0.117 |
| **30k** | 0.41 GB | 551.12 s | **251,255** | **24.86** | **0.855** | **0.114** |

- [rendering at Step 6999](../../render_result/RGBT-Scenes/thermal/Truck/traj_6999.mp4)
- [rendering at Step 29999](../../render_result/RGBT-Scenes/thermal/Truck/traj_29999.mp4)

