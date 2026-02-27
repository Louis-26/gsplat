# environment configuration
## prerequisites 
insert a table here
python version | environment | GPU |  pytorch version | cuda version | Operating System
--- | --- | --- | --- | --- | ---
3.10 | conda | NVIDIA GPU Quadro RTX 6000 | 2.0.0 | 11.8 | Linux 

## configuration step
step 1: create conda environment and activate
```bash
conda create -n gsplat python=3.10 -y
conda activate gsplat
```

step 2: ensure cuda 11.8, and install pytorch(version 2.0.0) with cuda 11.8 support
```bash
conda remove cuda-toolkit cuda-nvcc cuda-compiler cuda-cudart cuda-libraries-dev -y  
conda install -c nvidia cuda-nvcc=11.8.89 cuda-toolkit=11.8.0 cuda-runtime=11.8.0 cuda-cccl=11.8 -y
pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
# configure
export PATH=~/Anaconda3/envs/gsplat/bin:$PATH
export CUDA_HOME=~/Anaconda3/envs/gsplat
```

verify pytorch/CUDA installation, and version
```bash
nvcc --version # should be 11.8
python -c "import torch; print('Torch Version:', torch.__version__); print('CUDA Version:', torch.version.cuda); print('CUDA Available:', torch.cuda.is_available())" # should show torch 2.0.0, cuda 11.8, and cuda available True
ls $CONDA_PREFIX/include/thrust # should give headers
```

step 3: install dependencies and gsplat package
```bash
pip install ninja numpy jaxtyping rich

pip install gsplat --index-url https://docs.gsplat.studio/whl/pt20cu118
```

step 4: install example dependencies
```bash
cd examples
pip install -r requirements.txt --no-build-isolation
mkdir -p gsplat/cuda/csrc/third_party/glm
git clone https://github.com/g-truc/glm.git gsplat/cuda/csrc/third_party/glm
pip install -e . --no-build-isolation
```

complementary step:
```bash
find . -name ".git" 
cd ./gsplat/cuda/csrc/third_party/
rm -rf .git
cd $(git rev-parse --show-toplevel)
grep -qxF "/gsplat/cuda/csrc/third_party/" .gitignore || echo "/gsplat/cuda/csrc/third_party/" >> .gitignore 
grep -qxF "/git_script/" .gitignore || echo "/git_script/" >> .gitignore 
```

## demo
```bash
# ensure environment variables are set
conda activate gsplat
export PATH=~/Anaconda3/envs/gsplat/bin:$PATH
export CUDA_HOME=~/Anaconda3/envs/gsplat

# if dataset is not available
python datasets/download_dataset.py
bash benchmarks/basic.sh
```

use SLURM to run:
```bash
cd "$(git rev-parse --show-toplevel)/SLURM_execution/SLURM_script" && sbatch benchmark_experiment_script.sh
```