Lit. Survey on Thermal Imaging
## paper
1. R. Lu et al. ThermalGaussian: Thermal 3D Splatting. ICLR 2025
https://arxiv.org/pdf/2409.07200

2. Z. Gu and B. Wang. MMOne: Representing Multiple Modalities in One Scene. ICCV 2025
explanation: Optimization-based thermal reconstruction – has nodes for single-modal and multi-modal.
https://arxiv.org/pdf/2507.11129

3. NTR-Gaussian: Nighttime Dynamic Thermal Reconstruction with 4D Gaussian Splatting Based on Thermodynamics. CVPR 2025
https://arxiv.org/pdf/2503.03115

4. SIGGRAPH Asia 2025 paper – this actually seems good, uses 2DGS to render and talks about thermal-specific parameters. We can use this formulation, but it’s still optimization-based.
https://arxiv.org/pdf/2511.13011

5. There is mesh, 3D point cloud and thermal images, remote sensing perspective (not sure how useful)
https://arxiv.org/pdf/2503.22060

6. Surveys datasets in the area. Thermal is useful for driving as well.
https://dl.acm.org/doi/pdf/10.1145/3757377.3763938

## dataset
1. RGBT-Scenes dataset, handheld thermal camera, many views, very few (14) scenes.
https://arxiv.org/pdf/2007.03262

2. NTR dataset, considered convective heat transfer
https://github.com/NPU-CVPG/NTR-Gaussian

3. TI-NSD dataset
https://arxiv.org/pdf/2409.08042

4. ThermoNeRF dataset: Thermonerf: Multimodal neural radiance fields for thermal novel view synthesis
https://arxiv.org/pdf/2403.12154

5. RGBT-LOW dataset: Focus on low-light situations. RGBT-LOW dataset contain 20 scenes with 6000 images.
https://arxiv.org/abs/2406.14482

6. Multi-spectral dataset: W. Dai, Y. Zhang, S. Chen, D. Sun, and D. Kong, 
A multi-spectral dataset for evaluating motion estimation systems, in Proc. IEEE Int. Conf. Robot. Autom. (ICRA), 
May 2021, pp. 5560–5566.
https://arxiv.org/pdf/2007.00622
http://github.com/NGCLAB/multi-spectral-dataset

7. ViVID++ dataset: A. J. Lee, Y. Cho, Y.-S. Shin, A. Kim, and H. Myung, 
ViViD++: Vision for visibility dataset, IEEE Robot. Autom. Lett., vol. 7, no. 3, pp. 6282–6289, Jul. 2022
https://dl.acm.org/doi/pdf/10.1145/3737905.3769282 might be worth reading a bit more.
https://arxiv.org/pdf/2204.06183

