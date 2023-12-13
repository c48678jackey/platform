from pykml import parser

# # 读取 KML 文件
# with open('GEOJSON_file/data/20231118_a.kml') as f:
#     kml_doc = parser.parse(f).getroot()

# # 提取坐标信息
# coordinates_str = kml_doc.Document.Folder.GroundOverlay.coordinates.text

# coordinates_list = [float(coord) for pair in coordinates_str.split() for coord in pair.split(',')]

with open("GEOJSON_file/data/20231118_a.kml") as f:
        kml_doc = parser.parse(f).getroot()

    # 提取坐标信息
coordinates_str  = kml_doc.Document.Folder.GroundOverlay.coordinates.text
coordinates_list = [float(coord) for pair in coordinates_str.split() for coord in pair.split(',')]
print(coordinates_list)
