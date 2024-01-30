
fetch("data/")
  .then(response => response.text())
  .then(data => {
    console.log("data", data);
    // 用 DOMParser 來解析 fetch到的 HTML， 變成 可操作的物件
    const parser = new DOMParser();
    const htmlDoc = parser.parseFromString(data, 'text/html');
    console.log("htmlDoc", htmlDoc);

    // 獲取所有a_tags（通常是文件名）
    let a_tags_all = htmlDoc.querySelectorAll('a');
    console.log("a_tags_all", a_tags_all);
    a_tags_all = Array.from(a_tags_all);
    console.log("a_tags_all_array", a_tags_all);
    a_tags_you_want = a_tags_all.slice(3)
    console.log("a_tags_you_want", a_tags_you_want);
    console.log("a_tag", a_tags_you_want);
    console.log("a_tag", a_tags_you_want[0].getElementsByTagName("span")[0].textContent);
    console.log("a_tag", a_tags_you_want[1].getElementsByTagName("span")[0].textContent);
    console.log("a_tag", a_tags_you_want[2].getElementsByTagName("span")[0].textContent);
    console.log("a_tag", a_tags_you_want[3].getElementsByTagName("span")[0].textContent);
    console.log("a_tag", a_tags_you_want[4].getElementsByTagName("span")[0].textContent);

    let GeoJSONboatfileNames = a_tags_you_want.map(a_tag => a_tag.getElementsByTagName("span")[0].textContent);
    console.log("GeoJSONboatfileNames", GeoJSONboatfileNames);

    // 過濾出你想要的文件名，例如只獲取以 '.geojson' 结尾的文。件名
    let GeoJSONboatfiles = GeoJSONboatfileNames.filter(GEOfileName => GEOfileName.endsWith('.geojson'));
    console.log(GeoJSONboatfiles); // 在控制台輸出文件名列表
  })

