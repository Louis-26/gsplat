step 1: create conda environment and activate
```bash
conda create -n gsplat python=3.10 -y
conda activate gsplat
```

step 2: install pytorch(version 2.0.0) with cuda 11.8 support
```bash
conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia -y

```

verify pytorch/CUDA installation, and version
```bash
python -c "import torch; print('Torch Version:', torch.__version__); print('CUDA Version:', torch.version.cuda); print('CUDA Available:', torch.cuda.is_available())"
```

step 3: install dependencies and gsplat package
```bash
pip install ninja numpy jaxtyping rich

pip install gsplat --index-url https://docs.gsplat.studio/whl/pt20cu118
```

step 4: verify gsplat installation
```bash
cd examples
pip install -r requirements.txt
```