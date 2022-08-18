from argoverse.visualization.visualize_sequences import viz_sequence
seq_path = f"/home/be-happy/GSC/forecasting_test_v1.1/val/data/1.csv"
viz_sequence(afl.get(seq_path).seq_df, show=True)