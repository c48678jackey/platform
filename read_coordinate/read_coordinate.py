import rasterio

# 打開 GeoTIFF 文件
with rasterio.open('read_coordinate/123.tif') as dataset:
    # 獲取左上角座標和右下角座標
    left, top = dataset.transform * (0, 0)
    right, bottom = dataset.transform * (dataset.width, dataset.height)

print("左上角座標 (左經度, 上緯度):", left, top)
print("右下角座標 (右經度, 下緯度):", right, bottom)

with rasterio.open('read_coordinate/pp.png') as dataset:
    # 獲取左上角座標和右下角座標
    left, top = dataset.transform * (0, 0)
    right, bottom = dataset.transform * (dataset.width, dataset.height)

print("左上角座標 (左經度, 上緯度):", left, top)
print("右下角座標 (右經度, 下緯度):", right, bottom)