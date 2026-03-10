<font color="red">thermal</font> results from **ThermalGaussian** vs results from **gsplat**

## comparison
first 6 lines: results from ThermalGaussian paper

last line: results from gsplat package benchmark experiment


### RGB Results

| Metric | Method | Dimsum | Daily Stuff | Ebike | Road Block | Truck | Rotary Kiln | Building | Iron Ingot | Parterre | Land Scape | Avg. |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PSNR ↑** | 3DGS | 23.91 | 20.43 | 26.77 | 27.80 | 22.30 | 20.79 | 20.95 | 23.96 | 24.91 | 20.20 | 23.20 |
| | ThermoNeRF | 19.74 | 16.79 | 17.75 | 18.32 | 18.77 | 18.89 | 17.12 | 15.07 | 23.13 | 19.13 | 18.46 |
| | Ours<sub>MSMG</sub> | **24.42** | 21.71 | **27.34** | **28.22** | 23.57 | 22.23 | 23.08 | **25.69** | **25.57** | 20.91 | 24.27 |
| | Ours<sub>OMMG</sub> | 24.38 | **21.76** | 26.85 | 28.12 | **24.17** | **23.14** | **24.19** | 24.55 | 25.48 | **21.71** | **24.34** |
| | <font color="blue">gsplat</font> | <font color="blue">23.49</font> | <font color="blue">20.27</font> | <font color="blue">27.10</font> | <font color="blue">26.89</font> | <font color="blue">22.24</font> | <font color="blue">21.21</font> | <font color="blue">20.45</font> | <font color="blue">24.10</font> | <font color="blue">23.97</font> | <font color="blue">20.25</font> | <font color="blue">22.99</font> |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **SSIM ↑** | 3DGS | 0.847 | 0.748 | 0.901 | 0.910 | 0.807 | 0.772 | 0.791 | 0.872 | 0.859 | 0.696 | 0.820 |
| | ThermoNeRF | 0.688 | 0.639 | 0.540 | 0.619 | 0.688 | 0.600 | 0.460 | 0.293 | 0.756 | 0.583 | 0.586 |
| | Ours<sub>MSMG</sub> | **0.858** | 0.793 | **0.917** | 0.916 | 0.833 | 0.811 | 0.844 | **0.891** | **0.874** | 0.715 | 0.845 |
| | Ours<sub>OMMG</sub> | **0.858** | **0.797** | 0.905 | **0.920** | **0.840** | **0.822** | **0.849** | 0.884 | 0.855 | **0.739** | **0.847** |
| | <font color="blue">gsplat</font> | <font color="blue">0.840</font> | <font color="blue">0.745</font> | <font color="blue">0.905</font> | <font color="blue">0.904</font> | <font color="blue">0.802</font> | <font color="blue">0.767</font> | <font color="blue">0.783</font> | <font color="blue">0.860</font> | <font color="blue">0.841</font> | <font color="blue">0.684</font> | <font color="blue">0.813</font> |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **LPIPS ↓** | 3DGS | **0.194** | 0.299 | 0.171 | 0.201 | 0.232 | 0.217 | 0.228 | 0.188 | 0.183 | 0.280 | 0.219 |
| | ThermoNeRF | 0.228 | 0.465 | 0.244 | 0.548 | 0.311 | 0.207 | 0.291 | 0.301 | **0.167** | 0.275 | 0.303 |
| | Ours<sub>MSMG</sub> | **0.194** | 0.262 | **0.156** | 0.221 | 0.217 | 0.190 | **0.168** | **0.172** | 0.184 | 0.275 | 0.204 |
| | Ours<sub>OMMG</sub> | **0.194** | **0.253** | 0.169 | **0.199** | **0.211** | **0.184** | 0.170 | 0.186 | 0.195 | **0.268** | **0.203** |
| | <font color="blue">gsplat</font> | <font color="blue">**0.152**</font> | <font color="blue">**0.250**</font> | <font color="blue">**0.131**</font> | <font color="blue">**0.187**</font> | <font color="blue">0.212</font> | <font color="blue">**0.197**</font> | <font color="blue">0.253</font> | <font color="blue">**0.167**</font> | <font color="blue">**0.148**</font> | <font color="blue">**0.237**</font> | <font color="blue">**0.193**</font> |


conclusion: 

The results are generally worse than SOTA results from ThermalGaussian paper. However, for LPIPS metric, the gsplat package achieves superior results across multiple scenes.

### Thermal Results

| Metric | Method | Dimsum | Daily Stuff | Ebike | Road Block | Truck | Rotary Kiln | Building | Iron Ingot | Parterre | Land Scape | Avg. |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PSNR ↑** | 3DGS | 25.38 | × | × | × | 20.97 | 23.79 | 23.75 | × | × | × | × |
| | ThermoNeRF | 24.27 | 17.34 | 19.70 | 17.17 | 23.53 | 26.40 | 23.31 | 22.97 | 17.88 | 18.79 | 21.13 |
| | 3DGS+MI | 26.35 | 18.77 | 20.89 | 26.75 | 26.17 | 26.59 | 25.76 | 29.57 | 22.09 | 20.17 | 24.31 |
| | Ours<sub>MFTG</sub> | **26.94** | 20.52 | 22.51 | 24.96 | 25.02 | 26.91 | 26.11 | **30.41** | 23.55 | 20.03 | 24.70 |
| | Ours<sub>MSMG</sub> | 26.73 | 21.35 | 23.23 | 26.52 | **26.27** | **27.15** | **26.83** | 30.06 | 25.01 | 20.61 | 25.38 |
| | Ours<sub>OMMG</sub> | 26.46 | **22.28** | **23.31** | **27.17** | 25.88 | 26.33 | 26.72 | 29.86 | **26.16** | **22.27** | **25.64** |
| | <font color="blue">gsplat</font> | <font color="blue">26.27</font> | <font color="blue">19.07</font> | <font color="blue">21.26</font> | <font color="blue">26.37</font> | <font color="blue">24.86</font> | <font color="blue">26.78</font> | <font color="blue">25.37</font> | <font color="blue">29.73</font> | <font color="blue">22.08</font> | <font color="blue">19.47</font> | <font color="blue">24.13</font> |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **SSIM ↑** | 3DGS | 0.860 | × | × | × | 0.717 | 0.872 | 0.810 | × | × | × | × |
| | ThermoNeRF | 0.747 | 0.759 | 0.694 | 0.781 | 0.750 | 0.916 | 0.804 | 0.717 | 0.709 | 0.774 | 0.765 |
| | 3DGS+MI | 0.889 | 0.789 | 0.806 | 0.917 | 0.872 | 0.922 | 0.872 | 0.887 | 0.843 | 0.794 | 0.859 |
| | Ours<sub>MFTG</sub> | **0.890** | 0.798 | 0.845 | 0.906 | **0.880** | 0.920 | 0.886 | 0.895 | 0.859 | 0.808 | 0.869 |
| | Ours<sub>MSMG</sub> | 0.891 | 0.829 | 0.857 | 0.909 | 0.879 | **0.926** | **0.897** | **0.898** | 0.860 | 0.832 | 0.878 |
| | Ours<sub>OMMG</sub> | 0.886 | **0.835** | **0.862** | **0.919** | 0.874 | 0.922 | 0.888 | 0.896 | **0.883** | **0.850** | **0.882** |
| | <font color="blue">gsplat</font> | <font color="blue">**0.890**</font> | <font color="blue">0.795</font> | <font color="blue">0.813</font> | <font color="blue">0.905</font> | <font color="blue">0.855</font> | <font color="blue">0.925</font> | <font color="blue">0.872</font> | <font color="blue">0.897</font> | <font color="blue">0.835</font> | <font color="blue">0.773</font> | <font color="blue">0.856</font> |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **LPIPS ↓** | 3DGS | 0.157 | × | × | × | 0.281 | 0.193 | 0.299 | × | × | × | × |
| | ThermoNeRF | 0.312 | 0.494 | 0.290 | 0.293 | 0.291 | 0.170 | 0.234 | 0.152 | 0.309 | 0.264 | 0.280 |
| | 3DGS+MI | 0.124 | 0.274 | 0.313 | 0.204 | 0.139 | 0.125 | 0.211 | 0.093 | 0.252 | 0.328 | 0.206 |
| | Ours<sub>MFTG</sub> | **0.121** | 0.258 | 0.235 | 0.210 | **0.133** | 0.129 | 0.199 | 0.091 | 0.232 | 0.317 | 0.192 |
| | Ours<sub>MSMG</sub> | 0.124 | **0.208** | 0.220 | 0.213 | **0.133** | 0.130 | 0.189 | **0.086** | 0.227 | 0.293 | 0.182 |
| | Ours<sub>OMMG</sub> | 0.129 | 0.210 | **0.203** | **0.198** | 0.136 | **0.124** | **0.177** | 0.091 | **0.181** | **0.248** | **0.170** |
| | <font color="blue">gsplat</font> | <font color="blue">**0.089**</font> | <font color="blue">**0.203**</font> | <font color="blue">0.209</font> | <font color="blue">**0.101**</font> | <font color="blue">**0.114**</font> | <font color="blue">**0.076**</font> | <font color="blue">**0.146**</font> | <font color="blue">**0.058**</font> | <font color="blue">**0.173**</font> | <font color="blue">0.322</font> | <font color="blue">**0.149**</font> |

conclusion: 

The results are generally worse than SOTA results from ThermalGaussian paper. However, for LPIPS metric, the gsplat package achieves superior results across multiple scenes.