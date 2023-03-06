// 总览结点分布
function draw_pie_nodes_total(data) {
  // 处理数据
  var dataset = []
  var legendList = []
  for (var i in data) {
    dataset.push({ name: i, value: data[i] })
    legendList.push(i)
  }
  console.log(dataset)

  document.getElementById("node_container").innerHTML = ""
  var dom = document.getElementById('node_container');
  dom.removeAttribute('_echarts_instance_')
  // 样式设置
  let theme_obj = theme_purple()
  echarts.registerTheme('theme_purple', theme_obj)
  var myChart = echarts.init(dom, 'theme_purple');

  myChart.clear(this.option);

  var option;

  myChart.hideLoading()

  option = {
    tooltip: {
      trigger: 'item',
      // formatter: '{b}: {c} ({d}%)',
    },
    title: {
      text: "Total Node Distribution",
      top: '0%',
      padding: [20, 0, 0, 50]
    },
    legend: [{
      top: '5%',
      left: 'right',
      data: legendList.slice(0, (legendList.length) / 2)
    },
    {
      top: '15%',
      left: 'right',
      data: legendList.slice((legendList.length) / 2, legendList.length)
    }
    ],
    series: [
      {
        // name: 'Access From',
        type: 'pie',
        radius: ['30%', '60%'],
        center: ['50%', '65%'],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 5,
          borderColor: 'rgba(91,92,110,1)',
          borderWidth: 1
        },
        avoidLabelOverlap: true,
        label: {
          alignTo: 'edge',
          formatter: '{b} : {c} ({d}%)\n',
          minMargin: 2,
          edgeDistance: 50,
          lineHeight: 13
        },
        labelLine: {
          length: 10,
          length2: 0,
          maxSurfaceAngle: 100
        },
        labelLayout: function (params) {
          console.log(params)
          const isLeft = params.labelRect.x < myChart.getWidth() / 2;
          const points = params.labelLinePoints;
          // Update the end point.
          points[2][0] = isLeft
            ? params.labelRect.x
            : params.labelRect.x + params.labelRect.width;
          return {
            labelLinePoints: points,

          };
        },
        data: dataset
      }
    ]
  };
  myChart.setOption(option);

  if (option && typeof option === 'object') {
    myChart.setOption(option);
  }

  window.addEventListener('resize', myChart.resize);
}

// 子图结点分布
function draw_pie_nodes_subgraph(data) {
  // 处理数据
  var dataset = []
  var legendList = []
  for (var i in data) {
    dataset.push({ name: i, value: data[i] })
    legendList.push(i)
  }
  console.log(dataset)

  document.getElementById("node_container").innerHTML = ""
  var dom = document.getElementById('node_container');
  dom.removeAttribute('_echarts_instance_')
  // 样式设置
  let theme_obj = theme_purple()
  echarts.registerTheme('theme_purple', theme_obj)
  var myChart = echarts.init(dom, 'theme_purple');

  myChart.clear(this.option);

  var option;

  myChart.hideLoading()

  option = {
    tooltip: {
      trigger: 'item',
      // formatter: '{b}: {c} ({d}%)',
    },
    title: {
      text: "Subgraph Node Distribution",
      top: '0%',
      padding: [20, 0, 0, 50]
    },
    legend: [{
      top: '5%',
      left: 'right',
      data: legendList.slice(0, (legendList.length) / 2)
    },
    {
      top: '15%',
      left: 'right',
      data: legendList.slice((legendList.length) / 2, legendList.length)
    }
    ],
    series: [
      {
        // name: 'Access From',
        type: 'pie',
        radius: ['30%', '60%'],
        center: ['50%', '65%'],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 5,
          borderColor: 'rgba(91,92,110,1)',
          borderWidth: 1
        },
        avoidLabelOverlap: true,
        label: {
          alignTo: 'edge',
          formatter: '{b} : {c} ({d}%)\n',
          minMargin: 2,
          edgeDistance: 50,
          lineHeight: 13
        },
        labelLine: {
          length: 10,
          length2: 10,
          maxSurfaceAngle: 100
        },
        labelLayout: function (params) {
          console.log(params)
          const isLeft = params.labelRect.x < myChart.getWidth() / 2;
          const points = params.labelLinePoints;
          // Update the end point.
          points[2][0] = isLeft
            ? params.labelRect.x
            : params.labelRect.x + params.labelRect.width;
          return {
            labelLinePoints: points,

          };
        },
        data: dataset
      }
    ]
  };
  myChart.setOption(option);

  if (option && typeof option === 'object') {
    myChart.setOption(option);
  }

  window.addEventListener('resize', myChart.resize);
}

// 总览脏Domain分布
function draw_pie_domain_total(data) {
  // 处理数据
  var dataset = []
  var legendList = []
  for (var i in data) {
    dataset.push({ name: i, value: data[i] })
    legendList.push(i)
  }
  console.log(dataset)

  document.getElementById("domain_container").innerHTML = ""
  var dom = document.getElementById('domain_container');
  dom.removeAttribute('_echarts_instance_')
  // 样式设置
  let theme_obj = theme_purple()
  echarts.registerTheme('theme_purple', theme_obj)
  var myChart = echarts.init(dom, 'theme_purple');

  myChart.clear(this.option);

  var option;

  myChart.hideLoading()

  option = {
    tooltip: {
      trigger: 'item',
      // formatter: '{b}: {c} ({d}%)',
    },
    title: {
      text: "Total Dirty Domain Distribution",
      top: '0%',
      padding: [20, 0, 0, 50]
    },
    legend: [{
      top: '5%',
      left: 'right',
      data: legendList.slice(0, (legendList.length) / 2)
    },
    {
      top: '15%',
      left: 'right',
      data: legendList.slice((legendList.length) / 2, legendList.length)
    }
    ],
    series: [
      {
        type: 'pie',
        radius: ['30%', '60%'],
        center: ['50%', '65%'],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 5,
          borderColor: 'rgba(91,92,110,1)',
          borderWidth: 1
        },
        avoidLabelOverlap: true,
        label: {
          alignTo: 'edge',
          formatter: '{b} : {c} ({d}%)\n',
          minMargin: 2,
          edgeDistance: 50,
          lineHeight: 13
        },
        labelLine: {
          length: 10,
          length2: 10,
          maxSurfaceAngle: 100
        },
        labelLayout: function (params) {
          console.log(params)
          const isLeft = params.labelRect.x < myChart.getWidth() / 2;
          const points = params.labelLinePoints;
          // Update the end point.
          points[2][0] = isLeft
            ? params.labelRect.x
            : params.labelRect.x + params.labelRect.width;
          return {
            labelLinePoints: points,

          };
        },
        data: dataset
      }
    ]
  };
  myChart.setOption(option);

  if (option && typeof option === 'object') {
    myChart.setOption(option);
  }

  window.addEventListener('resize', myChart.resize);
}

// 子图脏Domain分布
function draw_pie_domain_subgraph(data) {
  // 处理数据
  var dataset = []
  var legendList = []
  for (var i in data) {
    dataset.push({ name: i, value: data[i] })
    legendList.push(i)
  }
  console.log(dataset)

  document.getElementById("domain_container").innerHTML = ""
  var dom = document.getElementById('domain_container');
  dom.removeAttribute('_echarts_instance_')
  // 样式设置
  let theme_obj = theme_purple()
  echarts.registerTheme('theme_purple', theme_obj)
  var myChart = echarts.init(dom, 'theme_purple');

  myChart.clear(this.option);

  var option;

  myChart.hideLoading()

  option = {
    tooltip: {
      trigger: 'item',
    },
    title: {
      text: "Subgraph Dirty Domain Distribution",
      top: '0%',
      padding: [20, 0, 0, 50]
    },
    legend: [{
      top: '5%',
      left: 'right',
      data: legendList.slice(0, (legendList.length) / 2)
    },
    {
      top: '15%',
      left: 'right',
      data: legendList.slice((legendList.length) / 2, legendList.length)
    }
    ],
    series: [
      {
        type: 'pie',
        radius: ['30%', '60%'],
        center: ['50%', '65%'],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 5,
          borderColor: 'rgba(91,92,110,1)',
          borderWidth: 1
        },
        avoidLabelOverlap: true,
        label: {
          alignTo: 'edge',
          formatter: '{b} : {c} ({d}%)\n',
          minMargin: 2,
          edgeDistance: 50,
          lineHeight: 13
        },
        labelLine: {
          length: 10,
          length2: 10,
          maxSurfaceAngle: 100
        },
        labelLayout: function (params) {
          console.log(params)
          const isLeft = params.labelRect.x < myChart.getWidth() / 2;
          const points = params.labelLinePoints;
          // Update the end point.
          points[2][0] = isLeft
            ? params.labelRect.x
            : params.labelRect.x + params.labelRect.width;
          return {
            labelLinePoints: points,

          };
        },
        data: dataset
      }
    ]
  };
  myChart.setOption(option);

  if (option && typeof option === 'object') {
    myChart.setOption(option);
  }

  window.addEventListener('resize', myChart.resize);
}


function showOverall(){
  draw_pie_nodes_total(total_nodes_distribution)
  draw_pie_domain_total(dirty_domain_distribution)
}