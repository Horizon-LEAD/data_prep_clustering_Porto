import pandas as pd

def start(fin_orders, fin_CPs):
	df = pd.read_excel(fin_orders)
	df = df.dropna(subset=['CP'])
	#print(df.head())
	#print(df.columns)

	# find Porto CPs and fill delivery lat, delivery long columns
	cp = pd.read_excel(fin_CPs)
	#print(cp.head())
	df_sortCP= df.sort_values(by=['CP'])
	df_lat_long = df_sortCP.join(cp, lsuffix='CP', rsuffix='cp7')
	df_lat_long = df_lat_long.dropna(subset=['lat']) # remove rows with lat = NaN
	df_lat_long['delivery latitude'] = df_lat_long['lat']
	df_lat_long['delivery longtitude'] = df_lat_long['long']
	df_lat_long.drop('lat', inplace=True, axis=1)
	df_lat_long.drop('long', inplace=True, axis=1)
	df = df_lat_long

	return df