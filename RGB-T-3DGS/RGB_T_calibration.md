# task
calibrate the RGB and thermal camera by computing the rotation matrix $R$ and translation vector $t$ that align the two camera coordinate systems, using the paired RGB and thermal images.

RGB-Thermal cameras calibration based on Maximum Index Map
- journal paper: [here](./complementary_literature/RGB-Thermal%20cameras%20calibration%20based%20on%20Maximum%20Index%20Map.pdf)

# Input
RGB and thermal paired images, $\{R_i, T_i\}_{i=1}^N$, where $(R_i,T_i)$ is a pair of RGB and thermal images captured for the same scene.

$$R_i \in \mathbb{R}^{H \times W \times 3}, \quad T_i \in \mathbb{R}^{H \times W}$$

# Formula
$$\begin{bmatrix}
u_{\text{RGB}} \\
v_{\text{RGB}} \\
1
\end{bmatrix} = K_{\text{RGB}} \left( R \cdot K_{\text{Th}}^{-1} \begin{bmatrix}
u_{\text{Th}} \\
v_{\text{Th}}
\end{bmatrix} + t \right)
$$

# Calibration methods
According to Wei et.al, they use a specially designed infrared calibration board to perform intrinsic calibration of the RGB-T cameras, and the extrinsic parameters of the RGB-T cameras can be calibrated online directly from the images captured by the cameras. It uses Maximum Index Map (MIM) to extract features from the RGB and thermal images, and then matches these features to compute the extrinsic parameters.


## step 1: Intrinsic calibration
Given a calibration checkerboard, heat gun was used to maintain thermal difference between the black and white squares. The total radiation detected of the object can be expressed as:
$W = \epsilon W_b + (1 − \epsilon)W_r$ where $\epsilon$ is the emissivity of the object; $W_b$ is the radiation value of a blackbody at the same temperature as the object; and $W_r$ is 
the energy value of environmental reflection.

A significant difference of object emissivity occurs between the black(0.93) and white squares(0.05).

## step 2: Feature extraction and matching
convolve the image with the log-Gabor filter, where 
$
G(s,o)
= \exp\!\left[
  -\frac{1}{2}
  \left(\frac{\rho - \rho_s}{\sigma_\rho}\right)^2
\right]
\exp\!\left[
  -\frac{1}{2}
  \left(\frac{\theta - \theta(s,o)}{\sigma_\theta}\right)^2
\right]
$
Feature detection is then performed by calculating phase consistency (PC), which 
is computed using the equation
$$
PC(x,y) =
\frac{
\displaystyle \sum_{s}\sum_{o}
\omega_o(x,y)\bigl[A_{so}(x,y)\,\Delta\Phi_{so}(x,y) - T\bigr]
}{
\displaystyle \sum_{s}\sum_{o} A_{so}(x,y) + \xi
}
$$

Where $(x, y)$ represents the pixel coordinates of the image; $\xi$ is a small value introduced to avoid division by zero; $T$ is the noise intensity; $A_{so}(x, y)$ represents the intensity information of the image; $\Delta\Phi_{so}(x, y)$ is the phase deviation function; $\omega_o(x, y)$ is the weight function.

This operator is then 
used in a contrast-invariant manner to identify edges and corners. The construction of the covariance data is as follows

$
\operatorname{Covx}(\theta_0) = PC(\theta_0)\cos(\theta_0)
$

$
\operatorname{Covy}(\theta_0) = PC(\theta_0)\sin(\theta_0)
$

$
a = \sum_{o} \operatorname{Covx}(\theta_0)^2
$

$
b = \sum_{o} \operatorname{Covx}(\theta_0)\operatorname{Covy}(\theta_0)
$

$
c = \sum_{o} \operatorname{Covy}(\theta_0)^2
$

Where $PC(\theta_0)$ is the PC mapping for the angle $\theta_0$. The computation of the **maximum** and **minimum** moments is given by: 
$
M = \frac{1}{2}\left(c + a + \sqrt{b^{2} + (a - c)^{2}}\right)
$

$
m = \frac{1}{2}\left(c + a - \sqrt{b^{2} + (a - c)^{2}}\right)
$

The maximum moment M functions as the edge map while the minimum moment m serves for corner detection.

MIM(Maximum Index Map) method also mitigates effect brought by NTR(nonlinear radiation distortion) in RGB cross-modal distortion. It can pick the most relevant features so that it can get more robust to noise. 

$$
A_o(x,y) = \sum_{i=1}^{p} A_{so}(x,y)
$$

$$
MIM(x_j, y_j) = \operatorname*{argmax}_{i=1}^{q} \left\{ A_o^{i}(x_j, y_j) \right\}
$$

Where $A_{so}(x,y)$ represents the filtered image; $A_o(x,y)$ is the image after scale summation; $i$ denotes different channels of the feature sequence; $(x_j, y_j)$ represents any point in $A_o(x,y)$; and $MIM(x_j, y_j)$ is the constructed Maximum Index Map.

Feature points are extracted from the maximum values of MIM.

## step 3: Extrinsic calibration
The 8-point algorithm is used to compute the extrinsic parameters.

1. Compute the two models in parallel:  
Uniformize feature point pairs using a quadtree algorithm. By leveraging the homographic relationship between two planes and the epipolar constraint, the inliers are input to compute the homography matrix and the fundamental matrix as follows:

$
(X_{\text{Thermal}})^{T} F X_{\text{RGB}} = 0
$

$
H X_{\text{RGB}} = X_{\text{Thermal}}
$

Where $X_{\text{RGB}}$ is the homogeneous coordinates of the feature points in the RGB image; $X_{\text{Thermal}}$ is the homogeneous coordinates of the feature points in the thermal image; $F$ is the fundamental matrix; and $H$ is the homography matrix.

2. Select the optimal model:  
The scores $S_F$ and $S_H$ for the fundamental matrix and homography matrix, respectively, are obtained by calculating the bidirectional reprojection errors. Then, the two models are compared using the following equation:

$$
P_H = \frac{S_H}{S_H + S_F}
$$

When $P_H \ge 0.45$, the homography matrix is chosen as the optimal model to avoid degeneration of the 8-point algorithm due to low disparities and coplanar feature points. In other cases, the fundamental matrix is chosen.

3. Recover the extrinsic parameters from the optimal model:  
After obtaining the optimal model, the translation vector $T$ and rotation $R$ are recovered from it. If the optimal model obtained in the second step is the homography matrix, a transformation is applied to eliminate the impact of inconsistent camera intrinsic parameters between the RGB and thermal cameras, as follows:

$
H_N = K_{\text{Thermal}}^{-1} \, H \, K_{\text{RGB}}
$

Where $K_{\text{Thermal}}$ is the intrinsic matrix of the thermal camera, $K_{\text{RGB}}$ is the intrinsic matrix of the RGB camera. The singular value decomposition (SVD) of $H_N$ is performed to obtain the translation and rotation vectors. If the optimal model obtained is the fundamental matrix, the intrinsic matrices of both cameras are used to obtain the essential matrix $E$, as follows:

$
E = K_{\text{Thermal}}^{T} F K_{\text{RGB}}
$
Finally, performing SVD decomposition on the essential matrix yields translation and rotation vectors.

## step 4: Evaluation metric
$
R_{PE} = \sqrt{\bigl(x(i,j) - \hat{x}(i,j)\bigr)^2}
$

$
R_{MSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left(R_{PE}\right)^2}
$

$
M_{AE} = \frac{1}{n} \sum_{i=1}^{n} \left|R_{PE}\right|
$

$
S_{D} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left(R_{PE} - \overline{R_{PE}}\right)^2}
$

Where

$
\hat{x} = \frac{1}{s} K P X
$

$
\overline{R_{PE}} = \frac{1}{n} \sum_{i=1}^{n} R_{PE}
$
Here, 𝑥 represents the 2D coordinates of the feature point; ̂𝑥 represents the 2D coordinates of the feature point after reprojection; 
𝑋 represents the 3D coordinates of the feature point; 𝑃  is the projection matrix; 𝐾 is the camera intrinsic matrix; 𝑠 is the depth of 
the feature point



# Output
The rotation matrix $R$ and translation vector $t$ 

# Reference 
Wei, J., Zou, Z., Lai, W., Du, J., Zhao, J., Liu, Z., & Wang, S. (2025). RGB-Thermal cameras calibration based on Maximum Index Map.

