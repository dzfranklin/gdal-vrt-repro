#!/usr/bin/env python3
import rasterio
ds: rasterio.DatasetReader = rasterio.open("index.vrt", masked=True)
val = list(ds.sample([(0, 51.4)]))[0][0]
print(val)
