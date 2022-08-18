from argoverse.map_representation.map_api import ArgoverseMap
from argoverse.data_loading.argoverse_tracking_loader import ArgoverseTrackingLoader
from argoverse.data_loading.argoverse_forecasting_loader import ArgoverseForecastingLoader
avm = ArgoverseMap()
argoverse_tracker_loader = ArgoverseTrackingLoader('argoverse-tracking/')    #simply change to your local path of the data
argoverse_forecasting_loader = ArgoverseForecastingLoader('argoverse-forecasting/') #simply change to your local path of the data