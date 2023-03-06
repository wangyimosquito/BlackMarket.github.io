function draw_pie(json_name){
    let theme_obj = theme_purple()
    document.getElementById("type-container").innerHTML = ""
    var dom = document.getElementById('type-container');
    dom.removeAttribute('_echarts_instance_')
    echarts.registerTheme('theme_purple', theme_obj)
    var myChart = echarts.init(dom, 'theme_purple', {
      // renderer: 'canvas',
      // useDirtyRect: false
    });
    myChart.clear(this.option);
    var app = {};
    var option;

    $.get(json_name, function (webkitDep){
        myChart.hideLoading();
        console.log(webkitDep.nodes.length)
        name_list = ["Domain", "IP", "Cert", "Whois_Info", "IP_Info"]
        num_list = [0, 0, 0, 0, 0]
        for (let i=0; i<webkitDep.nodes.length; i++) {
            if (webkitDep.nodes[i].name == name_list[0]){
                num_list[0] += 1
            } else if (webkitDep.nodes[i].name == name_list[1]){
                num_list[1] += 1
            } else if (webkitDep.nodes[i].name == name_list[2]){
                num_list[2] += 1
            } else if (webkitDep.nodes[i].name == "Whois_Name" |
            webkitDep.nodes[i].name == "Whois_Email" |
            webkitDep.nodes[i].name == "Whois_Phone"){
                num_list[3] += 1
            } else {
                num_list[4] += 1
            }
        }

        option = {
            tooltip: {
                trigger: 'item',
                // formatter: '{b}: {c} ({d}%)',
            },
            title : {
                text: "Node Type Distribution",
                padding: [20, 0, 0, 50]
            },
            legend: [{
                top: '5%',
                padding: [10, 65, 20, 20],
                // orient: 'vertical',
                left: 'right',
                data: ["Domain", "IP", "Cert"]
            },
            {
              top: '15%',
              padding: [10, 65, 20, 20],
              // orient: 'vertical',
              left: 'right',
              data: ["Whois_Info", "IP_Info"]
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
                // label: {
                //     formatter: '{b}: {d}%',
                //     // show: false,
                //     position: 'outside',
                //     alignTo: 'labelLine'
                // },
                avoidLabelOverlap: true,
                label: {
                    alignTo: 'edge',
                    formatter: '{b} : {c} ({d}%)\n',
                    minMargin: 2,
                    edgeDistance: 100,
                    lineHeight: 15
                    // rich: {
                    //   time: {
                    //     fontSize: 10,
                    //     color: '#999'
                    //   }
                    // }
                  },
                  labelLine: {
                    length: 10,
                    length2: 10,
                    maxSurfaceAngle: 100
                  },
                  labelLayout: function (params) {
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
                data: [
                    { value: num_list[0], name: name_list[0] },
                    { value: num_list[1], name: name_list[1] },
                    { value: num_list[2], name: name_list[2] },
                    { value: num_list[3], name: name_list[3] },
                    { value: num_list[4], name: name_list[4] }
                ]
                }
            ]
            };
        myChart.setOption(option);
    });

    if (option && typeof option === 'object') {
        myChart.setOption(option);
    }

    window.addEventListener('resize', myChart.resize);
}

function draw_pie_core(json_name){
  let theme_obj = theme_purple_invert()
  document.getElementById("type-container").innerHTML = ""
  var dom = document.getElementById('type-container')
  dom.removeAttribute('_echarts_instance_')
  echarts.registerTheme('theme_purple_invert', theme_obj)
  var myChart = echarts.init(dom, 'theme_purple_invert', {
    // renderer: 'canvas',
    // useDirtyRect: false
  });
  myChart.clear(this.option);
  var app = {};
  var option;

  $.get(json_name, function (webkitDep){
      myChart.hideLoading();
      console.log(webkitDep.nodes.length)
      name_list = ['Core Property', 'Other Property']
      num_list = [0, 0]
      for (let i=0; i<webkitDep.nodes.length; i++) {
          if (webkitDep.nodes[i].name == name_list[0]){
              num_list[0] += 1
          } else {
              num_list[1] += 1
          }
      }

      option = {
          tooltip: {
              trigger: 'item',
              // formatter: '{b}: {c} ({d}%)',
          },
          title : {
              text: "Node Type Distribution",
              padding: [20, 0, 0, 50]
          },
          legend: {
              top: '5%',
              padding: [10, 65, 20,20],
              // orient: 'vertical',
              left: 'right'
          },
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
              // label: {
              //     formatter: '{b}: {d}%',
              //     // show: false,
              //     position: 'outside',
              //     alignTo: 'labelLine'
              // },
              avoidLabelOverlap: true,
              label: {
                  alignTo: 'edge',
                  formatter: '{b} : {c} ({d}%)\n',
                  minMargin: 2,
                  edgeDistance: 60,
                  lineHeight: 15
                  // rich: {
                  //   time: {
                  //     fontSize: 10,
                  //     color: '#999'
                  //   }
                  // }
                },
                labelLine: {
                  length: 10,
                  length2: 10,
                  maxSurfaceAngle: 100
                },
                labelLayout: function (params) {
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
              data: [
                  { value: num_list[0], name: name_list[0] },
                  { value: num_list[1], name: name_list[1] }
              ]
              }
          ]
          };
      myChart.setOption(option);
  });

  if (option && typeof option === 'object') {
      myChart.setOption(option);
  }

  window.addEventListener('resize', myChart.resize);
}

function draw_bar(dict){
    let theme_obj = theme_purple()
    var dom = document.getElementById('dark-container');
    echarts.registerTheme('theme_purple', theme_obj)
    var myChart = echarts.init(dom, 'theme_purple', {
      renderer: 'canvas',
      useDirtyRect: false
    });
    var app = {};
    var option;
    console.log(dict)
    
    option = {
        title : {
            text: "Industry Type Distribution",
            padding: [20, 0, 0, 50]
        },
        dataset: [
          {
            dimensions: ['name', 'num'],
            source: [
              ['Erotic', dict['A']],
              ['Gambling', dict['B']],
              ['Scam', dict['C']],
              ['Drug', dict['D']],
              ['Gun', dict['E']],
              ['Hacker', dict['F']],
              ['Illegal Trade', dict['G']],
              ['Illegal Payment', dict['H']],
              ['Other', dict['I']]
            ]
          },
          {
            transform: {
              type: 'sort',
              config: { dimension: 'num', order: 'desc' }
            }
          }
        ],
        tooltip: {
            trigger: 'axis',
            position: 'top',
            textStyle: {
                fontSize: 10
            }
        },
        xAxis: {
          type: 'category',
          axisLabel: { interval: 0, rotate: 20 }
        },
        yAxis: {},
        series: {
          type: 'bar',
          encode: { x: 'name', y: 'num' },
          datasetIndex: 1,
          legendHoverLink: true
        }
      };
      
    option && myChart.setOption(option);
}