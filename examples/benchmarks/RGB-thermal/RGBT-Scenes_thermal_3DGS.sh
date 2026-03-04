SCENE_DIR="data/RGBT-Scenes"
# RESULT_DIR="results/RGBT-Scenes/thermal"
RESULT_DIR="results_60k/RGBT-Scenes/thermal"
SCENE_LIST="Building DailyStuff Dimsum Ebike IronIngot LandScape Parterre RoadBlock RotaryKiln Truck"
# SCENE_LIST="LandScape"
RENDER_TRAJ_PATH="ellipse"

for SCENE in $SCENE_LIST;
do
	mkdir -p $RESULT_DIR/$SCENE
    DATA_FACTOR=1
    echo "Running $SCENE"

    # train without eval
    CUDA_VISIBLE_DEVICES=0 python simple_trainer_RGBT_Scenes.py default --eval_steps -1 --disable_viewer --data_factor $DATA_FACTOR \
        --render_traj_path $RENDER_TRAJ_PATH \
        --data_dir $SCENE_DIR/$SCENE/ \
        --result_dir $RESULT_DIR/$SCENE/ \
		--image_type thermal \
		--max_steps 60000 \
		--save_ply

    # run eval and render
    for CKPT in $RESULT_DIR/$SCENE/ckpts/*;
    do
        CUDA_VISIBLE_DEVICES=0 python simple_trainer_RGBT_Scenes.py default --disable_viewer --data_factor $DATA_FACTOR \
            --render_traj_path $RENDER_TRAJ_PATH \
            --data_dir $SCENE_DIR/$SCENE/ \
            --result_dir $RESULT_DIR/$SCENE/ \
            --ckpt $CKPT \
			--image_type thermal \
			--save_ply
    done
done


for SCENE in $SCENE_LIST;
do
    echo "=== Eval Stats ==="

    for STATS in $RESULT_DIR/$SCENE/stats/val*.json;
    do  
        echo $STATS
        cat $STATS; 
        echo
    done

    echo "=== Train Stats ==="

    for STATS in $RESULT_DIR/$SCENE/stats/train*_rank0.json;
    do  
        echo $STATS
        cat $STATS; 
        echo
    done
done