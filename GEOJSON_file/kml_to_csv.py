import xml.etree.ElementTree as ET
import csv
import pandas
import shutil
import os
import time
import keyboard
import threading


def kml_to_csv(src_path, dst_path):
    # 读取 KML 文件
    tree = ET.parse(src_path)
    root = tree.getroot()
    namespaces = {
    'gx': 'http://www.google.com/kml/ext/2.2'
    }
    go = root.find(".//Document/Folder/GroundOverlay", namespaces=namespaces)
    if go is not None:
        if coords := go.find(".//gx:LatLonQuad/coordinates", namespaces=namespaces):
            print(coords.text)
    else:
        print("GroundOverlay not found under Folder.")

    # 提取坐标信息
    coordinates_str  = coords.text
    coordinates_list = [float(coord) for pair in coordinates_str.split() for coord in pair.split(',')]
    headers = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4']
    if  os.path.exists(dst_path):
        with open(dst_path, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(coordinates_list)
    else:
        with open(dst_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(headers)
            csv_writer.writerow(coordinates_list)

def dir_kml_to_csv(src_dir,finish_dir,dst_dir):
    if(os.path.isdir(src_dir) is False):
        print("src_dir 不存在，請輸入正確src_dir")
        return
    
    file_names = [file_name for file_name in os.listdir(src_dir) if (".kml" in file_name.lower())]
    for file_name in file_names:
        half_name = file_name.split(".")[0]  ### 取得 file_name 檔名部分
        extd_name = file_name.split(".")[1]  ### 取得 file_name 副檔名，其實可以指定"kml"就好，但我習慣寫得有彈性一點
        time_name = half_name.split("_")[4]  ### 取得日期時間
        date_name = time_name[:8]
        src_path    = f"{src_dir}/{half_name}.{extd_name}"  ### 拼出 src_path：來源資料夾/檔名.副檔名(csv)
        finish_path = f"{finish_dir}/{half_name}.{extd_name}"
        dst_path    = f"{dst_dir}/{date_name}_area.csv" 
        kml_to_csv(src_path, dst_path)
        shutil.move(src_path, finish_path)
        
src_dir    = "GEOJSON_file/data/"
dst_dir    = "GEOJSON_file/data/"
finish_dir = "GEOJSON_file/data/finish/"

#自動執行
def execute_dir_kml_to_csv():
    global stop_flag
    global pause_flag
    stop_flag  = False
    pause_flag = False 
    while not stop_flag:
        while not pause_flag:
            dir_kml_to_csv(src_dir=src_dir, finish_dir=finish_dir, dst_dir=dst_dir)
            
geojson_thread = threading.Thread(target=execute_dir_kml_to_csv)
geojson_thread.start()

while True:
    if keyboard.is_pressed("p"):
        if  pause_flag:
            pause_flag = False
            print("繼續運行，按下 'P' 鍵暫停")
        else:
            pause_flag = True
            print("暫停運行，按下 'P' 鍵繼續")
    if keyboard.is_pressed("s"):
        stop_flag = True
        print("停止運行")
        break
    time.sleep(0.1)