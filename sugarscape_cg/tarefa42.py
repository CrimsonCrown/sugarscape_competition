from sugarscape_cg.model import SugarscapeCg
from mesa import batch_run
import pandas as pd
import numpy as np
from datetime import datetime

params={"width":50, "height":50, "initial_population":100, "initial_population2": range(0,201,50)}

results=batch_run(
	SugarscapeCg,
	parameters=params,
	iterations=100,
	max_steps=50,
	number_processes=1,
	data_collection_period=-1,
	display_progress=True,
)

results_df=pd.DataFrame(results)

results_df.to_csv(datetime.now().strftime("%Y_%m_%d_%H_%M_%S_")+"experimento.csv")