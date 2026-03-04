#!/bin/bash
#SBATCH --job-name=RGBT_Scenes_experiment
#SBATCH --partition=ba100,brtx6,brtx6-ir,brtx-pod
#SBATCH --gpus=1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=24:00:00
#SBATCH --mail-type=all
#SBATCH --mail-user=ylu174@alumni.jhu.edu
#SBATCH --output=../SLURM_output/%x_%j.out            # Stdout file (%x=job name, %j=job ID)
#SBATCH --error=../SLURM_outcome/%x_%j.err             # Stderr file


RECORD_FILE="time_record_${SLURM_JOB_ID}.txt"
echo $RECORD_FILE

source /brtx/605-nvme2/ylu174/Anaconda3/etc/profile.d/conda.sh
conda activate gsplat


# record start time
cd "$(git rev-parse --show-toplevel)/SLURM_execution/SLURM_outcome"
START_TS=$(date +%s)
start_time=$(python -c "import time; print(time.time())")

python -c "import time; print(f'🚀 Job Started at: {time.strftime(\"%Y-%m-%d %H:%M:%S\")}')"
python3 <<EOF
import os
from datetime import datetime
with open("$RECORD_FILE", "a") as f:
    start_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"{'='*50}\nJob: $SLURM_JOB_NAME (ID: $SLURM_JOB_ID)\nStart: {start_str}\n")
EOF

# train the benchmark model
cd "$(git rev-parse --show-toplevel)/examples"
bash benchmarks/RGB-thermal/RGBT-Scenes_rgb_3DGS.sh
# sleep 5

# record end time and duration
cd "$(git rev-parse --show-toplevel)/SLURM_execution/SLURM_outcome"
END_TS=$(date +%s)
DURATION=$(( END_TS - START_TS ))


end_time=$(python -c "import time; print(time.time())")
python3 <<EOF
import time
start = float("$start_time")
end = float("$end_time")
delta = end - start
print(f"🏁 Job Finished at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"⏱️ Total Duration: {delta/3600:.2f} hours ({delta:.2f} seconds)")


import os
from datetime import datetime
duration_sec = $DURATION
with open("$RECORD_FILE", "a") as f:
    end_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"End: {end_str}\n")
    f.write(f"Duration: {duration_sec/60:.2f} min ({duration_sec} sec)\n")
    f.write(f"Status: Completed\n{'='*50}\n")
EOF