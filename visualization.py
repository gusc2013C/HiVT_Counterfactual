from argoverse.map_representation.map_api import ArgoverseMap
from argoverse.data_loading.argoverse_tracking_loader import ArgoverseTrackingLoader
from argoverse.data_loading.argoverse_forecasting_loader import ArgoverseForecastingLoader
avm = ArgoverseMap()
argoverse_forecasting_loader = ArgoverseForecastingLoader('/home/be-happy/GSC/argoverse-forecasting/') #simply change to your local path of the data

python visualize_30hz_benchmark_data_on_map.py --dataset_dir /home/be-happy/GSC/forecasting_test_v1.1/ --log_id 1 --experiment_prefix output
python eval.py --root /home/be-happy/GSC/forecasting_test_v1.1/ --batch_size 32 --ckpt_path ./checkpoints/HiVT-128/checkpoints/epoch=63-step=411903.ckpt