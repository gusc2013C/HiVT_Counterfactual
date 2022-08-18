from argoverse.data_loading.argoverse_forecasting_loader import ArgoverseForecastingLoader
from argoverse.visualization.visualize_sequences import viz_sequence

root_dir = '/home/be-happy/GSC/forecasting_test_v1.1/val/data/'
afl = ArgoverseForecastingLoader(root_dir)
print(argoverse_forecasting_data)
seq_path = f"{root_dir}/1.csv"
viz_sequence(afl.get(seq_path).seq_df, show=True)